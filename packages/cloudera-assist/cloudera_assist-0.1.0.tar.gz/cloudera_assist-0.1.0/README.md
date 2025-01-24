# cloudera-assist

A CLI application for managing credentials and executing playbooks for Cloudera demonstrations, workshops, and tutorials.

Built with [![Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

# Install

Install the CLI tool (in your preferred `venv` manager):

```bash
pip install git+https://github.com/cloudera-labs/cloudera-assist.git
```

And then run `cldr-assist` in any `ansible-navigator`-enabled Cloudera project!

# Usage

tk tk

# Develop

`cloudera-assist` uses [uv](https://github.com/astral-sh/uv) and [hatch](https://hatch.pypa.io/latest/) to manage the build process and environments and [pytest](https://docs.pytest.org/en/stable/) for testing.

Install the two management tools to your system, e.g. `brew install uv hatch`.

To work with a CLI development shell, run `hatch shell` to spin up a `venv` with the project's dependencies and some additional libraries for `pytest`.

You can then run tests using `hatch run test`.

Versioning can be handled by `hatch version` and its permutations; the tool is set to manage the `VERSION` variable in `src/cloudera_assist/__version__.py`.

To add a new Python dependency, run `uv add <the library>`. This will update the `pyproject.toml` file and the general `venv` for the project.

# License and Copyright

Copyright 2025, Cloudera, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
