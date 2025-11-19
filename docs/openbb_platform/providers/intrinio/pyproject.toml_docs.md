# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/intrinio/pyproject.toml`
- **Size**: 523 bytes
- **Lines**: 21
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-intrinio"
version = "1.5.0"
description = "Intrinio extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_intrinio" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
requests-cache = "^1.1.0"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
intrinio = "openbb_intrinio:intrinio_provider"

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

**Generated**: 2025-11-19T02:16:51.380680Z
**Generator**: World's Best Repo Book Generator v1.0
