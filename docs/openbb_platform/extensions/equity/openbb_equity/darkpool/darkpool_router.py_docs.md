# Documentation: openbb_platform/extensions/equity/openbb_equity/darkpool/darkpool_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/equity/openbb_equity/darkpool/darkpool_router.py`
- **Size**: 1,114 characters, 41 lines
- **Words**: 100
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Dark Pool Router."""

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

router = Router(prefix="/darkpool")

# pylint: disable=unused-argument


@router.command(
    model="OTCAggregate",
    examples=[
        APIEx(parameters={"provider": "finra"}),
        APIEx(
            description="Get OTC data for a symbol",
            parameters={"symbol": "AAPL", "provider": "finra"},
        ),
    ],
)
async def otc(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get the weekly aggregate trade data for Over The Counter deals.

    ATS and non-ATS trading data for each ATS/firm
    with trade reporting obligations under FINRA rules.
    """
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

Dark Pool Router.

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

router = Router(prefix="/darkpool")

# pylint: disable=unused-argument


@router.command(
model="OTCAggregate",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`otc`

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
- Generated: 2025-11-18T07:54:36.072229
- Generator: World's Best Repo Book Generator v1.0.0
