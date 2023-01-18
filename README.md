# Introduction
Template repository for python package.

After duplicating this repository, you may rename the default package name, which is `judilibre-eda`, with your package name wherever it is declared.
So rename it in:
* `pyproject.toml`
* `tests.yaml`
* `launch.json`

# Development setup
## Prerequisites
This following packages must be installed
* python
* poetry
* git

## Configuration
* `poetry` configuration, add environment variable `POETRY_VIRTUALENVS_IN_PROJECT=true`
* `vscode` configuration, add environment variable `PYTHON_VENV_LOC`
  * on windows: `PYTHON_VENV_LOC=.venv\\bin\\python.exe`
  * on linux: `PYTHON_VENV_LOC=.venv/bin/python`
* `git` configuration
```shell
git config --global user.name 'your name'
git config --global user.email 'your email'
```

## Initialization
* First setup `poetry install`
* Then `poetry shell`

# Build and publish with poetry
## Build
Manuel steps to generate and publish the package to TestPyPI with poetry, documentation from [packaging.python](https://python-poetry.org/docs/)

Build the package, generate distribution archives
```shell
poetry build
```

## Publish to Test PyPI
Add Test PyPI as an alternate package repository
```shell
poetry config repositories.testpypi https://test.pypi.org/legacy/
```

Upload/publish package/distribution archive to TestPyPI (a separate instance of the Python Package Index)
```shell
poetry publish -r testpypi
```

## Installation with pip
```shell
pip install --index-url https://test.pypi.org/simple/ judilibre-eda
```
or
```shell
pip3 install --index-url https://test.pypi.org/simple/ judilibre-eda
```

# Code of Conduct

# History (changelog)
