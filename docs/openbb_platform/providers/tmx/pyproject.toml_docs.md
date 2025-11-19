# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/tmx/pyproject.toml`
- **Size**: 670 bytes
- **Lines**: 24
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-tmx"
version = "1.4.0"
description = "Unofficial TMX data provider extension for the OpenBB Platform - Public Canadian markets data for Python and Fast API."
authors = ["OpenBB <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_tmx" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
aiohttp-client-cache = "^0.11.0"
aiosqlite = "^0.20.0"
random-user-agent = "^1.0.1"
exchange-calendars = "^4.5.4"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
tmx = "openbb_tmx:tmx_provider"

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

**Generated**: 2025-11-19T02:16:53.055992Z
**Generator**: World's Best Repo Book Generator v1.0
