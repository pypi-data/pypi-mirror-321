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
import configparser
import datetime
import os
import stat
import subprocess

from abc import abstractmethod
from pathlib import Path

from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from rich import box, print
from rich.console import Group, RenderableType
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Confirm
from rich.rule import Rule
from rich.style import Style
from rich.table import Table
from rich.text import Text

from cloudera_assist import console
from cloudera_assist.commands import Command
from cloudera_assist.env import EnvFile


class Credentials(Command):
    def __init__(self, env: EnvFile, label: str, info: str, debug: bool) -> None:
        super().__init__(label, info, debug)
        self.env = env

    def execute(self) -> None:
        if Confirm.ask("Apply?", default=True):
            self.apply()
        else:
            console.clear()
            self.execute()

    @abstractmethod
    def cancel(self) -> None:
        pass

    @abstractmethod
    def apply(self) -> None:
        pass

    def is_set(self) -> bool:
        return False

    def __rich__(self) -> RenderableType:
        if self.is_set():
            text = ":white_check_mark: "
        else:
            text = ":prohibited: "
        return Text.from_markup(text + self.label)


class SelectableTable(Credentials):
    SELECTED = Style(color="blue", bgcolor="white", bold=True)

    def __init__(
        self,
        env: EnvFile,
        label: str,
        info: str,
        title: str,
        headers: list,
        rows: list,
        debug: bool,
    ) -> None:
        super().__init__(env, label, info, debug)
        self.title = title
        self.headers = headers
        self.rows = rows

        self.selected = 0
        self.selection_active = True  # Set to False to cancel

    @property
    def selected_row(self) -> list:
        return self.rows[self.selected]

    def generate_table(self) -> Group:
        selector = Group()
        table = Table(box=box.MINIMAL, expand=True)

        for h in self.headers:
            table.add_column(h)

        size = console.height - 6
        index = 0
        visible_rows = self.rows

        # If we need to window the rows
        if len(self.rows) + 3 > size:
            # Handle the window at the top of the list
            if self.selected < size / 2:
                visible_rows = self.rows[:size]
            # Handle the window at the bottom of the list
            elif self.selected + size / 2 > len(self.rows):
                visible_rows = self.rows[-size:]
                index = len(self.rows) - size
            # Handle the window in all other locations
            else:
                visible_rows = self.rows[
                    self.selected - size // 2 : self.selected + size // 2 + 1
                ]
                index = self.selected - size // 2

        for i, row in enumerate(visible_rows, index):
            table.add_row(
                *row, style=SelectableTable.SELECTED if i == self.selected else None
            )

        selector.renderables.append(Rule(self.title))
        selector.renderables.append(table)
        selector.renderables.append(
            Rule(
                "[b]Up[/b] (:up_arrow:/k) | [b]Down[/b] (:down_arrow:/j) | [b]Escape[/b] (q/esc) | [b]Select[/b] (enter)"
            )
        )
        return selector

    def run_table_selection(self) -> None:
        console.clear()
        with Live(self.generate_table(), auto_refresh=False) as live:
            while True:
                if self.navigate(click.getchar()):
                    live.update(self.generate_table(), refresh=True)
                else:
                    live.stop()
                    break

    def navigate(self, ch: str) -> bool:
        # Up
        if ch == "\x1b[A" or ch == "k" or ch == "8":
            self.selected = max(0, self.selected - 1)
            return True
        # Down
        elif ch == "\x1b[B" or ch == "j" or ch == "2":
            self.selected = min(len(self.rows) - 1, self.selected + 1)
            return True
        # Enter / Select
        elif ch in ["\r"]:
            return False
        # Escape / Quit
        elif ch in ["q", "\x1b"]:
            self.selection_active = False
            return False
        else:
            return True

    def execute(self) -> None:
        while True:
            self.run_table_selection()
            if not self.selection_active or self.validate():
                break

        if self.selection_active:
            console.clear()
            print(
                Panel.fit("You selected the following: [green]" + self.selected_row[0])
            )
            super().execute()
        else:
            self.cancel()

    def cancel(self) -> None:
        if not Confirm.ask("Cancel?", default=False):
            self.selection_active = True
            self.execute()

    def validate(self) -> bool:
        return True


WITHIN_INTERVAL = datetime.timedelta(weeks=26)


def readable_timestamp(timestamp: int) -> str:
    ts = datetime.datetime.fromtimestamp(timestamp)
    current = datetime.datetime.now()
    if current - WITHIN_INTERVAL < ts < current + WITHIN_INTERVAL:
        return ts.strftime("%b %d %H:%M")
    else:
        return ts.strftime("%b %d  %Y")


