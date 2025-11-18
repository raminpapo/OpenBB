# Documentation: openbb_platform/providers/famafrench/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/famafrench/pyproject.toml`
- **Size**: 656 characters, 26 lines
- **Words**: 56
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-famafrench"
version = "1.1.0"
description = "Fama-French data integration for OpenBB Platform."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_famafrench" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[tool.poetry.scripts]


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
famafranch = "openbb_famafrench:famafrench_provider"

[tool.poetry.plugins."openbb_core_extension"]
famafrench = "openbb_famafrench.famafrench_router:router"

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
- Generated: 2025-11-18T07:54:38.355258
- Generator: World's Best Repo Book Generator v1.0.0
