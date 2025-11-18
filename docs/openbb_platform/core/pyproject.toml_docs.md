# Documentation: openbb_platform/core/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/core/pyproject.toml`
- **Size**: 821 characters, 36 lines
- **Words**: 103
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-core"
version = "1.5.5"
description = "OpenBB package with core functionality."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [
    { include = "openbb_core" },
    { include = "openbb" }
]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
uvicorn = "^0.35.0"
websockets = "^15.0"
pandas = ">=1.5.3"
html5lib = "^1.1"
fastapi = "^0.120.3"
uuid7 = "^0.1.0"
python-multipart = "^0.0.20"
pydantic = "^2.12.3"
requests = "^2.32.5"
importlib-metadata = ">=6.8.0"
python-dotenv = "^1.0.0"
aiohttp = "^3.13.2"
ruff = "^0.13"              # Needed here to lint generated code
pyjwt = "^2.10.1"

[tool.poetry.scripts]
openbb-build = "openbb_core.build:main"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

## High-Level Overview

This is a .toml file containing 36 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.787416
- Generator: World's Best Repo Book Generator v1.0.0
