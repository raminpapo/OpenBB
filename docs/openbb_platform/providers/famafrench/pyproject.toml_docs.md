# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/famafrench/pyproject.toml`
- **Size**: 656 bytes
- **Lines**: 26
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-famafrench"
version = "1.1.0"
description = "Fama-French data integration for OpenBB Platform."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_famafrench" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[tool.poetry.scripts]


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
famafranch = "openbb_famafrench:famafrench_provider"

[tool.poetry.plugins."openbb_core_extension"]
famafrench = "openbb_famafrench.famafrench_router:router"

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

**Generated**: 2025-11-19T02:16:49.437960Z
**Generator**: World's Best Repo Book Generator v1.0
