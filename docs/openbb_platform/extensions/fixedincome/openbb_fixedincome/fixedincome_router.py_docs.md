# File Documentation: fixedincome_router.py

## Metadata
- **Path**: `openbb_platform/extensions/fixedincome/openbb_fixedincome/fixedincome_router.py`
- **Size**: 2,962 bytes
- **Lines**: 89
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `fixedincome_router.py`.

**Python Module**

- **Functions** (2): bond_indices, mortgage_indices
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
- `openbb_fixedincome.corporate.corporate_router`
- `openbb_fixedincome.government.government_router`
- `openbb_fixedincome.rate.rate_router`
- `openbb_fixedincome.spreads.spreads_router`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.031330Z
**Generator**: World's Best Repo Book Generator v1.0
