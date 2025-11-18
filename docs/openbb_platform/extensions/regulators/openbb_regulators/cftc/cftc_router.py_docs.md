# Documentation: openbb_platform/extensions/regulators/openbb_regulators/cftc/cftc_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/regulators/openbb_regulators/cftc/cftc_router.py`
- **Size**: 2,125 characters, 68 lines
- **Words**: 181
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
# pylint: disable=W0613:unused-argument
"""Commodity Futures Trading Commission (CFTC) Router."""

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

router = Router(prefix="/cftc")


@router.command(
    model="COTSearch",
    examples=[
        APIEx(parameters={"provider": "cftc"}),
        APIEx(parameters={"query": "gold", "provider": "cftc"}),
    ],
)
async def cot_search(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get the current Commitment of Traders Reports.

    Search a list of the current Commitment of Traders Reports series information.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="COT",
    examples=[
        APIEx(parameters={"provider": "ctfc"}),
        APIEx(
            description="Get the latest report for all items classified as, GOLD.",
            parameters={"id": "gold", "provider": "cftc"},
        ),
        APIEx(
            description="Enter the entire history for a single CFTC Market Contract Code.",
            parameters={"id": "088691", "provider": "cftc"},
        ),
        APIEx(
            description="Get the report for futures only.",
            parameters={"id": "088691", "futures_only": True, "provider": "cftc"},
        ),
        APIEx(
            description="Get the most recent Commodity Index Traders Supplemental Report.",
            parameters={"id": "all", "report_type": "supplemental", "provider": "cftc"},
        ),
    ],
)
async def cot(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get Commitment of Traders Reports."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

pylint: disable=W0613:unused-argument
Commodity Futures Trading Commission (CFTC) Router.

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

router = Router(prefix="/cftc")


@router.command(
model="COTSearch",
examples=[

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`cot_search`, `cot`

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
- Generated: 2025-11-18T07:54:36.343015
- Generator: World's Best Repo Book Generator v1.0.0
