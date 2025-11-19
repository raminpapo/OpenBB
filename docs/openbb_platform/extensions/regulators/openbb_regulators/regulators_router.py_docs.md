# File Documentation: regulators_router.py

## Metadata
- **Path**: `openbb_platform/extensions/regulators/openbb_regulators/regulators_router.py`
- **Size**: 418 bytes
- **Lines**: 16
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
# pylint: disable=import-outside-toplevel
# pylint: disable=unused-import
# ruff: noqa: F401
"""Regulators Router."""

from openbb_core.app.router import Router

from .cftc.cftc_router import (
    router as cftc_router,
)
from .sec.sec_router import router as sec_router

router = Router(prefix="", description="Financial market regulators data.")
router.include_router(sec_router)
router.include_router(cftc_router)

```



---

## High-Level Overview

This is a **python** file named `regulators_router.py`.

**Python Module**

- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `.cftc.cftc_router`
- `.sec.sec_router`
- `Router`
- `openbb_core.app.router`
- `router`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.288848Z
**Generator**: World's Best Repo Book Generator v1.0
