# Documentation: openbb_platform/core/openbb_core/api/router/system.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/api/router/system.py`
- **Size**: 459 characters, 18 lines
- **Words**: 36
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

System router.

from typing import Annotated

from fastapi import APIRouter, Depends
from openbb_core.api.dependency.system import get_system_settings
from openbb_core.app.model.system_settings import SystemSettings

router = APIRouter(prefix="/system", tags=["System"])


@router.get("")
async def get_system_model(
system_settings: Annotated[SystemSettings, Depends(get_system_settings)],
):
Get system model.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`get_system_model`

**Imports** (8):
`typing`, `Annotated`, `fastapi`, `APIRouter`, `openbb_core.api.dependency.system`, `get_system_settings`, `openbb_core.app.model.system_settings`, `SystemSettings`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `fastapi`
- `openbb_core.api.dependency.system`
- `openbb_core.app.model.system_settings`

## Notes
- Generated: 2025-11-18T07:54:35.408080
- Generator: World's Best Repo Book Generator v1.0.0
