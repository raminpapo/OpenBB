# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/multpl/pyproject.toml`
- **Size**: 473 bytes
- **Lines**: 20
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-multpl"
version = "1.2.0"
description = "Public data on historical S&P Multiples."
authors = ["OpenBB Team <hello@openbb.co>"]
readme = "README.md"
packages = [{ include = "openbb_multpl" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
multpl = "openbb_multpl:multpl_provider"

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

**Generated**: 2025-11-19T02:16:51.602670Z
**Generator**: World's Best Repo Book Generator v1.0
