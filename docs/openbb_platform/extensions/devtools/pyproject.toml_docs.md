# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/extensions/devtools/pyproject.toml`
- **Size**: 844 bytes
- **Lines**: 36
- **Category**: config
- **Extension**: .toml

---

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



---

## High-Level Overview

This is a **config** file named `pyproject.toml`.

**Configuration File**

This file contains configuration settings for the project.


---

## Detailed Analysis

### Configuration Structure

This configuration file defines settings and parameters for the project.


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.847976Z
**Generator**: World's Best Repo Book Generator v1.0
