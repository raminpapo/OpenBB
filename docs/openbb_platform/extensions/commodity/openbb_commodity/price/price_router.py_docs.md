# Documentation: openbb_platform/extensions/commodity/openbb_commodity/price/price_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/commodity/openbb_commodity/price/price_router.py`
- **Size**: 885 characters, 34 lines
- **Words**: 67
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Price Router."""

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


@router.command(
    model="CommoditySpotPrices",
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"provider": "fred", "commodity": "wti"}),
    ],
)
async def spot(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Commodity Spot Prices."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

Price Router.

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


@router.command(
model="CommoditySpotPrices",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`spot`

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
- Generated: 2025-11-18T07:54:35.902219
- Generator: World's Best Repo Book Generator v1.0.0
