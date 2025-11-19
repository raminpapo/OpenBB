# File Documentation: user.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/api/auth/user.py`
- **Size**: 1,926 bytes
- **Lines**: 57
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""User authentication."""

import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from openbb_core.app.model.user_settings import UserSettings
from openbb_core.app.service.user_service import UserService
from openbb_core.env import Env

security = HTTPBasic() if Env().API_AUTH else lambda: None


async def authenticate_user(
    credentials: Annotated[HTTPBasicCredentials | None, Depends(security)],
):
    """Authenticate the user."""
    if credentials:
        username = Env().API_USERNAME
        password = Env().API_PASSWORD

        is_correct_username = False
        is_correct_password = False

        if username is not None and password is not None:
            current_username_bytes = credentials.username.encode("utf8")
            correct_username_bytes = username.encode("utf8")
            is_correct_username = secrets.compare_digest(
                current_username_bytes, correct_username_bytes
            )
            current_password_bytes = credentials.password.encode("utf8")
            correct_password_bytes = password.encode("utf8")
            is_correct_password = secrets.compare_digest(
                current_password_bytes, correct_password_bytes
            )

        if not (is_correct_username and is_correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},
            )


async def get_user_service() -> UserService:
    """Get user service."""
    return UserService()


async def get_user_settings(
    _: Annotated[None, Depends(authenticate_user)],
    user_service: Annotated[UserService, Depends(get_user_service)],
) -> UserSettings:
    """Get user settings."""
    return user_service.read_from_file()

```



---

## High-Level Overview

This is a **python** file named `user.py`.

**Python Module**

- **Functions** (3): authenticate_user, get_user_service, get_user_settings
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Annotated`
- `Depends`
- `Env`
- `HTTPBasic`
- `UserService`
- `UserSettings`
- `fastapi`
- `fastapi.security`
- `openbb_core.app.model.user_settings`
- `openbb_core.app.service.user_service`
- `openbb_core.env`
- `secrets`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.191343Z
**Generator**: World's Best Repo Book Generator v1.0
