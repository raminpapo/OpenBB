# File Documentation: pytest.ini

## Metadata
- **Path**: `pytest.ini`
- **Size**: 200 bytes
- **Lines**: 9
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
    openbb_platform/**/tests

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

**Generated**: 2025-11-19T02:15:18.717663Z
**Generator**: World's Best Repo Book Generator v1.0
