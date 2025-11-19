# File Documentation: pytest.ini

## Metadata
- **Path**: `cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/pytest.ini`
- **Size**: 171 bytes
- **Lines**: 8
- **Category**: config
- **Extension**: .ini

---

## Original Source

```
[pytest]
addopts = -p no:warnings
markers =
    linux: tests that are not stable on Windows
    integration: OpenBB Platform integration test marker
testpaths =
    tests

```



---

## High-Level Overview

This is a **config** file named `pytest.ini`.

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

**Generated**: 2025-11-19T02:16:44.949812Z
**Generator**: World's Best Repo Book Generator v1.0
