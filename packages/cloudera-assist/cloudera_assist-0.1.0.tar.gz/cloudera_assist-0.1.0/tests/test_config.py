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
import yaml

from cloudera_assist.config import Config
from cloudera_assist.credentials import AwsCredentials


def test_file_not_found(tmp_path, test_directory, capsys):
    d = tmp_path / "missing_file"
    d.mkdir()
    test_directory(d.resolve())

    with pytest.raises(SystemExit) as e:
        Config(None, "not-found", False)

    assert e.value.code == 253

    captured = capsys.readouterr()

    assert "File not found" in captured.out


def test_invalid_format(tmp_path, test_directory, capsys):
    d = tmp_path / "invalid_format"
    d.mkdir()
    test_directory(d.resolve())

    bogus = d / "bad-format"
    bogus.write_text("bad: format:", encoding="utf-8")

    with pytest.raises(SystemExit) as e:
        Config(None, "bad-format", False)

    assert e.value.code == 253

    captured = capsys.readouterr()

    assert "Error parsing environment configuration file" in captured.out


def test_default():
    config = Config(None, "cloudera-assist.yml", False)
    config.construct()

    assert len(config.actions) == 1
    assert config.actions[0].label == "Who am I?"

    assert len(config.credentials) == 1
    assert isinstance(config.credentials[0], AwsCredentials)


def test_credentials_invalid(tmp_path, test_directory, capsys):
    d = tmp_path / "invalid_credential"
    d.mkdir()
    test_directory(d.resolve())

    contents = dict(credentials=["bad_type"])

    bogus = d / "bad-type"
    bogus.write_text(yaml.safe_dump(contents), encoding="utf-8")

    with pytest.raises(SystemExit) as e:
        config = Config(None, "bad-type", False)
        config.construct()

    assert e.value.code == 253

    captured = capsys.readouterr()

    assert "Invalid credential type(s)" in captured.out


def test_credentials_aws(tmp_path, test_directory, capsys):
    d = tmp_path / "aws_credential"
    d.mkdir()
    test_directory(d.resolve())

    contents = dict(credentials=["aws"])

    bogus = d / "aws_cred.yml"
    bogus.write_text(yaml.safe_dump(contents), encoding="utf-8")

    with pytest.raises(SystemExit) as e:
        config = Config(None, "aws_cred.yml", False)
        config.construct()

    assert e.value.code == 253

    captured = capsys.readouterr()

    assert "Invalid credential type(s)" in captured.out
