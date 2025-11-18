# Documentation: openbb_platform/providers/stockgrid/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/stockgrid/pyproject.toml`
- **Size**: 531 characters, 21 lines
- **Words**: 52
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-stockgrid"
version = "1.5.0"
description = "stockgrid extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_stockgrid" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
pytest-freezegun = "^0.4.2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
stockgrid = "openbb_stockgrid:stockgrid_provider"

```

## High-Level Overview

This is a .toml file containing 21 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:41.692326
- Generator: World's Best Repo Book Generator v1.0.0
