# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/government_us/pyproject.toml`
- **Size**: 556 bytes
- **Lines**: 21
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-government-us"
version = "1.5.0"
description = "US Government Data Extension for OpenBB"
authors = ["OpenBB <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_government_us" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
random-user-agent = "^1.0.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
government_us = "openbb_government_us:government_us_provider"

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

**Generated**: 2025-11-19T02:16:51.205331Z
**Generator**: World's Best Repo Book Generator v1.0
