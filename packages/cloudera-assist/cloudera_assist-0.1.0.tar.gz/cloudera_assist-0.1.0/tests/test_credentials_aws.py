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
from cloudera_assist.env import EnvFile


def test_list_profiles():
    creds = AwsCredentials(None, False)

    profiles = creds.list_profiles()

    assert isinstance(profiles, list)


def test_apply(tmp_path, test_directory):
    d = tmp_path / "apply"
    d.mkdir()
    test_directory(d.resolve())

    env_file = d / "test-apply"
    env_file.touch()

    creds = AwsCredentials(EnvFile(env_file), False)
    creds.selected = 1

    creds.apply()

    results = env_file.read_text()
    assert results == "boom"
