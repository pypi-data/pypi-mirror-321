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

from pathlib import Path
import click

from unittest.mock import MagicMock

from rich.prompt import Confirm

from cloudera_assist.env import EnvFile
from cloudera_assist.credentials import SelectableFile

ENV_FILE = MagicMock(EnvFile)


class TestableSelectableFile(SelectableFile):
    def __init__(self, env: EnvFile, label: str, directory: Path, debug: bool) -> None:
        super().__init__(env, label, directory, debug)

    def apply(self) -> None:
        return

    def cancel(self) -> None:
        return


def test_selectable_file_down(monkeypatch, tmp_path):
    file_a = tmp_path / "file_a.txt"
    file_a.touch()
    file_b = tmp_path / "file_b.txt"
    file_b.touch()

    mock_nav = MagicMock()
    mock_nav.side_effect = ["j", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableFile(ENV_FILE, "test", tmp_path, False)

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 1
    assert cred.selected_row[0] == "file_a.txt"

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_file_up(monkeypatch, tmp_path):
    file_a = tmp_path / "file_a.txt"
    file_a.touch()
    file_b = tmp_path / "file_b.txt"
    file_b.touch()

    mock_nav = MagicMock()
    mock_nav.side_effect = ["k", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableFile(ENV_FILE, "test", tmp_path, False)
    cred.selected = 2

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 1
    assert cred.selected_row[0] == "file_a.txt"

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_file_directory_down(monkeypatch, tmp_path):
    dir_a = tmp_path / "dir_a"
    dir_a.mkdir()
    file_a = dir_a / "file_a.txt"
    file_a.touch()

    mock_nav = MagicMock()
    mock_nav.side_effect = ["j", "\r", "j", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableFile(ENV_FILE, "test", tmp_path, False)
    cred.selected = 0

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 1
    assert cred.selected_row[0] == "file_a.txt"

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()
