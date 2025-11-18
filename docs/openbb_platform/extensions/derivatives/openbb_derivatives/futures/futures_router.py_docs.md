# Documentation: openbb_platform/extensions/derivatives/openbb_derivatives/futures/futures_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/derivatives/openbb_derivatives/futures/futures_router.py`
- **Size**: 2,829 characters, 98 lines
- **Words**: 208
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Futures Router."""

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

router = Router(prefix="/futures")


# pylint: disable=unused-argument
@router.command(
    model="FuturesHistorical",
    examples=[
        APIEx(parameters={"symbol": "ES", "provider": "yfinance"}),
        APIEx(
            description="Enter multiple symbols.",
            parameters={"symbol": "ES,NQ", "provider": "yfinance"},
        ),
        APIEx(
            description='Enter expiration dates as "YYYY-MM".',
            parameters={
                "symbol": "ES",
                "provider": "yfinance",
                "expiration": "2025-12",
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
    """Historical futures prices."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FuturesCurve",
    examples=[
        APIEx(parameters={"symbol": "VX", "provider": "cboe", "date": "2024-06-25"}),
        APIEx(
            parameters={"symbol": "NG", "provider": "yfinance"},
        ),
    ],
)
async def curve(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Futures Term Structure, current or historical."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FuturesInstruments",
    examples=[
        APIEx(parameters={"provider": "deribit"}),
    ],
)
async def instruments(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get reference data for available futures instruments by provider."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FuturesInfo",
    examples=[
        APIEx(parameters={"provider": "deribit", "symbol": "BTC"}),
        APIEx(parameters={"provider": "deribit", "symbol": "SOLUSDC"}),
        APIEx(parameters={"provider": "deribit", "symbol": "SOL_USDC-PERPETUAL"}),
        APIEx(parameters={"provider": "deribit", "symbol": "BTC,ETH"}),
    ],
)
async def info(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get current trading statistics by futures contract symbol."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

Futures Router.

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

router = Router(prefix="/futures")


# pylint: disable=unused-argument
@router.command(
model="FuturesHistorical",
examples=[

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (4):
`historical`, `curve`, `instruments`, `info`

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
- Generated: 2025-11-18T07:54:35.961599
- Generator: World's Best Repo Book Generator v1.0.0
