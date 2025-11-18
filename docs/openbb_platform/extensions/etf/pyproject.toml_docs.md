# Documentation: openbb_platform/extensions/etf/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/etf/pyproject.toml`
- **Size**: 557 characters, 23 lines
- **Words**: 53
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-etf"
version = "1.5.0"
description = "ETF extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_etf" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
etf = "openbb_etf.etf_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
etf = "openbb_etf.etf_views:EtfViews"

```

## High-Level Overview

This is a .toml file containing 23 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:36.121615
- Generator: World's Best Repo Book Generator v1.0.0
