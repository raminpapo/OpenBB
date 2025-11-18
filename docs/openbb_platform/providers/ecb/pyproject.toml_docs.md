# Documentation: openbb_platform/providers/ecb/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/ecb/pyproject.toml`
- **Size**: 489 characters, 21 lines
- **Words**: 52
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-ecb"
version = "1.5.0"
description = "ECB extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_ecb" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
xmltodict = "^0.13.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
ecb = "openbb_ecb:ecb_provider"

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
- Generated: 2025-11-18T07:54:37.702289
- Generator: World's Best Repo Book Generator v1.0.0
