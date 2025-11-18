# Documentation: openbb_platform/providers/government_us/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/government_us/pyproject.toml`
- **Size**: 556 characters, 21 lines
- **Words**: 53
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-government-us"
version = "1.5.0"
description = "US Government Data Extension for OpenBB"
authors = ["OpenBB <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_government_us" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
random-user-agent = "^1.0.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
government_us = "openbb_government_us:government_us_provider"

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
- Generated: 2025-11-18T07:54:39.919537
- Generator: World's Best Repo Book Generator v1.0.0
