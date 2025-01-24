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

import pytest
import shutil

from cloudera_assist.cli import parse_execution_image


def test_parse_file_not_found(tmp_path, test_directory, capsys):
    d = tmp_path / "missing_file"
    d.mkdir()

    test_directory(d.resolve())

    with pytest.raises(SystemExit) as e:
        parse_execution_image("ansible-navigator.yml")

    assert e.value.code == 255

    captured = capsys.readouterr()

    assert "No such file or directory" in captured.out


def test_parse_invalid_yaml(tmp_path, test_directory, capsys):
    d = tmp_path / "invalid_format"
    d.mkdir()

    test_directory(d.resolve())

    bogus = d / "ansible-navigator.yml"
    bogus.write_text("bad: yaml:", encoding="utf-8")

    with pytest.raises(SystemExit) as e:
        parse_execution_image("ansible-navigator.yml")

    assert e.value.code == 255

    captured = capsys.readouterr()

    assert "Invalid YAML file" in captured.out


def test_parse_invalid_image(tmp_path, test_directory, request, capsys):
    d = tmp_path / "invalid_config"
    d.mkdir()

    test_directory(d.resolve())

    shutil.copyfile(
        request.fspath.dirpath() / "bogus-ansible-navigator.yml",
        d / "ansible-navigator.yml",
    )

    with pytest.raises(SystemExit) as e:
        parse_execution_image("ansible-navigator.yml")

    assert e.value.code == 255

    captured = capsys.readouterr()

    assert "Unable to parse YAML file" in captured.out


def test_parse_default():
    result = parse_execution_image("ansible-navigator.yml")

    assert result == "test-ee-image"


def test_parse_specific(tmp_path, test_directory, request):
    d = tmp_path / "specific_file"
    d.mkdir()

    test_directory(d.resolve())

    shutil.copyfile(
        request.fspath.dirpath() / "ansible-navigator.yml", d / "specific.yml"
    )

    result = parse_execution_image("specific.yml")

    assert result == "test-ee-image"
