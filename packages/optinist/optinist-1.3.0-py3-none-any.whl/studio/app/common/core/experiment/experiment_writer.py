import os
import shutil
from dataclasses import asdict
from datetime import datetime
from typing import Dict

import yaml

from studio.app.common.core.experiment.experiment import ExptConfig, ExptFunction
from studio.app.common.core.experiment.experiment_builder import ExptConfigBuilder
from studio.app.common.core.experiment.experiment_reader import ExptConfigReader
from studio.app.common.core.utils.config_handler import ConfigWriter
from studio.app.common.core.utils.filepath_creater import join_filepath
from studio.app.common.core.workflow.workflow import NodeRunStatus, WorkflowRunStatus
from studio.app.common.core.workflow.workflow_reader import WorkflowConfigReader
from studio.app.const import DATE_FORMAT
from studio.app.dir_path import DIRPATH


class ExptConfigWriter:
    def __init__(
        self,
        workspace_id: str,
        unique_id: str,
        name: str,
        nwbfile: Dict = {},
        snakemake: Dict = {},
    ) -> None:
        self.workspace_id = workspace_id
        self.unique_id = unique_id
        self.name = name
        self.nwbfile = nwbfile
        self.snakemake = snakemake
        self.builder = ExptConfigBuilder()

    @staticmethod
    def write_raw(workspace_id: str, unique_id: str, config: dict) -> None:
        ConfigWriter.write(
            dirname=join_filepath([DIRPATH.OUTPUT_DIR, workspace_id, unique_id]),
            filename=DIRPATH.EXPERIMENT_YML,
            config=config,
        )

    def write(self) -> None:
        expt_filepath = join_filepath(
            [
                DIRPATH.OUTPUT_DIR,
                self.workspace_id,
                self.unique_id,
                DIRPATH.EXPERIMENT_YML,
            ]
        )
        if os.path.exists(expt_filepath):
            expt_config = ExptConfigReader.read(expt_filepath)
            self.builder.set_config(expt_config)
            self.add_run_info()
        else:
            self.create_config()

        self.build_function_from_nodeDict()

        # Write EXPERIMENT_YML
        self.write_raw(
            self.workspace_id, self.unique_id, config=asdict(self.builder.build())
        )

    def create_config(self) -> ExptConfig:
        return (
            self.builder.set_workspace_id(self.workspace_id)
            .set_unique_id(self.unique_id)
            .set_name(self.name)
            .set_started_at(datetime.now().strftime(DATE_FORMAT))
            .set_success(WorkflowRunStatus.RUNNING.value)
            .set_nwbfile(self.nwbfile)
            .set_snakemake(self.snakemake)
            .build()
        )

    def add_run_info(self) -> ExptConfig:
        return (
            self.builder.set_started_at(
                datetime.now().strftime(DATE_FORMAT)
            )  # Update time
            .set_success(WorkflowRunStatus.RUNNING.value)
            .build()
        )

    def build_function_from_nodeDict(self) -> ExptConfig:
        func_dict: Dict[str, ExptFunction] = {}
        node_dict = WorkflowConfigReader.read(
            join_filepath(
                [
                    DIRPATH.OUTPUT_DIR,
                    self.workspace_id,
                    self.unique_id,
                    DIRPATH.WORKFLOW_YML,
                ]
            )
        ).nodeDict

        for node in node_dict.values():
            func_dict[node.id] = ExptFunction(
                unique_id=node.id,
                name=node.data.label,
                hasNWB=False,
                success=NodeRunStatus.RUNNING.value,
            )
            if node.data.type == "input":
                timestamp = datetime.now().strftime(DATE_FORMAT)
                func_dict[node.id].started_at = timestamp
                func_dict[node.id].finished_at = timestamp
                func_dict[node.id].success = NodeRunStatus.SUCCESS.value

        return self.builder.set_function(func_dict).build()


class ExptDataWriter:
    def __init__(
        self,
        workspace_id: str,
        unique_id: str,
    ):
        self.workspace_id = workspace_id
        self.unique_id = unique_id

    def delete_data(self) -> bool:
        result = True

        shutil.rmtree(
            join_filepath([DIRPATH.OUTPUT_DIR, self.workspace_id, self.unique_id])
        )

        return result

    def rename(self, new_name: str) -> ExptConfig:
        filepath = join_filepath(
            [
                DIRPATH.OUTPUT_DIR,
                self.workspace_id,
                self.unique_id,
                DIRPATH.EXPERIMENT_YML,
            ]
        )

        # validate params
        new_name = "" if new_name is None else new_name  # filter None

        # Note: "r+" option is not used here because it requires file pointer control.
        with open(filepath, "r") as f:
            config = yaml.safe_load(f)
            config["name"] = new_name

        with open(filepath, "w") as f:
            yaml.dump(config, f, sort_keys=False)

        return ExptConfig(
            workspace_id=config["workspace_id"],
            unique_id=config["unique_id"],
            name=config["name"],
            started_at=config.get("started_at"),
            finished_at=config.get("finished_at"),
            success=config.get("success", WorkflowRunStatus.RUNNING.value),
            hasNWB=config["hasNWB"],
            function=ExptConfigReader.read_function(config["function"]),
            nwb=config.get("nwb"),
            snakemake=config.get("snakemake"),
        )
