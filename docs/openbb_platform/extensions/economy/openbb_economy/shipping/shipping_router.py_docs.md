# Documentation: openbb_platform/extensions/economy/openbb_economy/shipping/shipping_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/economy/openbb_economy/shipping/shipping_router.py`
- **Size**: 3,157 characters, 106 lines
- **Words**: 267
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Economy shipping router."""

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

router = Router(prefix="/shipping")

# pylint: disable=unused-argument


@router.command(
    model="PortInfo",
    examples=[
        APIEx(parameters={"provider": "imf"}),
        APIEx(parameters={"provider": "imf", "continent": "asia_pacific"}),
    ],
)
async def port_info(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get general metadata and statistics for all ports from a given provider."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="PortVolume",
    examples=[
        APIEx(
            description="Get average dwelling times and TEU volumes from the top ports.",
            parameters={"provider": "econdb"},
        ),
        APIEx(
            description="Get daily port calls and estimated trading volumes for specific ports"
            + " Get the list of available ports with `openbb shipping port_info`",
            parameters={
                "provider": "imf",
                "port_code": "rotterdam,singapore",
            },
        ),
        APIEx(
            description="Get data for all ports in a specific country. Use the 3-letter ISO country code.",
            parameters={
                "provider": "imf",
                "country": "GBR",
            },
        ),
    ],
)
async def port_volume(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Daily port calls and estimates of trading volumes for ports around the world."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="MaritimeChokePointInfo",
    examples=[
        APIEx(parameters={"provider": "imf"}),
    ],
)
async def chokepoint_info(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get general metadata and statistics for all maritime chokepoint locations from a given provider."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="MaritimeChokePointVolume",
    examples=[
        APIEx(parameters={"provider": "imf"}),
        APIEx(
            parameters={
                "provider": "imf",
                "chokepoint": "suez_canal,panama_canal",
            }
        ),
    ],
)
async def chokepoint_volume(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Daily transit calls and estimates of transit trade volumes for shipping lane chokepoints around the world."""
    return await OBBject.from_query(Query(**locals()))

```

## High-Level Overview

Economy shipping router.

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

router = Router(prefix="/shipping")

# pylint: disable=unused-argument


@router.command(
model="PortInfo",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (4):
`port_info`, `port_volume`, `chokepoint_info`, `chokepoint_volume`

**Imports** (14):
`openbb_core.app.model.command_context`, `CommandContext`, `openbb_core.app.model.example`, `APIEx`, `openbb_core.app.model.obbject`, `OBBject`, `openbb_core.app.provider_interface`, `openbb_core.app.query`, `Query`, `openbb_core.app.router`, `Router`, `a`, `the`, `a`


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
- Generated: 2025-11-18T07:54:36.042218
- Generator: World's Best Repo Book Generator v1.0.0
