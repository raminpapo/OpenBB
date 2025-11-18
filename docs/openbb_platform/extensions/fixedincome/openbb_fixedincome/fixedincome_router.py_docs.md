# Documentation: openbb_platform/extensions/fixedincome/openbb_fixedincome/fixedincome_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/fixedincome/openbb_fixedincome/fixedincome_router.py`
- **Size**: 2,962 characters, 89 lines
- **Words**: 223
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Fixed Income Router."""

# pylint: disable=W0613:unused-argument

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

from openbb_fixedincome.corporate.corporate_router import router as corporate_router
from openbb_fixedincome.government.government_router import router as government_router
from openbb_fixedincome.rate.rate_router import router as rate_router
from openbb_fixedincome.spreads.spreads_router import router as spreads_router

router = Router(prefix="", description="Fixed Income market data.")
router.include_router(rate_router)
router.include_router(spreads_router)
router.include_router(government_router)
router.include_router(corporate_router)


@router.command(
    model="BondIndices",
    examples=[
        APIEx(
            description="The default state for FRED are series for constructing the US Corporate Bond Yield Curve.",
            parameters={"provider": "fred"},
        ),
        APIEx(
            description="Multiple indices, from within the same 'category', can be requested.",
            parameters={
                "category": "high_yield",
                "index": "us,europe,emerging",
                "index_type": "total_return",
                "provider": "fred",
            },
        ),
        APIEx(
            description="From FRED, there are three main categories, 'high_yield', 'us', and 'emerging_markets'."
            + " Emerging markets is a broad category.",
            parameters={
                "category": "emerging_markets",
                "index": "corporate,private_sector,public_sector",
                "provider": "fred",
            },
        ),
    ],
)
async def bond_indices(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:  # type: ignore
    """Bond Indices."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="MortgageIndices",
    examples=[
        APIEx(
            description="The default state for FRED are the primary mortgage indices from Optimal Blue.",
            parameters={"provider": "fred"},
        ),
        APIEx(
            description="Multiple indices can be requested.",
            parameters={
                "index": "jumbo_30y,conforming_30y,conforming_15y",
                "provider": "fred",
            },
        ),
    ],
)
async def mortgage_indices(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:  # type: ignore
    """Mortgage Indices."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

Fixed Income Router.

# pylint: disable=W0613:unused-argument

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

from openbb_fixedincome.corporate.corporate_router import router as corporate_router
from openbb_fixedincome.government.government_router import router as government_router
from openbb_fixedincome.rate.rate_router import router as rate_router
from openbb_fixedincome.spreads.spreads_router import router as spreads_router


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`bond_indices`, `mortgage_indices`

**Imports** (21):
`openbb_core.app.model.command_context`, `CommandContext`, `openbb_core.app.model.example`, `APIEx`, `openbb_core.app.model.obbject`, `OBBject`, `openbb_core.app.provider_interface`, `openbb_core.app.query`, `Query`, `openbb_core.app.router`, `Router`, `openbb_fixedincome.corporate.corporate_router`, `router`, `openbb_fixedincome.government.government_router`, `router`, `openbb_fixedincome.rate.rate_router`, `router`, `openbb_fixedincome.spreads.spreads_router`, `router`, `within`


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
- `openbb_fixedincome.corporate.corporate_router`
- `openbb_fixedincome.government.government_router`
- `openbb_fixedincome.rate.rate_router`
- `openbb_fixedincome.spreads.spreads_router`

## Notes
- Generated: 2025-11-18T07:54:36.136981
- Generator: World's Best Repo Book Generator v1.0.0
