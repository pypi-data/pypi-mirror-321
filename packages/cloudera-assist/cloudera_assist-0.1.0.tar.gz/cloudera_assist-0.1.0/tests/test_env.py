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
import pytest

from pathlib import Path

from cloudera_assist.env import EnvFile


def test_file_not_found(tmp_path, test_directory, capsys):
    d = tmp_path / "missing_file"
    d.mkdir()

    test_directory(d.resolve())

    with pytest.raises(SystemExit) as e:
        env = EnvFile("not-found")
        env.read_env()

    assert e.value.code == 254

    captured = capsys.readouterr()

    assert "File not found" in captured.out


@pytest.mark.skip("Need to convert to use a Mock exception out of the dotenv parser")
def test_invalid_format(tmp_path, test_directory, capsys):
    d = tmp_path / "invalid_format"
    d.mkdir()

    test_directory(d.resolve())

    bogus = d / "bad-format"
    bogus.write_text('a="\nb=c', encoding="utf-8")

    with pytest.raises(SystemExit) as e:
        env = EnvFile("bad-format")
        env.read_env()

    assert e.value.code == 254

    captured = capsys.readouterr()

    assert "Error parsing environment configuration file" in captured.out


@pytest.mark.skip("Set up click testing for prompts")
def test_touch_true():
    pass


@pytest.mark.skip("Set up click testing for prompts")
def test_touch_false():
    pass


def test_read():
    results = EnvFile("example.env").read_env()

    assert results == True
    assert os.environ["BARE"] == "bare"
    assert os.environ["BARE_SPACE"] == "space"
    assert os.environ["QUOTED"] == "quoted"
    assert os.environ["QUOTED_SPACE"] == "quoted space"
    assert os.environ["QUOTED_QUOTE"] == 'quote"d'
    assert os.environ["COMMENTS"] == "comments"
    assert os.environ["COMMENTED_COMMENT"] == "comm#ent"


def test_get():
    results = EnvFile("example.env").get_env()

    assert results["BARE"] == "bare"
    assert results["BARE_SPACE"] == "space"
    assert results["QUOTED"] == "quoted"
    assert results["QUOTED_SPACE"] == "quoted space"
    assert results["QUOTED_QUOTE"] == 'quote"d'
    assert results["COMMENTS"] == "comments"
    assert results["COMMENTED_COMMENT"] == "comm#ent"


def test_set(tmp_path):
    d = tmp_path / "set_env"
    d.mkdir()

    config = d / "set.env"
    Path(config).touch()

    EnvFile(config).set_env(dict(foo="bar"))

    results = config.read_text()

    assert "foo='bar'\n" in results
    assert "ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES='foo'" in results
    assert os.environ["foo"] == "bar"
    assert os.environ["ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES"] == "foo"


def test_set_existing(tmp_path):
    d = tmp_path / "set_env"
    d.mkdir()

    config = d / "set_existing.env"
    config.write_text("STUFF=stuff", "utf-8")

    EnvFile(config).set_env(dict(foo="bar"))

    results = config.read_text()

    assert "STUFF=stuff\n" in results
    assert "foo='bar'\n" in results
    assert "ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES='foo'" in results
    assert os.environ["foo"] == "bar"
    assert os.environ["ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES"] == "foo"


def test_set_overwrite(tmp_path):
    d = tmp_path / "set_env"
    d.mkdir()

    config = d / "set_overwrite.env"
    config.write_text("STUFF=stuff", "utf-8")

    EnvFile(config).set_env(dict(STUFF="bar"))

    results = config.read_text()

    assert "STUFF='bar'\n" in results
    assert "ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES='STUFF'" in results
    assert os.environ["STUFF"] == "bar"
    assert os.environ["ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES"] == "STUFF"


def test_set_multiple(tmp_path):
    d = tmp_path / "set_env"
    d.mkdir()

    config = d / "set_multiple.env"
    Path(config).touch()

    EnvFile(config).set_env(dict(foo="bar", gaz="blarg"))

    results = config.read_text()

    assert "foo='bar'\n" in results
    assert "gaz='blarg'\n" in results
    assert "ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES='foo,gaz'" in results
    assert os.environ["foo"] == "bar"
    assert os.environ["gaz"] == "blarg"
    assert os.environ["ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES"] == "foo,gaz"


def test_unset(tmp_path):
    d = tmp_path / "unset_env"
    d.mkdir()

    config = d / "unset.env"
    with open(config, "w", encoding="utf-8") as file:
        file.write("STUFF=stuff\n")
        file.write("ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES='STUFF'\n")

    env_file = EnvFile(config)
    env_file.read_env()
    env_file.unset_env(["STUFF"])

    results = config.read_text()

    assert results == ""
    assert "STUFF" not in os.environ
    assert "ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES" not in os.environ


def test_unset_multiple(tmp_path):
    d = tmp_path / "unset_env"
    d.mkdir()

    config = d / "unset_multiple.env"
    with open(config, "w", encoding="utf-8") as file:
        file.write("foo='bar'\n")
        file.write("gaz='blarg'\n")
        file.write("der='yugh'\n")
        file.write("ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES='der,foo,gaz'\n")

    env_file = EnvFile(config)
    env_file.read_env()
    env_file.unset_env(["foo"])

    results = config.read_text()

    assert "foo" not in results
    assert "gaz='blarg'\n" in results
    assert "der='yugh'\n" in results
    assert "ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES='der,gaz'" in results
    assert "foo" not in os.environ
    assert os.environ["gaz"] == "blarg"
    assert os.environ["der"] == "yugh"
    assert os.environ["ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES"] == "der,gaz"
