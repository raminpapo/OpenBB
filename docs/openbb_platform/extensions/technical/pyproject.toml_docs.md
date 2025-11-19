# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/extensions/technical/pyproject.toml`
- **Size**: 679 bytes
- **Lines**: 25
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-technical"
version = "1.5.0"
description = "Technical Analysis extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_technical" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
pandas-ta-openbb = "^0.4.20"
scikit-learn = "^1.6.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
technical = "openbb_technical.technical_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
technical = "openbb_technical.technical_views:TechnicalViews"

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

**Generated**: 2025-11-19T02:16:47.308444Z
**Generator**: World's Best Repo Book Generator v1.0
