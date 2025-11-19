# File Documentation: gdp_router.py

## Metadata
- **Path**: `openbb_platform/extensions/economy/openbb_economy/gdp/gdp_router.py`
- **Size**: 2,099 bytes
- **Lines**: 84
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `gdp_router.py`.

**Python Module**

- **Functions** (3): forecast, nominal, real
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

**Generated**: 2025-11-19T02:16:46.915511Z
**Generator**: World's Best Repo Book Generator v1.0
