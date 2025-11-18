# Documentation: openbb_platform/providers/sec/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/sec/pyproject.toml`
- **Size**: 628 characters, 27 lines
- **Words**: 70
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-sec"
version = "1.5.0"
description = "SEC extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_sec" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
aiohttp-client-cache = "^0.11.0"
aiosqlite = "^0.20.0"
xmltodict = "^0.13.0"
beautifulsoup4 = "^4.12"
lxml = "^5.2.1"
trafilatura = "^2.0"
inscriptis = "^2.5.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
sec = "openbb_sec:sec_provider"

```

## High-Level Overview

This is a .toml file containing 27 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.651370
- Generator: World's Best Repo Book Generator v1.0.0
