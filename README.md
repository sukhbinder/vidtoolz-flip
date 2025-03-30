# vidtoolz-flip

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-flip.svg)](https://pypi.org/project/vidtoolz-flip/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-flip?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-flip/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-flip/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-flip/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-flip/blob/main/LICENSE)

Flip a vedio vertically or horizontally

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-flip
```
## Usage

type ``vid flip --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-flip
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
