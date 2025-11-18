# Documentation: openbb_platform/extensions/devtools/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/devtools/pyproject.toml`
- **Size**: 844 characters, 36 lines
- **Words**: 105
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-devtools"
version = "1.5.3"
description = "Tools for OpenBB Platform Developers"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_devtools" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"              # scipy forces <4.0 explicitly
ruff = "^0.13"
pylint = "^3.3"
mypy = "^1.12.1"
pydocstyle = "^6.3.0"
black = "^25.1.0"
bandit = "^1.7.5"
codespell = "^2.2.5"
pre-commit = "^3.5.0"
tox = "^4.11.3"
pytest = ">=8.4.1"
pytest-subtests = "^0.11.0"
pytest-recorder = ">=0.6.1"
pytest-asyncio = "^0.23.2"
pytest-order = "^1.3.0"
pytest-cov = "^4.1.0"
ipykernel = "^6.30.1"
types-python-dateutil = "^2.8.19.14"
types-toml = "^0.10.8.7"
poetry = ">=2.1.3"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

## High-Level Overview

This is a .toml file containing 36 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.996779
- Generator: World's Best Repo Book Generator v1.0.0
