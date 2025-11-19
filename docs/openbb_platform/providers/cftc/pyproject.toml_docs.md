# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/cftc/pyproject.toml`
- **Size**: 622 bytes
- **Lines**: 20
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-cftc"
version = "1.2.0"
description = "The mission of the Commodity Futures Trading Commission (CFTC) is to promote the integrity, resilience, and vibrancy of the U.S. derivatives markets through sound regulation."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_cftc" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
cftc = "openbb_cftc:cftc_provider"

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

**Generated**: 2025-11-19T02:16:48.651281Z
**Generator**: World's Best Repo Book Generator v1.0
