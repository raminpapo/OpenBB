# File Documentation: cftc_router.py

## Metadata
- **Path**: `openbb_platform/extensions/regulators/openbb_regulators/cftc/cftc_router.py`
- **Size**: 2,125 bytes
- **Lines**: 68
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `cftc_router.py`.

**Python Module**

- **Functions** (2): cot_search, cot
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

**Generated**: 2025-11-19T02:16:47.290894Z
**Generator**: World's Best Repo Book Generator v1.0
