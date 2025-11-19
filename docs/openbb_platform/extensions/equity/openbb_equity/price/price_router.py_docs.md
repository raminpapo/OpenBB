# File Documentation: price_router.py

## Metadata
- **Path**: `openbb_platform/extensions/equity/openbb_equity/price/price_router.py`
- **Size**: 2,288 bytes
- **Lines**: 76
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
    model="EquityQuote",
    examples=[APIEx(parameters={"symbol": "AAPL", "provider": "fmp"})],
)
async def quote(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get the latest quote for a given stock. Quote includes price, volume, and other data."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="EquityNBBO",
    examples=[APIEx(parameters={"symbol": "AAPL", "provider": "polygon"})],
)
async def nbbo(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get the National Best Bid and Offer for a given stock."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="EquityHistorical",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "fmp"}),
        APIEx(parameters={"symbol": "AAPL", "interval": "1d", "provider": "intrinio"}),
    ],
)
async def historical(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical price data for a given stock. This includes open, high, low, close, and volume."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="PricePerformance",
    examples=[APIEx(parameters={"symbol": "AAPL", "provider": "fmp"})],
)
async def performance(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get price performance data for a given stock. This includes price changes for different time periods."""
    return await OBBject.from_query(Query(**locals()))

```



---

## High-Level Overview

This is a **python** file named `price_router.py`.

**Python Module**

- **Functions** (4): quote, nbbo, historical, performance
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

**Generated**: 2025-11-19T02:16:46.976333Z
**Generator**: World's Best Repo Book Generator v1.0
