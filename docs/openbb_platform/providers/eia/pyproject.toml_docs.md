# Documentation: openbb_platform/providers/eia/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/eia/pyproject.toml`
- **Size**: 748 characters, 23 lines
- **Words**: 87
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-us-eia"
version = "1.2.0"
description = "The U.S. Energy Information Administration is committed to its free and open data by making it available through an Application Programming Interface (API) and its open data tools. See https://www.eia.gov/opendata/ for more information."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_us_eia" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
async-lru = "^2.0.4"
openpyxl = "^3.1.5"
xlrd = "^2.0.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
us_eia = "openbb_us_eia:eia_provider"

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
- Generated: 2025-11-18T07:54:38.288996
- Generator: World's Best Repo Book Generator v1.0.0
