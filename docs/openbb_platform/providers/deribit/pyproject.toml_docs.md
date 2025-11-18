# Documentation: openbb_platform/providers/deribit/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/deribit/pyproject.toml`
- **Size**: 532 characters, 21 lines
- **Words**: 54
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-deribit"
version = "1.1.0"
description = "Deribit is a crypto-native derivatives exchange."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_deribit" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
async-lru = "^2.0.4"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
deribit = "openbb_deribit:deribit_provider"

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
- Generated: 2025-11-18T07:54:37.664239
- Generator: World's Best Repo Book Generator v1.0.0
