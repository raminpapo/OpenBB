# Documentation: openbb_platform/core/tests/app/test_deprecation.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/test_deprecation.py`
- **Size**: 1,077 characters, 28 lines
- **Words**: 71
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test deprecated commands.

import unittest

from openbb_core.app.static.package_builder import PathHandler
from openbb_core.app.version import VERSION, get_major_minor


class DeprecatedCommandsTest(unittest.TestCase):
Test deprecated commands.
Test deprecated commands.
current_major_minor = get_major_minor(VERSION)
route_map = PathHandler.build_route_map()

for path, route in route_map.items():
with self.subTest(i=path):
if getattr(route, "deprecated", False):
deprecation_message = getattr(route, "summary", "")
if hasattr(deprecation_message, "metadata"):
obb_deprecation_warning = deprecation_message.metadata

## Detailed Structure

### Python File Structure

**Classes** (1):
`DeprecatedCommandsTest`

**Functions** (1):
`test_deprecated_commands`

**Imports** (5):
`unittest`, `openbb_core.app.static.package_builder`, `PathHandler`, `openbb_core.app.version`, `VERSION`


## Key Components

**Class `DeprecatedCommandsTest`**: Test deprecated commands.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest`
- `openbb_core.app.static.package_builder`
- `openbb_core.app.version`

## Notes
- Generated: 2025-11-18T07:54:35.867181
- Generator: World's Best Repo Book Generator v1.0.0
