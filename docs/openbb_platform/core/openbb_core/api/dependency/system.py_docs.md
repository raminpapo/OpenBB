# Documentation: openbb_platform/core/openbb_core/api/dependency/system.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/api/dependency/system.py`
- **Size**: 643 characters, 22 lines
- **Words**: 49
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

System dependency.

from typing import Annotated

from fastapi import Depends
from openbb_core.app.model.system_settings import SystemSettings
from openbb_core.app.service.auth_service import AuthService
from openbb_core.app.service.system_service import SystemService


async def get_system_service() -> SystemService:
Get system service.
Get system settings.
return system_service.system_settings


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`get_system_service`, `get_system_settings`

**Imports** (10):
`typing`, `Annotated`, `fastapi`, `Depends`, `openbb_core.app.model.system_settings`, `SystemSettings`, `openbb_core.app.service.auth_service`, `AuthService`, `openbb_core.app.service.system_service`, `SystemService`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `fastapi`
- `openbb_core.app.model.system_settings`
- `openbb_core.app.service.auth_service`
- `openbb_core.app.service.system_service`

## Notes
- Generated: 2025-11-18T07:54:35.396614
- Generator: World's Best Repo Book Generator v1.0.0
