# File Documentation: coverage.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/api/dependency/coverage.py`
- **Size**: 596 bytes
- **Lines**: 23
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `coverage.py`.

**Python Module**

- **Functions** (2): get_command_map, get_provider_interface
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
- `CommandMap`
- `Depends`
- `ProviderInterface`
- `fastapi`
- `openbb_core.app.provider_interface`
- `openbb_core.app.router`
- `openbb_core.app.service.auth_service`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.194081Z
**Generator**: World's Best Repo Book Generator v1.0
