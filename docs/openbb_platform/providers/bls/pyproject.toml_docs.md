# File Documentation: pyproject.toml

## Metadata
- **Path**: `openbb_platform/providers/bls/pyproject.toml`
- **Size**: 762 bytes
- **Lines**: 20
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-bls"
version = "1.2.0"
description = "The Bureau of Labor Statistics' (BLS) Public Data Application Programming Interface (API) gives the public access to economic data from all BLS programs. It is the Bureau's hope that talented developers and programmers will use the BLS Public Data API to create original, inventive applications with published BLS data."
authors = ["OpenBB Team <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
packages = [{ include = "openbb_bls" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_provider_extension"]
bls = "openbb_bls:bls_provider"

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

**Generated**: 2025-11-19T02:16:48.350320Z
**Generator**: World's Best Repo Book Generator v1.0
