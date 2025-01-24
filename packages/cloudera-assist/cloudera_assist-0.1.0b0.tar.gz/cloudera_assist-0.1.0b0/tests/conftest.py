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

from pathlib import Path
from unittest import mock

import pytest


@pytest.fixture(autouse=True)
def test_directory(request, monkeypatch):
    """
    Change current working directory to test directory.
    Optionally, update the working directory to the given Path.

    Args:
        request (FixtureRequest): Pytest request
        monkeypatch (MonkeyPatch): Pytest monkeypatch

    Returns:
        _type_: _description_
    """
    monkeypatch.chdir(request.fspath.dirname)

    def chdir(directory: Path):
        monkeypatch.chdir(directory)

    return chdir


@pytest.fixture(autouse=True)
def test_env():
    """
    Clear and set a working os.environ for a test.

    Args:

    Returns:
        _type_: _description_
    """
    with mock.patch.dict(os.environ, clear=True):
        yield
