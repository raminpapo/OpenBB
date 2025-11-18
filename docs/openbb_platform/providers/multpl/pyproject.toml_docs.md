# Documentation: openbb_platform/providers/multpl/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/multpl/pyproject.toml`
- **Size**: 473 characters, 20 lines
- **Words**: 48
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-multpl"
version = "1.2.0"
description = "Public data on historical S&P Multiples."
authors = ["OpenBB Team <hello@openbb.co>"]
readme = "README.md"
packages = [{ include = "openbb_multpl" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
multpl = "openbb_multpl:multpl_provider"

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
- Generated: 2025-11-18T07:54:40.300303
- Generator: World's Best Repo Book Generator v1.0.0
