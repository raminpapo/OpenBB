# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/pyproject.toml`
- **Size**: 684 bytes
- **Lines**: 27
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-charting"
version = "2.4.0"
description = "Charting extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_charting" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"  # scipy forces python <4.0 explicitly
openbb-core = "^1.5.1"
pandas-ta-openbb = "^0.4.22"
plotly = "^6.3.1"
pywry = { version = "^0.6.2", optional = true }
nbformat = "^5.10.0"

[tool.poetry.extras]
pywry = ["pywry"]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_obbject_extension"]
openbb_charting = "openbb_charting:ext"

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

**Generated**: 2025-11-19T02:16:47.392431Z
**Generator**: World's Best Repo Book Generator v1.0
