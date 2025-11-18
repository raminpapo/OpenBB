# Documentation: cookiecutter/pyproject.toml

## File Metadata
- **Path**: `cookiecutter/pyproject.toml`
- **Size**: 684 characters, 25 lines
- **Words**: 62
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-cookiecutter"
version = "0.4.0"
description = "Extensions template for the OpenBB Python Package."
license = "AGPL-3.0-only"
authors = ["OpenBB Team <hello@openbb.co>"]
packages = [{ include = "openbb_cookiecutter" }]
readme = "README.md"
homepage = "https://openbb.co"
repository = "https://github.com/OpenBB-finance/openbb-cookiecutter"

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
cookiecutter = "^2.6.0"

[tool.poetry.scripts]
openbb-cookiecutter = "openbb_cookiecutter.cli:main"

[tool.poetry.plugins."cookiecutter.templates"]
openbb = "openbb_cookiecutter"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

## High-Level Overview

This is a .toml file containing 25 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.770353
- Generator: World's Best Repo Book Generator v1.0.0
