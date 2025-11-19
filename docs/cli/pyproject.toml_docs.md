# File Documentation: pyproject.toml

## Metadata
- **Path**: `cli/pyproject.toml`
- **Size**: 766 bytes
- **Lines**: 32
- **Category**: config
- **Extension**: .toml

---

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



---

## High-Level Overview

This is a **config** file named `pyproject.toml`.

**Configuration File**

This file contains configuration settings for the project.


---

## Detailed Analysis

### Configuration Structure

This configuration file defines settings and parameters for the project.


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:15:18.805470Z
**Generator**: World's Best Repo Book Generator v1.0
