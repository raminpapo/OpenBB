# Documentation: openbb_platform/extensions/equity/openbb_equity/calendar/calendar_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/equity/openbb_equity/calendar/calendar_router.py`
- **Size**: 4,072 characters, 141 lines
- **Words**: 306
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Calendar Router."""

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

router = Router(prefix="/calendar")

# pylint: disable=unused-argument


@router.command(
    model="CalendarIpo",
    examples=[
        APIEx(parameters={"provider": "intrinio"}),
        APIEx(parameters={"limit": 100, "provider": "nasdaq"}),
        APIEx(
            description="Get all IPOs available.", parameters={"provider": "intrinio"}
        ),
        APIEx(
            description="Get IPOs for specific dates.",
            parameters={
                "start_date": "2024-02-01",
                "end_date": "2024-02-07",
                "provider": "nasdaq",
            },
        ),
    ],
)
async def ipo(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming initial public offerings (IPOs)."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CalendarDividend",
    examples=[
        APIEx(parameters={"provider": "fmp"}),
        APIEx(
            description="Get dividend calendar for specific dates.",
            parameters={
                "start_date": "2024-02-01",
                "end_date": "2024-02-07",
                "provider": "nasdaq",
            },
        ),
    ],
)
async def dividend(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming dividend payments. Includes dividend amount, ex-dividend and payment dates."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CalendarSplits",
    examples=[
        APIEx(parameters={"provider": "fmp"}),
        APIEx(
            description="Get stock splits calendar for specific dates.",
            parameters={
                "start_date": "2024-02-01",
                "end_date": "2024-02-07",
                "provider": "fmp",
            },
        ),
    ],
)
async def splits(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming stock split operations."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CalendarEvents",
    examples=[
        APIEx(parameters={"provider": "fmp"}),
        APIEx(
            description="Get company events calendar for specific dates.",
            parameters={
                "start_date": "2024-02-01",
                "end_date": "2024-02-07",
                "provider": "fmp",
            },
        ),
    ],
)
async def events(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming company events, such as Investor Day, Conference Call, Earnings Release."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CalendarEarnings",
    examples=[
        APIEx(parameters={"provider": "fmp"}),
        APIEx(
            description="Get earnings calendar for specific dates.",
            parameters={
                "start_date": "2024-02-01",
                "end_date": "2024-02-07",
                "provider": "fmp",
            },
        ),
    ],
)
async def earnings(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming company earnings releases. Includes earnings per share (EPS) and revenue data."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

Calendar Router.

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

router = Router(prefix="/calendar")

# pylint: disable=unused-argument


@router.command(
model="CalendarIpo",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (5):
`ipo`, `dividend`, `splits`, `events`, `earnings`

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
- Generated: 2025-11-18T07:54:36.067830
- Generator: World's Best Repo Book Generator v1.0.0
