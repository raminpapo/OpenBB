# Documentation: openbb_platform/extensions/commodity/openbb_commodity/commodity_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/commodity/openbb_commodity/commodity_router.py`
- **Size**: 2,274 characters, 81 lines
- **Words**: 186
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""The Commodity router."""

# pylint: disable=unused-argument,unused-import
# flake8: noqa: F401

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

from openbb_commodity.price.price_router import router as price_router

router = Router(prefix="", description="Commodity market data.")


router.include_router(price_router)


@router.command(
    model="PetroleumStatusReport",
    examples=[
        APIEx(
            description="Get the EIA's Weekly Petroleum Status Report.",
            parameters={"provider": "eia"},
        ),
        APIEx(
            description="Select the category of data, and filter for a specific table within the report.",
            parameters={
                "category": "weekly_estimates",
                "table": "imports",
                "provider": "eia",
            },
        ),
    ],
)
async def petroleum_status_report(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """EIA Weekly Petroleum Status Report."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="ShortTermEnergyOutlook",
    examples=[
        APIEx(
            description="Get the EIA's Short Term Energy Outlook.",
            parameters={"provider": "eia"},
        ),
        APIEx(
            description="Select the specific table of data from the STEO. Table 03d is World Crude Oil Production.",
            parameters={
                "table": "03d",
                "provider": "eia",
            },
        ),
    ],
)
async def short_term_energy_outlook(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Monthly short term (18 month) projections using EIA's STEO model.

    Source: www.eia.gov/steo/
    """
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

The Commodity router.

# pylint: disable=unused-argument,unused-import
# flake8: noqa: F401

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

from openbb_commodity.price.price_router import router as price_router


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`petroleum_status_report`, `short_term_energy_outlook`

**Imports** (14):
`openbb_core.app.model.command_context`, `CommandContext`, `openbb_core.app.model.example`, `APIEx`, `openbb_core.app.model.obbject`, `OBBject`, `openbb_core.app.provider_interface`, `openbb_core.app.query`, `Query`, `openbb_core.app.router`, `Router`, `openbb_commodity.price.price_router`, `router`, `the`


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
- `openbb_commodity.price.price_router`

## Notes
- Generated: 2025-11-18T07:54:35.900013
- Generator: World's Best Repo Book Generator v1.0.0
