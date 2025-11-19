# File Documentation: pyproject.toml

## Metadata
- **Path**: `cookiecutter/pyproject.toml`
- **Size**: 684 bytes
- **Lines**: 25
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
[tool.poetry]
name = "openbb-cookiecutter"
version = "0.4.0"
description = "Extensions template for the OpenBB Python Package."
license = "AGPL-3.0-only"
authors = ["OpenBB Team <hello@openbb.co>"]
packages = [{ include = "openbb_cookiecutter" }]
readme = "README.md"
homepage = "https://openbb.co"
repository = "https://github.com/OpenBB-finance/openbb-cookiecutter"

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
cookiecutter = "^2.6.0"

[tool.poetry.scripts]
openbb-cookiecutter = "openbb_cookiecutter.cli:main"

[tool.poetry.plugins."cookiecutter.templates"]
openbb = "openbb_cookiecutter"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

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

**Generated**: 2025-11-19T02:16:44.938120Z
**Generator**: World's Best Repo Book Generator v1.0
