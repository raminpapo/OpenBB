# Documentation: openbb_platform/core/openbb_core/api/dependency/coverage.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/api/dependency/coverage.py`
- **Size**: 596 characters, 23 lines
- **Words**: 50
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Coverage dependency."""

from typing import Annotated

from fastapi import Depends
from openbb_core.app.provider_interface import ProviderInterface
from openbb_core.app.router import CommandMap
from openbb_core.app.service.auth_service import AuthService


async def get_command_map(
    _: Annotated[None, Depends(AuthService().auth_hook)],
) -> CommandMap:
    """Get command map."""
    return CommandMap()


async def get_provider_interface(
    _: Annotated[None, Depends(AuthService().auth_hook)],
) -> ProviderInterface:
    """Get provider interface."""
    return ProviderInterface()

```

## High-Level Overview

Coverage dependency.

from typing import Annotated

from fastapi import Depends
from openbb_core.app.provider_interface import ProviderInterface
from openbb_core.app.router import CommandMap
from openbb_core.app.service.auth_service import AuthService


async def get_command_map(
_: Annotated[None, Depends(AuthService().auth_hook)],
) -> CommandMap:
Get command map.
Get provider interface.
return ProviderInterface()


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`get_command_map`, `get_provider_interface`

**Imports** (10):
`typing`, `Annotated`, `fastapi`, `Depends`, `openbb_core.app.provider_interface`, `ProviderInterface`, `openbb_core.app.router`, `CommandMap`, `openbb_core.app.service.auth_service`, `AuthService`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `fastapi`
- `openbb_core.app.provider_interface`
- `openbb_core.app.router`
- `openbb_core.app.service.auth_service`

## Notes
- Generated: 2025-11-18T07:54:35.395423
- Generator: World's Best Repo Book Generator v1.0.0
