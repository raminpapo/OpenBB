# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/eia/pyproject.toml`
- **Size**: 748 bytes
- **Lines**: 23
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-us-eia"
version = "1.2.0"
description = "The U.S. Energy Information Administration is committed to its free and open data by making it available through an Application Programming Interface (API) and its open data tools. See https://www.eia.gov/opendata/ for more information."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_us_eia" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
async-lru = "^2.0.4"
openpyxl = "^3.1.5"
xlrd = "^2.0.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
us_eia = "openbb_us_eia:eia_provider"

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

**Generated**: 2025-11-19T02:16:49.373882Z
**Generator**: World's Best Repo Book Generator v1.0
