# Documentation: openbb_platform/extensions/platform_api/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/platform_api/pyproject.toml`
- **Size**: 712 characters, 24 lines
- **Words**: 73
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-platform-api"
version = "1.2.1"
description = "OpenBB Platform API: Launch script and widgets builder for the OpenBB Platform API and Workspace Backend Connector."
authors = ["OpenBB <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
homepage = "https://openbb.co"
repository = "https://github.com/openbb-finance/openbb"
documentation = "https://docs.openbb.co"
packages = [{ include = "openbb_platform_api" }]

[tool.poetry.scripts]
openbb-api = "openbb_platform_api.main:main"

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
deepdiff = ">=8.6.1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

```

## High-Level Overview

This is a .toml file containing 24 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:36.287803
- Generator: World's Best Repo Book Generator v1.0.0
