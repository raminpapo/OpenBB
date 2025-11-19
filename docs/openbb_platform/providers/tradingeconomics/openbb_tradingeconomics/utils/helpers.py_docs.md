# File Documentation: helpers.py

## Metadata
- **Path**: `openbb_platform/providers/tradingeconomics/openbb_tradingeconomics/utils/helpers.py`
- **Size**: 741 bytes
- **Lines**: 25
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""TradingEconomics Helpers."""

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.utils.errors import EmptyDataError, UnauthorizedError


async def response_callback(response, _) -> dict | list[dict]:
    """Return the response."""
    if response.status != 200:
        message = await response.text()

        if "credentials" in message or "unauthorized" in message.lower():
            raise UnauthorizedError(
                f"Unauthorized TradingEconomics request -> {message}"
            )

        raise OpenBBError(f"{response.status} -> {message}")

    results = await response.json()

    if not results:
        raise EmptyDataError("The request was returned empty.")

    return results

```



---

## High-Level Overview

This is a **python** file named `helpers.py`.

**Python Module**

- **Functions** (1): response_callback
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `EmptyDataError`
- `OpenBBError`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.066925Z
**Generator**: World's Best Repo Book Generator v1.0
