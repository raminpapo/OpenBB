# File Documentation: conftest.py

## Metadata
- **Path**: `openbb_platform/conftest.py`
- **Size**: 1,263 bytes
- **Lines**: 47
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Root configuration for pytest."""

# flake8: noqa: S101
# pylint: disable=unused-argument,unused-import

import os
from pathlib import Path

import pytest  # noqa: F401

ROOT_DIR = Path(__file__).parent


def pytest_configure():
    """Set environment variables for testing."""
    os.environ["OPENBB_AUTO_BUILD"] = "true"


def pytest_collection_modifyitems(config, items):
    """Modify test collection to ensure cleanup-dependent tests run first."""
    # Find tests that should run early (checking clean state)
    early_tests: list = []
    other_tests: list = []

    for item in items:
        # Tests that check repository state should run first
        if (
            "repository_state" in item.name.lower()
            or "extension_map" in item.name.lower()
            or item.get_closest_marker("order")
        ):
            early_tests.append(item)
        else:
            other_tests.append(item)

    # Sort early tests by their order marker if present
    early_tests.sort(
        key=lambda x: (
            getattr(x.get_closest_marker("order"), "args", [999])[0]
            if x.get_closest_marker("order")
            else 999
        )
    )

    # Reorder: early tests first, then others
    items[:] = early_tests + other_tests

```



---

## High-Level Overview

This is a **python** file named `conftest.py`.

**Python Module**

- **Functions** (2): pytest_configure, pytest_collection_modifyitems
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`pytest_configure()`**
- **`pytest_collection_modifyitems(config, items)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Path`
- `import`
- `pathlib`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.119681Z
**Generator**: World's Best Repo Book Generator v1.0
