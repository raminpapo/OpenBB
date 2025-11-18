# Documentation: openbb_platform/providers/bls/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/providers/bls/pyproject.toml`
- **Size**: 762 characters, 20 lines
- **Words**: 94
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-bls"
version = "1.2.0"
description = "The Bureau of Labor Statistics' (BLS) Public Data Application Programming Interface (API) gives the public access to economic data from all BLS programs. It is the Bureau's hope that talented developers and programmers will use the BLS Public Data API to create original, inventive applications with published BLS data."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_bls" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
bls = "openbb_bls:bls_provider"

```

## High-Level Overview

This is a .toml file containing 20 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:37.444404
- Generator: World's Best Repo Book Generator v1.0.0
