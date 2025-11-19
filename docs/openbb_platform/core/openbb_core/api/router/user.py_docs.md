# File Documentation: user.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/api/router/user.py`
- **Size**: 557 bytes
- **Lines**: 20
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OpenBB Platform API Account Router."""

from typing import Annotated

from fastapi import APIRouter, Depends
from openbb_core.api.auth.user import authenticate_user, get_user_settings
from openbb_core.app.model.user_settings import UserSettings

router = APIRouter(prefix="/user", tags=["User"])
auth_hook = authenticate_user
user_settings_hook = get_user_settings


@router.get("/me")
async def read_user_settings(
    user_settings: Annotated[UserSettings, Depends(get_user_settings)],
):
    """Read current user settings."""
    return user_settings

```



---

## High-Level Overview

This is a **python** file named `user.py`.

**Python Module**

- **Functions** (1): read_user_settings
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
- `UserSettings`
- `authenticate_user`
- `fastapi`
- `openbb_core.api.auth.user`
- `openbb_core.app.model.user_settings`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.203781Z
**Generator**: World's Best Repo Book Generator v1.0
