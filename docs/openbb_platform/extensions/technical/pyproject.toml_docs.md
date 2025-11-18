# Documentation: openbb_platform/extensions/technical/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/technical/pyproject.toml`
- **Size**: 679 characters, 25 lines
- **Words**: 60
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-technical"
version = "1.5.0"
description = "Technical Analysis extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_technical" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
pandas-ta-openbb = "^0.4.20"
scikit-learn = "^1.6.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
technical = "openbb_technical.technical_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
technical = "openbb_technical.technical_views:TechnicalViews"

```

## High-Level Overview

This is a .toml file containing 25 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:36.386767
- Generator: World's Best Repo Book Generator v1.0.0
