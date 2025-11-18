# Documentation: openbb_platform/extensions/crypto/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/crypto/pyproject.toml`
- **Size**: 587 characters, 23 lines
- **Words**: 53
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-crypto"
version = "1.5.0"
description = "Crypto extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_crypto" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
crypto = "openbb_crypto.crypto_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
crypto = "openbb_crypto.crypto_views:CryptoViews"

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
- Generated: 2025-11-18T07:54:35.929077
- Generator: World's Best Repo Book Generator v1.0.0
