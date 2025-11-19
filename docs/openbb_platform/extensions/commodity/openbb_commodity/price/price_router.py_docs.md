# File Documentation: price_router.py

## Metadata
- **Path**: `openbb_platform/extensions/commodity/openbb_commodity/price/price_router.py`
- **Size**: 885 bytes
- **Lines**: 34
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Price Router."""

# pylint: disable=unused-argument

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


@router.command(
    model="CommoditySpotPrices",
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"provider": "fred", "commodity": "wti"}),
    ],
)
async def spot(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Commodity Spot Prices."""
    return await OBBject.from_query(Query(**locals()))

```



---

## High-Level Overview

This is a **python** file named `price_router.py`.

**Python Module**

- **Functions** (1): spot
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

**Generated**: 2025-11-19T02:16:46.743914Z
**Generator**: World's Best Repo Book Generator v1.0
