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

from unittest.mock import MagicMock

from rich.prompt import Confirm

from cloudera_assist import console
from cloudera_assist.env import EnvFile
from cloudera_assist.credentials import SelectableTable

ENV_FILE = MagicMock(EnvFile)


class TestableSelectableTable(SelectableTable):
    def apply(self) -> None:
        return

    def cancel(self) -> None:
        return


def test_selectable_table_down(monkeypatch):
    mock_nav = MagicMock()
    mock_nav.side_effect = ["j", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableTable(
        ENV_FILE, "test", ["ONE", "TWO"], [("one", "two"), ("three", "four")], False
    )

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 1
    assert cred.selected_row == ("three", "four")

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_table_up(monkeypatch):
    mock_nav = MagicMock()
    mock_nav.side_effect = ["k", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableTable(
        ENV_FILE, "test", ["ONE", "TWO"], [("one", "two"), ("three", "four")], False
    )
    cred.selected = 1

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 0
    assert cred.selected_row == ("one", "two")

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_table_down_multiple(monkeypatch):
    mock_nav = MagicMock()
    mock_nav.side_effect = ["j", "2", "\x1b[B", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableTable(
        ENV_FILE,
        "test",
        ["ONE", "TWO"],
        [("one", "two"), ("three", "four"), ("five", "six"), ("seven", "eight")],
        False,
    )

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 3
    assert cred.selected_row == ("seven", "eight")

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_table_up_multiple(monkeypatch):
    mock_nav = MagicMock()
    mock_nav.side_effect = ["k", "8", "\x1b[A", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableTable(
        ENV_FILE,
        "test",
        ["ONE", "TWO"],
        [("one", "two"), ("three", "four"), ("five", "six"), ("seven", "eight")],
        False,
    )
    cred.selected = 3

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 0
    assert cred.selected_row == ("one", "two")

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_table_top(monkeypatch):
    mock_nav = MagicMock()
    mock_nav.side_effect = ["k", "k", "k", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableTable(
        ENV_FILE, "test", ["ONE", "TWO"], [("one", "two"), ("three", "four")], False
    )

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 0
    assert cred.selected_row == ("one", "two")

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_table_bottom(monkeypatch):
    mock_nav = MagicMock()
    mock_nav.side_effect = ["j", "j", "j", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableTable(
        ENV_FILE, "test", ["ONE", "TWO"], [("one", "two"), ("three", "four")], False
    )

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 1
    assert cred.selected_row == ("three", "four")

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_table_up_window(monkeypatch):
    mock_nav = MagicMock()
    mock_nav.side_effect = ["k", "k", "8", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableTable(
        ENV_FILE,
        "test",
        ["ONE", "TWO"],
        [
            ("one", "two"),
            ("three", "four"),
            ("five", "six"),
            ("seven", "eight"),
            ("nine", "ten"),
        ],
        False,
    )
    cred.selected = 4  # Start on the last entry of the list
    console.height = 7  # Window of 3 entries

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 1
    assert cred.selected_row == ("three", "four")

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_table_down_window(monkeypatch):
    mock_nav = MagicMock()
    mock_nav.side_effect = ["j", "j", "2", "\r"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableTable(
        ENV_FILE,
        "test",
        ["ONE", "TWO"],
        [
            ("one", "two"),
            ("three", "four"),
            ("five", "six"),
            ("seven", "eight"),
            ("nine", "ten"),
        ],
        False,
    )
    cred.selected = 0  # Start on the first entry of the list
    console.height = 7  # Window of 3 entries

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 3
    assert cred.selected_row == ("seven", "eight")

    mock_cancel.assert_not_called()
    mock_apply.assert_called_once()


def test_selectable_table_cancel(monkeypatch):
    mock_nav = MagicMock()
    mock_nav.side_effect = ["j", "j", "\x1b"]

    mock_confirm = MagicMock()
    mock_confirm.return_value = True

    monkeypatch.setattr(click, "getchar", mock_nav)
    monkeypatch.setattr(Confirm, "ask", mock_confirm)

    cred = TestableSelectableTable(
        ENV_FILE,
        "test",
        ["ONE", "TWO"],
        [
            ("one", "two"),
            ("three", "four"),
            ("five", "six"),
            ("seven", "eight"),
            ("nine", "ten"),
        ],
        False,
    )
    cred.selected = 0

    mock_apply = MagicMock()
    monkeypatch.setattr(cred, "apply", mock_apply)

    mock_cancel = MagicMock()
    monkeypatch.setattr(cred, "cancel", mock_cancel)

    cred.execute()

    assert cred.selected == 2
    assert cred.selected_row == ("five", "six")

    mock_cancel.assert_called_once()
    mock_apply.assert_not_called()
