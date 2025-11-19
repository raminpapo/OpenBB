# File Documentation: price_router.py

## Metadata
- **Path**: `openbb_platform/extensions/crypto/openbb_crypto/price/price_router.py`
- **Size**: 1,758 bytes
- **Lines**: 59
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
# pylint: disable=W0613:unused-argument
"""Crypto Price Router."""

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


# pylint: disable=unused-argument,line-too-long
@router.command(
    model="CryptoHistorical",
    examples=[
        APIEx(parameters={"symbol": "BTCUSD", "provider": "fmp"}),
        APIEx(
            parameters={
                "symbol": "BTCUSD",
                "start_date": "2024-01-01",
                "end_date": "2024-01-31",
                "provider": "fmp",
            },
        ),
        APIEx(
            parameters={
                "symbol": "BTCUSD,ETHUSD",
                "start_date": "2024-01-01",
                "end_date": "2024-01-31",
                "provider": "polygon",
            },
        ),
        APIEx(
            description="Get monthly historical prices from Yahoo Finance for Ethereum.",
            parameters={
                "symbol": "ETH-USD",
                "interval": "1m",
                "start_date": "2024-01-01",
                "end_date": "2024-12-31",
                "provider": "yfinance",
            },
        ),
    ],
)
async def historical(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical price data for cryptocurrency pair(s) within a provider."""
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

**Generated**: 2025-11-19T02:16:46.765141Z
**Generator**: World's Best Repo Book Generator v1.0
