# File Documentation: price_router.py

## Metadata
- **Path**: `openbb_platform/extensions/index/openbb_index/price/price_router.py`
- **Size**: 999 bytes
- **Lines**: 37
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Price Router."""

from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router

router = Router(prefix="/price")

# pylint: disable=unused-argument


@router.command(
    model="IndexHistorical",
    examples=[
        APIEx(parameters={"symbol": "^GSPC", "provider": "fmp"}),
        APIEx(
            description="Not all providers have the same symbols.",
            parameters={"symbol": "SPX", "provider": "intrinio"},
        ),
    ],
)
async def historical(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Historical Index Levels."""
    return await OBBject.from_query(Query(**locals()))

```



---

## High-Level Overview

This is a **python** file named `price_router.py`.

**Python Module**

- **Functions** (1): historical
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure


#### Decorators Used

router


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `APIEx`
- `CommandContext`
- `OBBject`
- `Query`
- `Router`
- `openbb_core.app.model.command_context`
- `openbb_core.app.model.example`
- `openbb_core.app.model.obbject`
- `openbb_core.app.provider_interface`
- `openbb_core.app.query`
- `openbb_core.app.router`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.069464Z
**Generator**: World's Best Repo Book Generator v1.0
