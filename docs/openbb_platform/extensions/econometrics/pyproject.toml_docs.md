# Documentation: openbb_platform/extensions/econometrics/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/econometrics/pyproject.toml`
- **Size**: 747 characters, 26 lines
- **Words**: 68
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-econometrics"
version = "1.6.0"
description = "Econometrics Toolkit for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_econometrics" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"  # scipy forces python <4.0 explicitly
openbb-core = "^1.5.1"
pandas-ta-openbb = "^0.4.20"
arch = "^7.2"
linearmodels = "^6"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
econometrics = "openbb_econometrics.econometrics_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
econometrics = "openbb_econometrics.econometrics_views:EconometricsViews"
```

## High-Level Overview

This is a .toml file containing 26 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:36.022306
- Generator: World's Best Repo Book Generator v1.0.0
