# Documentation: openbb_platform/providers/cboe/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/cboe/pyproject.toml`
- **Size**: 528 characters, 22 lines
- **Words**: 55
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-cboe"
version = "1.5.0"
description = "CBOE extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_cboe" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
aiohttp-client-cache = "^0.11.0"
aiosqlite = "^0.20.0"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
cboe = "openbb_cboe:cboe_provider"

```

## High-Level Overview

This is a .toml file containing 22 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:37.484138
- Generator: World's Best Repo Book Generator v1.0.0
