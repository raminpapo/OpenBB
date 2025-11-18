# Documentation: openbb_platform/extensions/currency/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/currency/pyproject.toml`
- **Size**: 607 characters, 23 lines
- **Words**: 53
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-currency"
version = "1.5.0"
description = "Currency extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_currency" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
currency = "openbb_currency.currency_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
currency = "openbb_currency.currency_views:CurrencyViews"

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
- Generated: 2025-11-18T07:54:35.949771
- Generator: World's Best Repo Book Generator v1.0.0
