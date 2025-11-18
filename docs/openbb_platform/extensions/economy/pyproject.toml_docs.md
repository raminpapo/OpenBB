# Documentation: openbb_platform/extensions/economy/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/economy/pyproject.toml`
- **Size**: 597 characters, 23 lines
- **Words**: 53
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-economy"
version = "1.5.0"
description = "Economy extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_economy" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
economy = "openbb_economy.economy_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
economy = "openbb_economy.economy_views:EconomyViews"

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
- Generated: 2025-11-18T07:54:36.053420
- Generator: World's Best Repo Book Generator v1.0.0
