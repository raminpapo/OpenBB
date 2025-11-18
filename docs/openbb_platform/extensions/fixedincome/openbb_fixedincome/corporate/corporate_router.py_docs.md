# Documentation: openbb_platform/extensions/fixedincome/openbb_fixedincome/corporate/corporate_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/fixedincome/openbb_fixedincome/corporate/corporate_router.py`
- **Size**: 3,138 characters, 97 lines
- **Words**: 311
- **Extension**: .py
- **Classification**: Text file

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

router = Router(prefix="/corporate")

# pylint: disable=unused-argument


@router.command(
    model="HighQualityMarketCorporateBond",
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"yield_curve": "par", "provider": "fred"}),
    ],
)
async def hqm(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """High Quality Market Corporate Bond.

    The HQM yield curve represents the high quality corporate bond market, i.e.,
    corporate bonds rated AAA, AA, or A.  The HQM curve contains two regression terms.
    These terms are adjustment factors that blend AAA, AA, and A bonds into a single HQM yield curve
    that is the market-weighted average (MWA) quality of high quality bonds.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="SpotRate",
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"maturity": "10,20,30,50", "provider": "fred"}),
    ],
)
async def spot_rates(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Spot Rates.

    The spot rates for any maturity is the yield on a bond that provides a single payment at that maturity.
    This is a zero coupon bond.
    Because each spot rate pertains to a single cashflow, it is the relevant interest rate
    concept for discounting a pension liability at the same maturity.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CommercialPaper",
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"category": "all", "maturity": "15d", "provider": "fred"}),
    ],
)
async def commercial_paper(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Commercial Paper.

    Commercial paper (CP) consists of short-term, promissory notes issued primarily by corporations.
    Maturities range up to 270 days but average about 30 days.
    Many companies use CP to raise cash needed for current transactions,
    and many find it to be a lower-cost alternative to bank loans.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(model="BondPrices", examples=[APIEx(parameters={"provider": "tmx"})])
async def bond_prices(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Corporate Bond Prices."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

Fixed Income Corporate Router.

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

router = Router(prefix="/corporate")

# pylint: disable=unused-argument


@router.command(
model="HighQualityMarketCorporateBond",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (4):
`hqm`, `spot_rates`, `commercial_paper`, `bond_prices`

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
- Generated: 2025-11-18T07:54:36.135258
- Generator: World's Best Repo Book Generator v1.0.0
