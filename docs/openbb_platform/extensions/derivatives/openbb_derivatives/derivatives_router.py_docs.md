# File Documentation: derivatives_router.py

## Metadata
- **Path**: `openbb_platform/extensions/derivatives/openbb_derivatives/derivatives_router.py`
- **Size**: 372 bytes
- **Lines**: 11
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Derivatives Router."""

from openbb_core.app.router import Router

from openbb_derivatives.futures.futures_router import router as futures_router
from openbb_derivatives.options.options_router import router as options_router

router = Router(prefix="", description="Derivatives market data.")
router.include_router(options_router)
router.include_router(futures_router)

```



---

## High-Level Overview

This is a **python** file named `derivatives_router.py`.

**Python Module**

- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Router`
- `openbb_core.app.router`
- `openbb_derivatives.futures.futures_router`
- `openbb_derivatives.options.options_router`
- `router`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.811072Z
**Generator**: World's Best Repo Book Generator v1.0
