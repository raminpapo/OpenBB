# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/extensions/platform_api/pyproject.toml`
- **Size**: 712 bytes
- **Lines**: 24
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-platform-api"
version = "1.2.1"
description = "OpenBB Platform API: Launch script and widgets builder for the OpenBB Platform API and Workspace Backend Connector."
authors = ["OpenBB <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
homepage = "https://openbb.co"
repository = "https://github.com/openbb-finance/openbb"
documentation = "https://docs.openbb.co"
packages = [{ include = "openbb_platform_api" }]

[tool.poetry.scripts]
openbb-api = "openbb_platform_api.main:main"

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
deepdiff = ">=8.6.1"

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

**Generated**: 2025-11-19T02:16:47.183056Z
**Generator**: World's Best Repo Book Generator v1.0
