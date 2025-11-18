# Documentation: openbb_platform/core/openbb_core/api/router/user.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/api/router/user.py`
- **Size**: 557 characters, 20 lines
- **Words**: 47
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

OpenBB Platform API Account Router.

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
Read current user settings.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`read_user_settings`

**Imports** (8):
`typing`, `Annotated`, `fastapi`, `APIRouter`, `openbb_core.api.auth.user`, `authenticate_user`, `openbb_core.app.model.user_settings`, `UserSettings`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `fastapi`
- `openbb_core.api.auth.user`
- `openbb_core.app.model.user_settings`

## Notes
- Generated: 2025-11-18T07:54:35.409204
- Generator: World's Best Repo Book Generator v1.0.0
