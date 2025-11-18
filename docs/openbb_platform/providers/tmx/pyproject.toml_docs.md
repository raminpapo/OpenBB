# Documentation: openbb_platform/providers/tmx/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/tmx/pyproject.toml`
- **Size**: 670 characters, 24 lines
- **Words**: 75
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-tmx"
version = "1.4.0"
description = "Unofficial TMX data provider extension for the OpenBB Platform - Public Canadian markets data for Python and Fast API."
authors = ["OpenBB <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_tmx" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
aiohttp-client-cache = "^0.11.0"
aiosqlite = "^0.20.0"
random-user-agent = "^1.0.1"
exchange-calendars = "^4.5.4"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
tmx = "openbb_tmx:tmx_provider"

```

## High-Level Overview

This is a .toml file containing 24 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:41.825401
- Generator: World's Best Repo Book Generator v1.0.0
