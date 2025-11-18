# Documentation: cli/pyproject.toml

## File Metadata
- **Path**: `cli/pyproject.toml`
- **Size**: 766 characters, 32 lines
- **Words**: 86
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-cli"
version = "1.2.1"
description = "Investment Research for Everyone, Anywhere."
authors = ["OpenBB <hello@openbb.co>"]
packages = [{ include = "openbb_cli" }]
license = "AGPL-3.0-only"
readme = "README.md"
homepage = "https://openbb.co"
repository = "https://github.com/OpenBB-finance/OpenBB"
documentation = "https://docs.openbb.co/cli"

[tool.poetry.scripts]
openbb = 'openbb_cli.cli:main'

[tool.poetry.dependencies]
python = "^3.10,<3.14"

# OpenBB dependencies
openbb = { version = "^4.5.0", extras = ["all"] }

# CLI dependencies
prompt-toolkit = "^3.0.50"
rich = "^14.0.0"
python-dotenv = "^1.0.1"
openpyxl = "^3.1.5"
pywry = "^0.6.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

```

## High-Level Overview

This is a .toml file containing 32 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.702128
- Generator: World's Best Repo Book Generator v1.0.0
