# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/sec/pyproject.toml`
- **Size**: 628 bytes
- **Lines**: 27
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-sec"
version = "1.5.0"
description = "SEC extension for OpenBB"
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_sec" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
aiohttp-client-cache = "^0.11.0"
aiosqlite = "^0.20.0"
xmltodict = "^0.13.0"
beautifulsoup4 = "^4.12"
lxml = "^5.2.1"
trafilatura = "^2.0"
inscriptis = "^2.5.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
sec = "openbb_sec:sec_provider"

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

**Generated**: 2025-11-19T02:16:51.964496Z
**Generator**: World's Best Repo Book Generator v1.0
