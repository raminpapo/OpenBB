# Documentation: openbb_platform/obbject_extensions/charting/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/pyproject.toml`
- **Size**: 684 characters, 27 lines
- **Words**: 78
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-charting"
version = "2.4.0"
description = "Charting extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_charting" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"  # scipy forces python <4.0 explicitly
openbb-core = "^1.5.1"
pandas-ta-openbb = "^0.4.22"
plotly = "^6.3.1"
pywry = { version = "^0.6.2", optional = true }
nbformat = "^5.10.0"

[tool.poetry.extras]
pywry = ["pywry"]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_obbject_extension"]
openbb_charting = "openbb_charting:ext"

```

## High-Level Overview

This is a .toml file containing 27 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:37.206360
- Generator: World's Best Repo Book Generator v1.0.0
