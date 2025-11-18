# Documentation: openbb_platform/obbject_extensions/charting/openbb_charting/__init__.py

## File Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/openbb_charting/__init__.py`
- **Size**: 607 characters, 26 lines
- **Words**: 44
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OpenBB OBBject extension for charting."""

import warnings

from openbb_core.app.model.extension import Extension

warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module="openbb_core.app.model.extension",
)


def get_charting_module():
    """Get the Charting module."""
    # pylint: disable=import-outside-toplevel
    import importlib

    _Charting = importlib.import_module("openbb_charting.charting").Charting
    return _Charting


ext = Extension(name="charting", description="Create custom charts from OBBject data.")

Charting = ext.obbject_accessor(get_charting_module())

```

## High-Level Overview

OpenBB OBBject extension for charting.

import warnings

from openbb_core.app.model.extension import Extension

warnings.filterwarnings(
"ignore",
category=UserWarning,
module="openbb_core.app.model.extension",
)


def get_charting_module():
Get the Charting module.
pylint: disable=import-outside-toplevel

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`get_charting_module`

**Imports** (5):
`warnings`, `openbb_core.app.model.extension`, `Extension`, `importlib`, `OBBject`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `warnings`
- `openbb_core.app.model.extension`
- `importlib`

## Notes
- Generated: 2025-11-18T07:54:36.424258
- Generator: World's Best Repo Book Generator v1.0.0
