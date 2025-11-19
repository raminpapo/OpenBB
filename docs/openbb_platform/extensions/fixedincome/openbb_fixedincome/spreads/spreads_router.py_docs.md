# File Documentation: spreads_router.py

## Metadata
- **Path**: `openbb_platform/extensions/fixedincome/openbb_fixedincome/spreads/spreads_router.py`
- **Size**: 3,076 bytes
- **Lines**: 87
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Fixed Income Corporate Router."""

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

router = Router(prefix="/spreads")

# pylint: disable=unused-argument


@router.command(
    model="TreasuryConstantMaturity",
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"maturity": "2y", "provider": "fred"}),
    ],
)
async def tcm(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Treasury Constant Maturity.

    Get data for 10-Year Treasury Constant Maturity Minus Selected Treasury Constant Maturity.
    Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of auctioned U.S.
    Treasuries. The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury
    yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="SelectedTreasuryConstantMaturity",
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"maturity": "10y", "provider": "fred"}),
    ],
)
async def tcm_effr(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Select Treasury Constant Maturity.

    Get data for Selected Treasury Constant Maturity Minus Federal Funds Rate
    Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of auctioned U.S.
    Treasuries. The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury
    yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="SelectedTreasuryBill",
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"maturity": "6m", "provider": "fred"}),
    ],
)
async def treasury_effr(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Select Treasury Bill.

    Get Selected Treasury Bill Minus Federal Funds Rate.
    Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of
    auctioned U.S. Treasuries.
    The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury
    yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.
    """
    return await OBBject.from_query(Query(**locals()))

```



---

## High-Level Overview

This is a **python** file named `spreads_router.py`.

**Python Module**

- **Functions** (3): tcm, tcm_effr, treasury_effr
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

**Generated**: 2025-11-19T02:16:47.047203Z
**Generator**: World's Best Repo Book Generator v1.0
