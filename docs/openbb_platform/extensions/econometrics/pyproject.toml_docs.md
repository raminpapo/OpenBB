# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/extensions/econometrics/pyproject.toml`
- **Size**: 747 bytes
- **Lines**: 26
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-econometrics"
version = "1.6.0"
description = "Econometrics Toolkit for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_econometrics" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"  # scipy forces python <4.0 explicitly
openbb-core = "^1.5.1"
pandas-ta-openbb = "^0.4.20"
arch = "^7.2"
linearmodels = "^6"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
econometrics = "openbb_econometrics.econometrics_router:router"

[tool.poetry.plugins."openbb_charting_extension"]
econometrics = "openbb_econometrics.econometrics_views:EconometricsViews"
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

**Generated**: 2025-11-19T02:16:46.863591Z
**Generator**: World's Best Repo Book Generator v1.0
