# File Documentation: helpers.py

## Metadata
- **Path**: `openbb_platform/providers/polygon/openbb_polygon/utils/helpers.py`
- **Size**: 2,815 bytes
- **Lines**: 101
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Polygon Helpers Module."""

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.utils.errors import EmptyDataError, UnauthorizedError
from openbb_core.provider.utils.helpers import (
    ClientResponse,
    ClientSession,
    amake_request,
)


async def response_callback(response: ClientResponse, _: ClientSession) -> dict | list:
    """Use callback for make_request."""
    data = await response.json()  # type: ignore

    if response.status != 200:
        message = data.get("error") or data.get("message")
        raise OpenBBError(f"Error in Polygon request -> {message}")

    if isinstance(data, dict) and data.get("status") == "NOT_AUTHORIZED":
        raise UnauthorizedError(response.get("message", str(response)))

    if not data:
        raise EmptyDataError("No data was returned from the Polygon endpoint")

    return data


async def get_data(url: str, **kwargs: Any) -> list | dict:
    """Get data from Polygon endpoint."""
    return await amake_request(url, response_callback=response_callback, **kwargs)


async def get_data_many(
    url: str, sub_dict: str | None = None, **kwargs: Any
) -> list[dict]:
    """Get data from Polygon endpoint and convert to list of schemas.

    Parameters
    ----------
    url: str
        The URL to get the data from.
    sub_dict: Optional[str]
        The sub-dictionary to use.

    Returns
    -------
    List[dict]
        Dictionary of data.
    """
    data = await get_data(url, **kwargs)
    if sub_dict and isinstance(data, dict):
        data = data.get(sub_dict, [])
    if isinstance(data, dict):
        raise ValueError("Expected list of dicts, got dict")
    return data


async def get_data_one(url: str, **kwargs: Any) -> dict:
    """Get data from Polygon endpoint and convert to schema."""
    data = await get_data(url, **kwargs)
    if isinstance(data, list):
        if len(data) == 0:
            raise ValueError("Expected dict, got empty list")

        try:
            data = {i: data[i] for i in range(len(data))} if len(data) > 1 else data[0]
        except TypeError as e:
            raise ValueError("Expected dict, got list of dicts") from e

    return data


def get_date_condition(date: str) -> tuple:
    """Get the date condition for the querystring."""
    date_conditions = {
        "<": "lt",
        "<=": "lte",
        ">": "gt",
        ">=": "gte",
    }

    for key, value in date_conditions.items():
        if key in date:
            return date.split(key)[1], value

    return date, "eq"


def map_tape(tape: int) -> str:
    """Map the tape to a string."""
    STOCK_TAPE_MAP = {
        1: "Tape A: NYSE",
        2: "Tape B: NYSE ARCA",
        3: "Tape C: NASDAQ",
    }

    return STOCK_TAPE_MAP.get(tape, "") if tape else ""

```



---

## High-Level Overview

This is a **python** file named `helpers.py`.

**Python Module**

- **Functions** (6): response_callback, get_data, get_data_many, get_data_one, get_date_condition, map_tape
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `EmptyDataError`
- `OpenBBError`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.886553Z
**Generator**: World's Best Repo Book Generator v1.0
