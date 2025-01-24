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

import click
import subprocess

from abc import ABC, abstractmethod

from rich import print
from rich.console import Group, RenderableType
from rich.panel import Panel
from rich.text import Text

from cloudera_assist import console
from cloudera_assist.env import EnvFile, generate_env_table


class Command(ABC):
    def __init__(self, label: str, info: str, debug: bool) -> None:
        self.label = label
        self.info = info
        self.debug = debug

    @abstractmethod
    def execute(self) -> None:
        pass

    def __rich__(self) -> RenderableType:
        return Text(self.label)


class AdHoc(Command):
    def __init__(
        self,
        label: str,
        command: list,
        info: str = "Undefined adhoc command",
        debug: bool = False,
        pause: bool = True,
    ) -> None:
        super().__init__(label, info, debug)
        self.command = command
        self.pause = pause

    @abstractmethod
    def get_error_title(self) -> str:
        pass

    def execute(self) -> None:
        try:
            cli = subprocess.Popen(self.command)
            cli.wait()

            if self.debug:
                print(cli)
        except subprocess.CalledProcessError as e:
            if self.debug:
                print(e)
            print(Panel.fit("[red]" + e.stderr, title=self.get_error_title()))

        if self.pause:
            click.pause()
        return


class Action(AdHoc):
    def get_error_title(self) -> str:
        return "Action Execution Error"


class Utility(AdHoc):
    def get_error_title(self) -> str:
        return "Utility Execution Error"


class ExitApplication(Command):
    def __init__(self) -> None:
        super().__init__("Exit", "Exit", False)

    def execute(self) -> None:
        print("[bold][green]Goodbye!")
        exit()


class CurrentEnv(Command):
    def __init__(self, env: EnvFile, debug) -> None:
        info = """
# View the Current Environment

`cloudera-assist` helps manage your application's environment variables.
Select this command to view your current variables.

The variables are both set in the current running process and written to
disk, as specified by the `--env-file` option, which defaults to `.env`.

If you want to use these variables outside of `cloudera-assist`, simply
source the `env-file`, for example:

```bash
set -a; source .env; set +a
```
        """
        super().__init__("View environment file", info, debug)
        self.env = env

    def execute(self) -> None:
        console.clear()
        print(
            Panel.fit(
                Group(
                    "Current environment file:\n",
                    generate_env_table(self.env.get_env()),
                    "",
                )
            )
        )
        click.pause()
        return


class Launch(Command):
    def __init__(
        self,
        label: str,
        url: str,
        info: str = "Undefined Launch command",
        debug: bool = False,
    ) -> None:
        super().__init__(label, info, debug)
        self.url = url

    def execute(self) -> None:
        click.launch(self.url)


# TODO Generate a new SSH key
