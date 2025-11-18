# Documentation: openbb_platform/providers/cftc/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/cftc/pyproject.toml`
- **Size**: 622 characters, 20 lines
- **Words**: 70
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-cftc"
version = "1.2.0"
description = "The mission of the Commodity Futures Trading Commission (CFTC) is to promote the integrity, resilience, and vibrancy of the U.S. derivatives markets through sound regulation."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_cftc" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
cftc = "openbb_cftc:cftc_provider"

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
- Generated: 2025-11-18T07:54:37.586853
- Generator: World's Best Repo Book Generator v1.0.0
