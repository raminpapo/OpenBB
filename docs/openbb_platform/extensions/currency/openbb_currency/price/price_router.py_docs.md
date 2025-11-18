# Documentation: openbb_platform/extensions/currency/openbb_currency/price/price_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/currency/openbb_currency/price/price_router.py`
- **Size**: 1,786 characters, 54 lines
- **Words**: 158
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Price router for Currency.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`historical`

**Imports** (11):
`openbb_core.app.model.command_context`, `CommandContext`, `openbb_core.app.model.example`, `APIEx`, `openbb_core.app.model.obbject`, `OBBject`, `openbb_core.app.provider_interface`, `openbb_core.app.query`, `Query`, `openbb_core.app.router`, `Router`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.command_context`
- `openbb_core.app.model.example`
- `openbb_core.app.model.obbject`
- `openbb_core.app.provider_interface`
- `openbb_core.app.query`
- `openbb_core.app.router`

## Notes
- Generated: 2025-11-18T07:54:35.940714
- Generator: World's Best Repo Book Generator v1.0.0
