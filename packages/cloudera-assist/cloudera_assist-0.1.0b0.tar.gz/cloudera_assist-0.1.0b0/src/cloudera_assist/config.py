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
import yaml

from rich import print
from rich.panel import Panel

from cloudera_assist.commands import Action, CurrentEnv, Command, Launch, Utility
from cloudera_assist.credentials import CREDENTIALS
from cloudera_assist.env import EnvFile


def error_panel(error_msg) -> None:
    print(Panel.fit("[red]" + error_msg, title="cloudera-assist Configuration Error"))
    exit(253)


class Config(object):
    def __init__(self, env: EnvFile, config_file: str, debug: bool) -> None:
        self.env = env
        self.debug = debug

        self._credentials = []
        self._actions = []
        self._utilities = []

        self.prelude = ""
        self.info = ""

        try:
            if os.path.isfile(config_file):
                with open(config_file, "r") as file:
                    self.config = yaml.safe_load(file)
            else:
                error_panel(f"File not found, [i]{config_file}[/i]")
        except Exception as e:
            error_panel(
                f"Error parsing environment configuration file, {config_file}: {str(e)}"
            )

    def construct(self) -> None:
        if "credentials" in self.config:
            invalid_credentials = set(self.config["credentials"]) - set(
                CREDENTIALS.keys()
            )
            if invalid_credentials:
                error_panel(
                    f"Invalid credential type(s): [i]{', '.join(invalid_credentials)}[/i]"
                )

            for c in self.config["credentials"]:
                credential = CREDENTIALS[c](self.env, self.debug)
                self._credentials.append(credential)

        if "actions" in self.config:
            for a in self.config["actions"]:
                if "label" not in a:
                    error_panel("Missing actions label: " + str(a))

                payload = dict(label=a["label"], debug=self.debug)
                if "info" in a:
                    payload.update(info=a["info"])

                if "url" in a:
                    payload.update(url=a["url"])
                    self._actions.append(Launch(**payload))
                elif "command" in a:
                    payload.update(command=a["command"])
                    if "pause" in a:
                        payload.update(pause=a["pause"])
                    self._actions.append(Action(**payload))
                else:
                    error_panel("Invalid actions configuration: " + str(a))

        if "utilities" in self.config:
            for u in self.config["utilities"]:
                if "label" not in u:
                    error_panel("Missing utilities label: " + str(u))

                payload = dict(label=u["label"], debug=self.debug)
                if "info" in u:
                    payload.update(info=u["info"])

                if "url" in u:
                    payload.update(url=u["url"])
                    self._utilities.append(Launch(**payload))
                elif "command" in u:
                    payload.update(command=u["command"])
                    if "pause" in u:
                        payload.update(pause=u["pause"])
                    self._utilities.append(Utility(**payload))
                else:
                    error_panel("Invalid utilities configuration: " + str(u))

        # Add current environment utility
        self._utilities.append(CurrentEnv(self.env, self.debug))

        # Add the prelude content
        if "prelude" in self.config:
            self.prelude = self.config["prelude"]

        # Add the initial info panel content
        if "info" in self.config:
            self.info = self.config["info"]

    @property
    def actions(self) -> list[Command]:
        return self._actions

    @property
    def credentials(self) -> list[Command]:
        return self._credentials

    @property
    def utilities(self) -> list[Command]:
        return self._utilities
