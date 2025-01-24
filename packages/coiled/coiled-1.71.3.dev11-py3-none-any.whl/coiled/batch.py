from __future__ import annotations

import shlex
import time

from aiohttp import ServerDisconnectedError

import coiled
from coiled.cli.curl import sync_request
from coiled.utils import dict_to_key_val_list


def run(
    command: list[str] | str,
    *,
    workspace: str | None = None,
    software: str | None = None,
    container: str | None = None,
    env: list | dict | None = None,
    secret_env: list | dict | None = None,
    tag: list | dict | None = None,
    vm_type: list | None = None,
    arm: bool | None = False,
    cpu: int | None = None,
    memory: str | None = None,
    gpu: bool | None = False,
    region: str | None = None,
    disk_size: str | None = None,
    ntasks: int | None = None,
    task_on_scheduler: bool | None = False,
    array: str | None = None,
    scheduler_task_array: str | None = None,
    max_workers: int | None = None,
    wait_for_ready_cluster: bool | None = None,
    forward_aws_credentials: bool | None = None,
    package_sync_strict: bool = False,
    package_sync_conda_extras: list | None = None,
    logger=None,
) -> dict:
    if isinstance(command, str):
        command = shlex.split(command)

    env = dict_to_key_val_list(env)
    secret_env = dict_to_key_val_list(secret_env)
    tag = dict_to_key_val_list(tag)
    vm_type = [vm_type] if isinstance(vm_type, str) else vm_type

    kwargs = dict(
        command=command,
        workspace=workspace,
        software=software,
        container=container,
        env=env,
        secret_env=secret_env,
        tag=tag,
        vm_type=vm_type,
        arm=arm,
        cpu=cpu,
        memory=memory,
        gpu=gpu,
        region=region,
        disk_size=disk_size,
        ntasks=ntasks,
        task_on_scheduler=task_on_scheduler,
        array=array,
        scheduler_task_array=scheduler_task_array,
        max_workers=max_workers,
        wait_for_ready_cluster=wait_for_ready_cluster,
        forward_aws_credentials=forward_aws_credentials,
        package_sync_strict=package_sync_strict,
        package_sync_conda_extras=package_sync_conda_extras,
        logger=logger,
    )

    # avoid circular imports
    from coiled.cli.batch.run import _batch_run, batch_run_cli

    # {kwarg: default value} dict, taken from defaults on the CLI
    cli_defaults = {param.name: param.default for param in batch_run_cli.params}

    # this function uses `None` as the default
    # we want to both (1) track which kwargs are that default and (2) replace with default from CLI
    default_kwargs = {key: cli_defaults[key] for key, val in kwargs.items() if val is None and key in cli_defaults}
    kwargs = {
        **kwargs,
        **default_kwargs,
    }

    cluster_id, job_id = _batch_run(default_kwargs, **kwargs)

    return {"cluster_id": cluster_id, "job_id": job_id}


def wait_for_job_done(job_id: int):
    with coiled.Cloud() as cloud:
        url = f"{cloud.server}/api/v2/jobs/{job_id}"
        while True:
            try:
                response = sync_request(cloud, url, "get", data=None, json_output=True)
            except ServerDisconnectedError:
                continue
            state = response.get("state")
            if state and "done" in state:
                return state
            time.sleep(5)
