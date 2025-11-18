# Documentation: openbb_platform/extensions/news/openbb_news/news_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/news/openbb_news/news_router.py`
- **Size**: 3,213 characters, 103 lines
- **Words**: 236
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
# pylint: disable=import-outside-toplevel, W0613:unused-argument
"""News Router."""

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

router = Router(prefix="", description="Financial market news data.")


@router.command(
    model="WorldNews",
    examples=[
        APIEx(parameters={"provider": "fmp"}),
        APIEx(parameters={"limit": 100, "provider": "intrinio"}),
        APIEx(
            description="Get news on the specified dates.",
            parameters={
                "start_date": "2024-02-01",
                "end_date": "2024-02-07",
                "provider": "intrinio",
            },
        ),
        APIEx(
            description="Display the headlines of the news.",
            parameters={"display": "headline", "provider": "benzinga"},
        ),
        APIEx(
            description="Get news by topics.",
            parameters={"topics": "finance", "provider": "benzinga"},
        ),
        APIEx(
            description="Get news by source using 'tingo' as provider.",
            parameters={"provider": "tiingo", "source": "bloomberg"},
        ),
        APIEx(
            description="Filter aticles by term using 'biztoc' as provider.",
            parameters={"provider": "biztoc", "term": "apple"},
        ),
    ],
)
async def world(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """World News. Global news data."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CompanyNews",
    examples=[
        APIEx(parameters={"provider": "benzinga"}),
        APIEx(parameters={"limit": 100, "provider": "benzinga"}),
        APIEx(
            description="Get news on the specified dates.",
            parameters={
                "symbol": "AAPL",
                "start_date": "2024-02-01",
                "end_date": "2024-02-07",
                "provider": "intrinio",
            },
        ),
        APIEx(
            description="Display the headlines of the news.",
            parameters={
                "symbol": "AAPL",
                "display": "headline",
                "provider": "benzinga",
            },
        ),
        APIEx(
            description="Get news for multiple symbols.",
            parameters={"symbol": "aapl,tsla", "provider": "fmp"},
        ),
        APIEx(
            description="Get news company's ISIN.",
            parameters={
                "symbol": "NVDA",
                "isin": "US0378331005",
                "provider": "benzinga",
            },
        ),
    ],
)
async def company(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Company News. Get news for one or more companies."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

pylint: disable=import-outside-toplevel, W0613:unused-argument
News Router.

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

router = Router(prefix="", description="Financial market news data.")


@router.command(
model="WorldNews",
examples=[

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`world`, `company`

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
- Generated: 2025-11-18T07:54:36.243158
- Generator: World's Best Repo Book Generator v1.0.0
