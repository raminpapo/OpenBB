# Documentation: openbb_platform/extensions/equity/openbb_equity/estimates/estimates_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/equity/openbb_equity/estimates/estimates_router.py`
- **Size**: 5,128 characters, 192 lines
- **Words**: 363
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Estimates Router."""

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

router = Router(prefix="/estimates")

# pylint: disable=unused-argument


@router.command(
    model="PriceTarget",
    examples=[
        APIEx(parameters={"provider": "benzinga"}),
        APIEx(
            description="Get price targets for Microsoft using 'benzinga' as provider.",
            parameters={
                "start_date": "2020-01-01",
                "end_date": "2024-02-16",
                "limit": 10,
                "symbol": "msft",
                "provider": "benzinga",
                "action": "downgrades",
            },
        ),
    ],
)
async def price_target(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get analyst price targets by company."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="AnalystEstimates",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "fmp"}),
    ],
)
async def historical(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical analyst estimates for earnings and revenue."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="PriceTargetConsensus",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "fmp"}),
        APIEx(parameters={"symbol": "AAPL,MSFT", "provider": "yfinance"}),
    ],
)
async def consensus(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get consensus price target and recommendation."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="AnalystSearch",
    examples=[
        APIEx(parameters={"provider": "benzinga"}),
        APIEx(parameters={"firm_name": "Wedbush", "provider": "benzinga"}),
    ],
)
async def analyst_search(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Search for specific analysts and get their forecast track record."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="ForwardSalesEstimates",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "intrinio"}),
        APIEx(
            parameters={
                "fiscal_year": 2025,
                "fiscal_period": "fy",
                "provider": "intrinio",
            }
        ),
    ],
)
async def forward_sales(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get forward sales estimates."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="ForwardEbitdaEstimates",
    examples=[
        APIEx(parameters={"provider": "intrinio"}),
        APIEx(
            parameters={
                "symbol": "AAPL",
                "fiscal_period": "annual",
                "provider": "intrinio",
            }
        ),
        APIEx(
            parameters={
                "symbol": "AAPL,MSFT",
                "fiscal_period": "quarter",
                "provider": "fmp",
            }
        ),
    ],
)
async def forward_ebitda(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get forward EBITDA estimates."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="ForwardEpsEstimates",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "intrinio"}),
        APIEx(
            parameters={
                "fiscal_year": 2025,
                "fiscal_period": "fy",
                "provider": "intrinio",
            }
        ),
    ],
)
async def forward_eps(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get forward EPS estimates."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="ForwardPeEstimates",
    examples=[
        APIEx(parameters={"provider": "intrinio"}),
        APIEx(
            parameters={
                "symbol": "AAPL,MSFT,GOOG",
                "provider": "intrinio",
            }
        ),
    ],
)
async def forward_pe(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get forward PE estimates."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

Estimates Router.

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

router = Router(prefix="/estimates")

# pylint: disable=unused-argument


@router.command(
model="PriceTarget",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (8):
`price_target`, `historical`, `consensus`, `analyst_search`, `forward_sales`, `forward_ebitda`, `forward_eps`, `forward_pe`

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
- Generated: 2025-11-18T07:54:36.080595
- Generator: World's Best Repo Book Generator v1.0.0
