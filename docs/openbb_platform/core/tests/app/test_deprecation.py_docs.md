# File Documentation: test_deprecation.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/test_deprecation.py`
- **Size**: 1,077 bytes
- **Lines**: 28
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test deprecated commands."""

import unittest

from openbb_core.app.static.package_builder import PathHandler
from openbb_core.app.version import VERSION, get_major_minor


class DeprecatedCommandsTest(unittest.TestCase):
    """Test deprecated commands."""

    def test_deprecated_commands(self):
        """Test deprecated commands."""
        current_major_minor = get_major_minor(VERSION)
        route_map = PathHandler.build_route_map()

        for path, route in route_map.items():
            with self.subTest(i=path):
                if getattr(route, "deprecated", False):
                    deprecation_message = getattr(route, "summary", "")
                    if hasattr(deprecation_message, "metadata"):
                        obb_deprecation_warning = deprecation_message.metadata

                        assert (
                            obb_deprecation_warning.expected_removal
                            != current_major_minor
                        ), f"The expected removal version of `{path}` matches the current version, please remove it."

```



---

## High-Level Overview

This is a **python** file named `test_deprecation.py`.

**Python Module**

- **Classes** (1): DeprecatedCommandsTest
- **Functions** (1): test_deprecated_commands
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`DeprecatedCommandsTest`**(unittest.TestCase)

#### Functions

- **`test_deprecated_commands(self)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `PathHandler`
- `VERSION`
- `openbb_core.app.static.package_builder`
- `openbb_core.app.version`
- `unittest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.636280Z
**Generator**: World's Best Repo Book Generator v1.0
