# Documentation: openbb_platform/extensions/commodity/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/commodity/pyproject.toml`
- **Size**: 504 characters, 20 lines
- **Words**: 49
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-commodity"
version = "1.4.0"
description = "Commodity extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_commodity" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
commodity = "openbb_commodity.commodity_router:router"

```

## High-Level Overview

This is a .toml file containing 20 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.910623
- Generator: World's Best Repo Book Generator v1.0.0
