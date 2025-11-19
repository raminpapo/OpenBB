# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/extensions/derivatives/pyproject.toml`
- **Size**: 637 bytes
- **Lines**: 23
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-derivatives"
version = "1.5.0"
description = "Derivatives extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_derivatives" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
derivatives = "openbb_derivatives.derivatives_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
derivatives = "openbb_derivatives.derivatives_views:DerivativesViews"

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

**Generated**: 2025-11-19T02:16:46.803715Z
**Generator**: World's Best Repo Book Generator v1.0
