import os
from typing import cast

import bluish.actions.base
import bluish.nodes.job
import bluish.nodes.step
import bluish.process
from bluish.logging import error, info
from bluish.schemas import Int, Object, Optional, Str
from bluish.utils import safe_string


def run_git_command(
    command: str, step: bluish.nodes.step.Step
) -> bluish.process.ProcessResult:
    preamble: str = ""

    key_file = step.inputs.get("ssh_key_file")
    if key_file:
        preamble = f"export GIT_SSH_COMMAND='ssh -i {key_file} -o IdentitiesOnly=yes -o StrictHostKeychecking=no';"

    job = cast(bluish.nodes.job.Job, step.parent)
    return job.exec(f"{preamble} {command}", step)


def prepare_environment(step: bluish.nodes.step.Step) -> bluish.process.ProcessResult:
    REQUIRED = {
        "git": "git",
        "openssh-client": "ssh",
    }

    job = cast(bluish.nodes.job.Job, step.parent)

    required_packages = [
        package
        for package, binary in REQUIRED.items()
        if job.exec(f"which {binary}", step).failed
    ]
    if required_packages:
        info(f"Installing missing packages: {required_packages}...")
        result = bluish.process.install_package(
            job.get_inherited_attr("runs_on_host"), required_packages
        )
        if result.failed:
            error(f"Failed to install required packages. Error: {result.error}")
            return result

    return bluish.process.ProcessResult()


def cleanup_environment(step: bluish.nodes.step.Step) -> None:
    pass


class Checkout(bluish.actions.base.Action):
    FQN: str = "git/checkout"

    INPUTS_SCHEMA = Object(
        {
            "repository": Str,
            "depth": Optional(Int),
            "branch": Optional(Str),
        }
    )

    SENSITIVE_INPUTS: tuple[str, ...] = ("ssh_key_file", "password")

    @property
    def fqn(self) -> str:
        return "git/checkout"

    def run(self, step: bluish.nodes.step.Step) -> bluish.process.ProcessResult:
        try:
            inputs = step.inputs

            repository: str = step.expand_expr(inputs["repository"])
            repo_name = os.path.basename(repository)

            result = prepare_environment(step)
            if result.failed:
                return result

            options = ""
            if "depth" in inputs:
                options += f"--depth {inputs['depth']}"
            else:
                options += "--depth 1"

            if "branch" in inputs:
                options += f" --branch {inputs['branch']}"

            info(f"Cloning repository: {safe_string(repository)}...")
            clone_result = run_git_command(
                f"git clone {repository} {options} ./{repo_name}", step
            )
            if clone_result.failed:
                error(f"Failed to clone repository: {clone_result.error}")
                return clone_result

            # Update the current job working dir to the newly cloned repo
            info(f"Setting working directory to: {repo_name}...")
            wd = step.get_inherited_attr("working_directory", ".")
            assert step.parent is not None
            step.parent.set_attr("working_directory", f"{wd}/{repo_name}")

            return clone_result
        finally:
            cleanup_environment(step)
