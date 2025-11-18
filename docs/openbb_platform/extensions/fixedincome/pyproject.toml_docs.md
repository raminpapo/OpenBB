# Documentation: openbb_platform/extensions/fixedincome/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/fixedincome/pyproject.toml`
- **Size**: 638 characters, 23 lines
- **Words**: 54
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-fixedincome"
version = "1.5.0"
description = "Fixed income extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_fixedincome" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
fixedincome = "openbb_fixedincome.fixedincome_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
fixedincome = "openbb_fixedincome.fixedincome_views:FixedIncomeViews"

```

## High-Level Overview

This is a .toml file containing 23 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:36.155971
- Generator: World's Best Repo Book Generator v1.0.0
