# File Documentation: system.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/api/dependency/system.py`
- **Size**: 643 bytes
- **Lines**: 22
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""System dependency."""

from typing import Annotated

from fastapi import Depends
from openbb_core.app.model.system_settings import SystemSettings
from openbb_core.app.service.auth_service import AuthService
from openbb_core.app.service.system_service import SystemService


async def get_system_service() -> SystemService:
    """Get system service."""
    return SystemService()


async def get_system_settings(
    _: Annotated[None, Depends(AuthService().auth_hook)],
    system_service: Annotated[SystemService, Depends(get_system_service)],
) -> SystemSettings:
    """Get system settings."""
    return system_service.system_settings

```



---

## High-Level Overview

This is a **python** file named `system.py`.

**Python Module**

- **Functions** (2): get_system_service, get_system_settings
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Annotated`
- `AuthService`
- `Depends`
- `SystemService`
- `SystemSettings`
- `fastapi`
- `openbb_core.app.model.system_settings`
- `openbb_core.app.service.auth_service`
- `openbb_core.app.service.system_service`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.195483Z
**Generator**: World's Best Repo Book Generator v1.0
