# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/alpha_vantage/pyproject.toml`
- **Size**: 527 bytes
- **Lines**: 20
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-alpha-vantage"
version = "1.5.0"
description = "Alpha Vantage extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_alpha_vantage" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
alpha_vantage = "openbb_alpha_vantage:alpha_vantage_provider"

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

**Generated**: 2025-11-19T02:16:48.242377Z
**Generator**: World's Best Repo Book Generator v1.0
