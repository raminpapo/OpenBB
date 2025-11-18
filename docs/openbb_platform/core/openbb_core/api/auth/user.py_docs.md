# Documentation: openbb_platform/core/openbb_core/api/auth/user.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/api/auth/user.py`
- **Size**: 1,926 characters, 57 lines
- **Words**: 141
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

User authentication.

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
Authenticate the user.
Get user service.
return UserService()

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`authenticate_user`, `get_user_service`, `get_user_settings`

**Imports** (13):
`secrets`, `typing`, `Annotated`, `fastapi`, `Depends`, `fastapi.security`, `HTTPBasic`, `openbb_core.app.model.user_settings`, `UserSettings`, `openbb_core.app.service.user_service`, `UserService`, `openbb_core.env`, `Env`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `secrets`
- `typing`
- `fastapi`
- `fastapi.security`
- `openbb_core.app.model.user_settings`
- `openbb_core.app.service.user_service`
- `openbb_core.env`

## Notes
- Generated: 2025-11-18T07:54:35.392809
- Generator: World's Best Repo Book Generator v1.0.0
