# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/openbb_charting/__init__.py`
- **Size**: 607 bytes
- **Lines**: 26
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Functions** (1): get_charting_module
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`get_charting_module()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Extension`
- `importlib`
- `openbb_core.app.model.extension`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.401248Z
**Generator**: World's Best Repo Book Generator v1.0
