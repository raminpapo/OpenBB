# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/congress_gov/pyproject.toml`
- **Size**: 633 bytes
- **Lines**: 22
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-congress-gov"
version = "1.1.0"
description = "Congress.gov Provider Extension for the OpenBB Platform"
authors = ["OpenBB Team <hello@openbb.co>"]
readme = "README.md"
packages = [{ include = "openbb_congress_gov" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
congress_gov = "openbb_congress_gov:congress_gov_provider"

[tool.poetry.plugins."openbb_core_extension"]
uscongress = "openbb_congress_gov.router.congress_gov_router:router"

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

**Generated**: 2025-11-19T02:16:48.684388Z
**Generator**: World's Best Repo Book Generator v1.0
