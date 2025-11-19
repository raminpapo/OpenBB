# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/extensions/fixedincome/pyproject.toml`
- **Size**: 638 bytes
- **Lines**: 23
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-fixedincome"
version = "1.5.0"
description = "Fixed income extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_fixedincome" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
fixedincome = "openbb_fixedincome.fixedincome_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
fixedincome = "openbb_fixedincome.fixedincome_views:FixedIncomeViews"

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

**Generated**: 2025-11-19T02:16:47.022789Z
**Generator**: World's Best Repo Book Generator v1.0
