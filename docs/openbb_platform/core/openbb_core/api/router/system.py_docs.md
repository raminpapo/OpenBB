# File Documentation: system.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/api/router/system.py`
- **Size**: 459 bytes
- **Lines**: 18
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""System router."""

from typing import Annotated

from fastapi import APIRouter, Depends
from openbb_core.api.dependency.system import get_system_settings
from openbb_core.app.model.system_settings import SystemSettings

router = APIRouter(prefix="/system", tags=["System"])


@router.get("")
async def get_system_model(
    system_settings: Annotated[SystemSettings, Depends(get_system_settings)],
):
    """Get system model."""
    return system_settings

```



---

## High-Level Overview

This is a **python** file named `system.py`.

**Python Module**

- **Functions** (1): get_system_model
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Decorators Used

router


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `APIRouter`
- `Annotated`
- `SystemSettings`
- `fastapi`
- `get_system_settings`
- `openbb_core.api.dependency.system`
- `openbb_core.app.model.system_settings`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.202575Z
**Generator**: World's Best Repo Book Generator v1.0