def readable_size(size: int) -> str:
    for unit in ["B", "K", "M", "G", "T"]:
        if size < 1024.0 or unit == "T":
            break
        size /= 1024.0
    return f"{size:.1f}{unit}"


class SelectableFile(SelectableTable):
    def __init__(
        self,
        env: EnvFile,
        label: str,
        info: str,
        title: str,
        directory: Path,
        debug: bool,
    ) -> None:
        self.current_dir = None
        super().__init__(
            env,
            label,
            info,
            title,
            self.get_headers(),
            self.list_files(directory),
            debug,
        )

    @property
    def selected_path(self) -> Path:
        return self.current_dir.joinpath(self.selected_row[0]).expanduser().resolve()

    def get_headers(self) -> list[str]:
        return ["File", "Mode", "Owner", "Group", "Size", "Modified"]

    def parse_file(self, file: Path) -> list[str]:
        fs = os.stat(file)
        return (
            file.name,
            stat.filemode(fs.st_mode),
            file.owner(),
            file.group(),
            readable_size(fs.st_size),
            readable_timestamp(fs.st_mtime),
        )

    def parse_directory(self, dir: Path) -> list[str]:
        ds = os.stat(dir)
        return (
            dir.name + "/",
            stat.filemode(ds.st_mode),
            dir.owner(),
            dir.group(),
            readable_size(ds.st_size),
            readable_timestamp(ds.st_mtime),
        )

    def parse_symlink(self, dir: Path) -> list[str]:
        ds = os.stat(dir)
        return (
            dir.name + "*",
            stat.filemode(ds.st_mode),
            dir.owner(),
            dir.group(),
            readable_size(ds.st_size),
            readable_timestamp(ds.st_mtime),
        )

    def list_files(self, directory: Path) -> list:
        self.current_dir = directory.expanduser().resolve()
        output = []

        if self.current_dir.parent != self.current_dir:
            output.append(
                (
                    "../",
                    "",
                    "",
                )
            )

        for filepath in self.current_dir.iterdir():
            if filepath.exists():
                if filepath.is_dir():
                    output.append(self.parse_directory(filepath))
                elif filepath.is_file():
                    output.append(self.parse_file(filepath))
                elif filepath.is_symlink():
                    output.append(self.parse_symlink(filepath))

        output.sort(key=lambda file: file[0])
        return output

    def validate(self) -> bool:
        if self.selected_path.is_dir():
            self.rows = self.list_files(self.selected_path)
            self.selected = 0
            return False
        else:
            return True


class SshCredentials(SelectableFile):
    DEFAULT_CREDENTIALS_DIR = Path("~/.ssh").expanduser().resolve()
    ENV_VARIABLE = "SSH_PRIVATE_KEY_FILE"

    def __init__(self, env: EnvFile, debug: bool) -> None:
        info = """
Select a private SSH key that has no password.
        """
        super().__init__(
            env,
            "SSH Key",
            info,
            "SSH Private Key",
            self.DEFAULT_CREDENTIALS_DIR,
            debug,
        )

    def validate(self) -> bool:
        if super().validate():

            def validate_error(message, cause):
                print(Panel.fit(message, title="SSH Private Key Error"))
                if self.debug:
                    print(repr(cause))

            with open(self.selected_path, "rb") as file:
                try:
                    key = load_pem_private_key(file.read(), password=None)
                    if self.debug:
                        print(repr(key))
                    return True
                except ValueError as ve:
                    validate_error(
                        f"[red]Unable to read [i]{self.selected_row[0]}[/i]; {ve.args[0]}",
                        ve,
                    )
                except TypeError as te:
                    validate_error(
                        f"[red][i]{self.selected_row[0]}[/i] is unsupported. {te.args[0]}.",
                        te,
                    )
                except UnsupportedAlgorithm as uae:
                    validate_error(
                        f"[red][i]{self.selected_row[0]}[/i] is unsupported. {uae.args[0]}.",
                        uae,
                    )

            click.pause()

        return False

    def apply(self) -> None:
        self.env.set_env({self.ENV_VARIABLE: str(self.selected_path)})

    def is_set(self) -> bool:
        return self.ENV_VARIABLE in os.environ


