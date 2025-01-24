# Copyright 2025 Cloudera, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from io import StringIO
from pathlib import Path

from dotenv import dotenv_values, load_dotenv, set_key, unset_key

from rich import print
from rich.panel import Panel
from rich.prompt import Confirm
from rich.table import Table

PASS_ENV = "ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES"


def get_pass_env() -> list[str]:
    if PASS_ENV in os.environ:
        return sorted(os.environ[PASS_ENV].split(","))
    else:
        return []


class EnvFile(object):
    def __init__(self, env_file) -> None:
        self.env_file = env_file

    def touch_env(self) -> None:
        if not os.path.isfile(self.env_file):
            env_prompt = Confirm.ask(
                f"Environment file not found. Create [i]{self.env_file}[/i]?"
            )
            if env_prompt:
                Path(self.env_file).touch()
            else:
                print("Exiting.")
                exit()

    def read_env(self) -> bool:
        try:
            if os.path.isfile(self.env_file):
                return load_dotenv(self.env_file)
            else:
                error_msg = "File not found, " + self.env_file
        except Exception as e:
            error_msg = f"Error parsing environment configuration file, {self.env_file}: {str(e)}"

        print(
            Panel.fit("[red]" + error_msg, title="Environment Configuration File Error")
        )
        exit(254)

    def get_env(self, content: str = None) -> dict:
        if content is not None:
            return dotenv_values(stream=StringIO(content))
        else:
            return dotenv_values(self.env_file)

    def unset_env(self, variables: list) -> None:
        pass_vars = [v for v in get_pass_env() if v not in variables]
        if pass_vars:
            env_vars = ",".join(pass_vars)
            set_key(self.env_file, PASS_ENV, env_vars)
            os.environ[PASS_ENV] = env_vars
        else:
            unset_key(self.env_file, PASS_ENV)
            del os.environ[PASS_ENV]

        for v in variables:
            if v in os.environ:
                del os.environ[v]
            unset_key(self.env_file, v)

    def set_env(self, variables: dict) -> None:
        for k, v in variables.items():
            os.environ[k] = v
            set_key(self.env_file, k, v)

        pass_vars = get_pass_env()
        pass_vars = set(pass_vars).union(variables.keys())
        if pass_vars:
            env_vars = ",".join(sorted(pass_vars))
            set_key(self.env_file, PASS_ENV, env_vars)
            os.environ[PASS_ENV] = env_vars


def generate_env_table(variables: dict) -> Table:
    exports = Table(box=None, show_header=False, show_footer=False)

    exports.add_column(style="bold green")
    exports.add_column(style="green", overflow="fold")

    for k, v in sorted(variables.items()):
        exports.add_row(k, v)

    return exports
