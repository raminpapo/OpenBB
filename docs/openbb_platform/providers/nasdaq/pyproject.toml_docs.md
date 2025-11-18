# Documentation: openbb_platform/providers/nasdaq/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/nasdaq/pyproject.toml`
- **Size**: 594 characters, 24 lines
- **Words**: 61
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-nasdaq"
version = "1.5.0"
description = "Nasdaq extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_nasdaq" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
openbb-platform-api = "^1.2.1"
async-lru = "^2.0.5"
random-user-agent = "^1.0.1"
nasdaq-data-link = "^1.0.4"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
nasdaq = "openbb_nasdaq:nasdaq_provider"

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
- Generated: 2025-11-18T07:54:40.345950
- Generator: World's Best Repo Book Generator v1.0.0