class AwsCredentials(SelectableTable):
    def __init__(self, env: EnvFile, debug: bool) -> None:
        info = """
Select your AWS credentials. If you are using Single-Sign-On (SSO), be sure you have logged into that profile.
        """
        super().__init__(
            env,
            "AWS",
            info,
            "AWS Credentials",
            ["Profile"],
            self.list_profiles(),
            debug,
        )

    def list_profiles(self) -> list[list]:
        try:
            results = subprocess.run(
                ["aws", "configure", "list-profiles"],
                check=True,
                capture_output=True,
                encoding="utf-8",
            )
            return [[profile] for profile in results.stdout.splitlines()]
        except subprocess.CalledProcessError as e:
            print(Panel.fit("[red]" + str(e), title="AWS Profiles Error"))
            exit(255)

    def apply(self) -> None:
        try:
            aws_cli = subprocess.run(
                [
                    "aws",
                    "configure",
                    "export-credentials",
                    "--format=env-no-export",
                    f"--profile={self.selected_row[0]}",
                ],
                check=True,
                capture_output=True,
                encoding="utf-8",
            )

            if self.debug:
                print(aws_cli)

            # Parse the output into a dict of variables
            aws_exports = self.env.get_env(aws_cli.stdout)

            # Clear out any existing variables
            existing = self.env.get_env()

            clear = [
                k
                for k in existing.keys()
                if str(k).startswith("AWS_") and k not in aws_exports
            ]
            self.env.unset_env(clear)

            self.env.set_env(aws_exports)
        except subprocess.CalledProcessError as e:
            if self.debug:
                print(e)
            print(Panel.fit("[red]" + e.stderr, title="AWS Profile Export Error"))
            click.pause()

    def is_set(self) -> bool:
        if "AWS_ACCESS_KEY_ID" in os.environ:
            if "AWS_CREDENTIAL_EXPIRATION" in os.environ:
                now = datetime.datetime.now(datetime.timezone.utc).astimezone()
                expiration = datetime.datetime.fromisoformat(
                    os.environ["AWS_CREDENTIAL_EXPIRATION"]
                ).astimezone(now.tzinfo)
                if now > expiration:
                    return False
            return True
        else:
            return False


class LicenseCredentials(SelectableFile):
    DEFAULT_CREDENTIALS_DIR = Path("~")
    ENV_VARIABLE = "CDP_LICENSE_FILE"

    def __init__(self, env: EnvFile, debug: bool) -> None:
        info = """
Select your Cloudera on Premise license file.
        """
        super().__init__(
            env,
            "Cloudera on Premise",
            info,
            "Cloudera on Premise License",
            self.DEFAULT_CREDENTIALS_DIR,
            debug,
        )

    def apply(self) -> None:
        self.env.set_env({self.ENV_VARIABLE: str(self.selected_path)})

    def is_set(self) -> bool:
        return self.ENV_VARIABLE in os.environ


class CloudCredentials(SelectableTable):
    DEFAULT_CREDENTIALS_FILE = Path("~/.cdp/credentials")
    ENV_VARIABLE = "CDP_ACCESS_KEY_ID"

    def __init__(self, env: EnvFile, debug: bool) -> None:
        self.config = configparser.ConfigParser()
        self.collect_credentials()
        info = """
Select your Cloudera on Cloud credentials.
        """
        super().__init__(
            env,
            "Cloudera on Cloud",
            info,
            "Cloudera On Cloud Credentials",
            ["Cloudera Profile"],
            [[p] for p in self.config.sections()],
            debug,
        )

    def collect_credentials(self) -> None:
        config_file = (
            Path(
                os.environ["CDP_SHARED_CREDENTIALS_FILE"]
                if "CDP_SHARED_CREDENTIALS_FILE" in os.environ
                else self.DEFAULT_CREDENTIALS_FILE
            )
            .expanduser()
            .resolve()
        )

        try:
            self.config.read(config_file)

        except Exception as e:
            print(Panel.fit("[red]" + str(e), title="Cloud Credentials Error"))
            exit(255)

    def apply(self) -> None:
        try:
            # Set the cloud credentials
            cloud_exports = {
                "CDP_ACCESS_KEY_ID": self.config[self.selected_row[0]][
                    "cdp_access_key_id"
                ],
                "CDP_PRIVATE_KEY": self.config[self.selected_row[0]]["cdp_private_key"],
            }

            # Clear out any existing variables
            existing = self.env.get_env()

            clear = [
                k
                for k in existing.keys()
                if str(k).startswith("CDP_") and k not in cloud_exports
            ]
            self.env.unset_env(clear)

            self.env.set_env(cloud_exports)
        except subprocess.CalledProcessError as e:
            if self.debug:
                print(e)
            print(Panel.fit("[red]" + e.stderr, title="Cloud Profile Export Error"))
            click.pause()

    def is_set(self) -> bool:
        return self.ENV_VARIABLE in os.environ


CREDENTIALS = dict[str, Credentials](
    {
        "aws": AwsCredentials,
        "cloud": CloudCredentials,
        "license": LicenseCredentials,
        "ssh": SshCredentials,
    }
)
