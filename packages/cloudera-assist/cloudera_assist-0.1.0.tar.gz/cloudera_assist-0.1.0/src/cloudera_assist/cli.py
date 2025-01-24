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
import yaml

from time import sleep

from rich.console import Group
from rich.layout import Layout
from rich.live import Live
from rich.markdown import Markdown
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text
from rich import print

from cloudera_assist import __version__, console
from cloudera_assist.commands import Command, ExitApplication
from cloudera_assist.components import KeyboardThread
from cloudera_assist.credentials import Credentials
from cloudera_assist.config import Config
from cloudera_assist.env import EnvFile


def parse_execution_image(navigator_file) -> str:
    try:
        with open(navigator_file, "r") as file:
            nav_config = yaml.safe_load(file)
        return nav_config["ansible-navigator"]["execution-environment"]["image"]
    except yaml.YAMLError as ye:
        error_title = "ansible-navigator Configuration Format Error"
        error_msg = "Invalid YAML file: " + str(ye)
    except KeyError as ke:
        error_title = "ansible-navigator Configuration Parse Error"
        error_msg = "Unable to parse YAML file: " + str(ke)
    except Exception as e:
        error_title = "ansible-navigator Configuration File Error"
        error_msg = str(e)

    print(Panel.fit("[red]" + error_msg, title=error_title))
    exit(255)


class MainInput(object):
    PROMPT = "[bold blue]>> Select an option:[/bold blue] "

    def __init__(self, options: list[Command], warning: Layout) -> None:
        self.options = options
        self.warning = warning

        self.callback = None
        self.selection = ""

    def __rich__(self) -> str:
        return self.PROMPT + self.selection

    def process_input(self, ch) -> bool:
        if ch in ["\r", "\n"]:
            return self.execute()
        elif ch in ["\x7f"]:
            if self.selection != "":
                self.selection = self.selection[:-1]
            return False
        else:
            self.selection += ch
            return False

    def execute(self) -> bool:
        # Escape / Quit
        if self.selection in ["q", "\x1b"]:
            self.callback = ExitApplication()
            return True
        # Only a return
        elif self.selection == "":
            pass
        # If a digit
        elif self.selection.isdigit():
            try:
                self.callback = self.options[int(self.selection) - 1]
                return True
            except IndexError:
                self.warning.update(
                    "[red]Please enter a number shown above... :badger:"
                )
                self.selection = ""
        # Warn on everything else
        else:
            self.warning.update(
                f"You entered '[i]{self.selection}[/i]'. [red]Please enter a number... :grimacing:"
            )
            self.selection = ""

        return False


class MainMenu(object):
    def __init__(
        self,
        credentials: list[Credentials],
        actions: list[Command],
        utilities: list[Command],
    ) -> None:
        self.actions = 0
        self.utilities = len(actions)
        self.credentials = len(actions) + len(utilities)

        self.rows = [*actions, *utilities, *credentials]

        self.selected = -1
        self.active = True

    @property
    def selected_command(self) -> Command:
        if self.selected > -1:
            return self.rows[self.selected]
        else:
            return None

    def __rich__(self):
        menu = Table.grid()

        for i, row in enumerate(self.rows):
            if i == self.actions:
                menu.add_row(Text("Actions", justify="center", style="bold blue"))
                menu.add_section()
            elif i == self.utilities:
                menu.add_row(Text("Utilities", justify="center", style="bold blue"))
                menu.add_section()
            elif i == self.credentials:
                menu.add_row(Text("Credentials", justify="center", style="bold blue"))
                menu.add_section()

            if self.selected == i:
                menu.add_row(row, style="bold blue")
            else:
                menu.add_row(row)

        return menu

    def navigate(self, ch: str) -> bool:
        # Up
        if ch == "\x1b[A" or ch == "k" or ch == "8":
            self.selected = max(0, self.selected - 1)
            return False
        # Down
        elif ch == "\x1b[B" or ch == "j" or ch == "2":
            self.selected = min(len(self.rows) - 1, self.selected + 1)
            return False
        # Enter / Select
        elif ch in ["\r", "\n"]:
            self.active = False
            return True
        # Escape / Quit
        elif ch in ["q", "\x1b"]:
            self.selected = -1
            self.active = False
            return True
        else:
            return False

    def execute(self):
        if self.selected_command is None:
            ExitApplication().execute()
        else:
            self.selected_command.execute()


