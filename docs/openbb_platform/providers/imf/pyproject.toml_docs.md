# Documentation: openbb_platform/providers/imf/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/imf/pyproject.toml`
- **Size**: 518 characters, 21 lines
- **Words**: 49
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-imf"
version = "1.2.0"
description = "https://datahelp.imf.org/knowledgebase/articles/630877-api"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_imf" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
async-lru = "^2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
imf = "openbb_imf:imf_provider"

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
- Generated: 2025-11-18T07:54:40.044115
- Generator: World's Best Repo Book Generator v1.0.0
