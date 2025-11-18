# Documentation: openbb_platform/providers/federal_reserve/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/federal_reserve/pyproject.toml`
- **Size**: 569 characters, 21 lines
- **Words**: 54
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-federal-reserve"
version = "1.5.0"
description = "US Federal Reserve Data Extension for OpenBB"
authors = ["OpenBB <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_federal_reserve" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
beautifulsoup4 = "^4.13.4"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
federal_reserve = "openbb_federal_reserve:federal_reserve_provider"

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
- Generated: 2025-11-18T07:54:38.526001
- Generator: World's Best Repo Book Generator v1.0.0
