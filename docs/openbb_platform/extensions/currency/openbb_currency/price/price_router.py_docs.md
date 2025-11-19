# File Documentation: price_router.py

## Metadata
- **Path**: `openbb_platform/extensions/currency/openbb_currency/price/price_router.py`
- **Size**: 1,786 bytes
- **Lines**: 54
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Price router for Currency."""

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


# pylint: disable=unused-argument
@router.command(
    model="CurrencyHistorical",
    examples=[
        APIEx(parameters={"symbol": "EURUSD", "provider": "fmp"}),
        APIEx(
            description="Filter historical data with specific start and end date.",
            parameters={
                "symbol": "EURUSD",
                "start_date": "2023-01-01",
                "end_date": "2023-12-31",
                "provider": "fmp",
            },
        ),
        APIEx(
            description="Get data with different granularity.",
            parameters={"symbol": "EURUSD", "provider": "polygon", "interval": "15m"},
        ),
    ],
)
async def historical(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """
    Currency Historical Price. Currency historical data.

    Currency historical prices refer to the past exchange rates of one currency against
    another over a specific period.
    This data provides insight into the fluctuations and trends in the foreign exchange market,
    helping analysts, traders, and economists understand currency performance,
    evaluate economic health, and make predictions about future movements.
    """
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

**Generated**: 2025-11-19T02:16:46.790537Z
**Generator**: World's Best Repo Book Generator v1.0
