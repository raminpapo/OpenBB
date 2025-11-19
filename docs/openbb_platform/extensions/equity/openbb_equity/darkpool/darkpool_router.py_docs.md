# File Documentation: darkpool_router.py

## Metadata
- **Path**: `openbb_platform/extensions/equity/openbb_equity/darkpool/darkpool_router.py`
- **Size**: 1,114 bytes
- **Lines**: 41
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `darkpool_router.py`.

**Python Module**

- **Functions** (1): otc
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

**Generated**: 2025-11-19T02:16:46.960964Z
**Generator**: World's Best Repo Book Generator v1.0
