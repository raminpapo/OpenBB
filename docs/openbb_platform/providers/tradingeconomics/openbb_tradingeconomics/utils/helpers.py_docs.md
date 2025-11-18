# Documentation: openbb_platform/providers/tradingeconomics/openbb_tradingeconomics/utils/helpers.py

## File Metadata
- **Path**: `openbb_platform/providers/tradingeconomics/openbb_tradingeconomics/utils/helpers.py`
- **Size**: 741 characters, 25 lines
- **Words**: 65
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

TradingEconomics Helpers.

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.utils.errors import EmptyDataError, UnauthorizedError


async def response_callback(response, _) -> dict | list[dict]:
Return the response.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`response_callback`

**Imports** (4):
`openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.utils.errors`, `EmptyDataError`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`

## Notes
- Generated: 2025-11-18T07:54:43.481442
- Generator: World's Best Repo Book Generator v1.0.0
