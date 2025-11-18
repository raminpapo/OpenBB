# Documentation: openbb_platform/extensions/economy/openbb_economy/gdp/gdp_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/economy/openbb_economy/gdp/gdp_router.py`
- **Size**: 2,099 characters, 84 lines
- **Words**: 151
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Economy GDP Router."""

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

router = Router(prefix="/gdp")

# pylint: disable=unused-argument


@router.command(
    model="GdpForecast",
    examples=[
        APIEx(parameters={"provider": "oecd"}),
        APIEx(
            parameters={
                "country": "united_states,germany,france",
                "frequency": "annual",
                "units": "capita",
                "provider": "oecd",
            }
        ),
    ],
)
async def forecast(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get Forecasted GDP Data."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="GdpNominal",
    examples=[
        APIEx(parameters={"provider": "oecd"}),
        APIEx(
            parameters={
                "units": "capita",
                "country": "all",
                "frequency": "annual",
                "provider": "oecd",
            }
        ),
    ],
)
async def nominal(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get Nominal GDP Data."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="GdpReal",
    examples=[
        APIEx(parameters={"provider": "oecd"}),
        APIEx(
            parameters={"country": "united_states,germany,japan", "provider": "econdb"}
        ),
    ],
)
async def real(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get Real GDP Data."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

Economy GDP Router.

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

router = Router(prefix="/gdp")

# pylint: disable=unused-argument


@router.command(
model="GdpForecast",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`forecast`, `nominal`, `real`

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
- Generated: 2025-11-18T07:54:36.039998
- Generator: World's Best Repo Book Generator v1.0.0
