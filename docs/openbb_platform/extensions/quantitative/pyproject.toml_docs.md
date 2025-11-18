# Documentation: openbb_platform/extensions/quantitative/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/quantitative/pyproject.toml`
- **Size**: 560 characters, 21 lines
- **Words**: 53
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-quantitative"
version = "1.5.0"
description = "Quantitative Analysis extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_quantitative" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
pandas-ta-openbb = "^0.4.20"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
quantitative = "openbb_quantitative.quantitative_router:router"

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
- Generated: 2025-11-18T07:54:36.333186
- Generator: World's Best Repo Book Generator v1.0.0
