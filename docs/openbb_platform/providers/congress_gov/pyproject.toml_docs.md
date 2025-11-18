# Documentation: openbb_platform/providers/congress_gov/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/congress_gov/pyproject.toml`
- **Size**: 633 characters, 22 lines
- **Words**: 53
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-congress-gov"
version = "1.1.0"
description = "Congress.gov Provider Extension for the OpenBB Platform"
authors = ["OpenBB Team <hello@openbb.co>"]
readme = "README.md"
packages = [{ include = "openbb_congress_gov" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
congress_gov = "openbb_congress_gov:congress_gov_provider"

[tool.poetry.plugins."openbb_core_extension"]
uscongress = "openbb_congress_gov.router.congress_gov_router:router"

```

## High-Level Overview

This is a .toml file containing 22 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:37.619356
- Generator: World's Best Repo Book Generator v1.0.0