class InfoPanel(object):
    def __init__(self, menu: MainMenu, content: str) -> None:
        self.menu = menu
        self.initial_content = content

    def __rich__(self):
        if self.menu.selected_command is not None:
            return Markdown(self.menu.selected_command.info)
        else:
            return Markdown(self.initial_content)


class CldrAssist(object):
    def __init__(
        self, debug, navigator, navigator_file, env_file, create_env, assist_file
    ) -> None:
        # Set the runtime variables
        self.debug = debug
        self.check_navigator = navigator
        self.navigator_file = navigator_file
        self.check_env = create_env
        self.env_file = env_file
        self.ee_image = None

        # Initialize the command to run
        self.callback = None

        # Set up the environment variables file
        self.env = EnvFile(env_file)

        # Set up the cloudera-assist configuration file
        self.config = Config(self.env, assist_file, debug)

    def load(self):
        # Parse the EE image
        if self.check_navigator:
            self.ee_image = parse_execution_image(self.navigator_file)

        # Create the environment file if needed
        if self.check_env:
            self.env.touch_env()

        # Load the environment variable configuration file, prompt to create
        self.env.read_env()

        # Construct the cloudera-assist configuration
        self.config.construct()

    def main_menu(self):
        # Clear the screen of prior activities
        console.clear()

        # Create the layout
        layout = Layout(name="root")
        layout.split(
            Layout(
                Rule("[bold][orange]Cloudera Assist: Main Menu", characters="=!="),
                name="header",
                size=1,
            ),
            Layout(
                Markdown(self.config.prelude),
                name="prelude",
                ratio=1 if self.config.prelude != "" else 0,
            ),
            Layout(name="body", ratio=3),
            Layout(
                Group(Text(), Rule("Press [bold]q[/bold] to quit.", align="left")),
                name="footer",
                size=2,
            ),
        )

        layout["body"].split_row(
            Layout(name="menu"),
            Layout(name="info"),
        )

        # Prepare the menu table
        menu = MainMenu(
            self.config.credentials, self.config.actions, self.config.utilities
        )
        layout["menu"].update(menu)

        # Prepare the info panel
        info = InfoPanel(
            menu,
            self.config.info,
        )
        layout["info"].update(info)

        # Start the input capture thread
        KeyboardThread(menu.navigate)

        # Execute the live refresh until a selection is made
        with Live(layout, refresh_per_second=5, screen=True):
            while menu.active:
                sleep(0.1)

        # Execute the selected option
        menu.execute()

        # Rebuild the main menu
        self.main_menu()


@click.command()
@click.version_option(version=__version__.VERSION)
@click.help_option()
@click.option("--debug/--no-debug", default=False, help="Enable debugging.")
@click.option(
    "--navigator/--no-navigator",
    default=True,
    help="Check for valid ansible-navigator.yml file and EE image.",
)
@click.option(
    "--navigator-file",
    default="ansible-navigator.yml",
    help="Specify the Ansible Navigator configuration file.",
)
@click.option(
    "--env-file", default=".env", help="Specify the environment credentials file."
)
@click.option(
    "--create-env/--no-create-env",
    default=True,
    help="Prompt to create environment credentials file.",
)
@click.option(
    "--assist-file",
    default="cloudera-assist.yml",
    help="Specify the Cloudera Assist configuration file.",
)
def main(debug, navigator, navigator_file, env_file, create_env, assist_file):
    # Initialize the assistant
    cldr = CldrAssist(
        debug, navigator, navigator_file, env_file, create_env, assist_file
    )

    # Load variables and read configurations
    cldr.load()

    # Create the main entrypoint
    cldr.main_menu()
