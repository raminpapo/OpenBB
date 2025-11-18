# Documentation: openbb_platform/providers/benzinga/openbb_benzinga/utils/helpers.py

## File Metadata
- **Path**: `openbb_platform/providers/benzinga/openbb_benzinga/utils/helpers.py`
- **Size**: 639 characters, 22 lines
- **Words**: 52
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Benzinga Helpers."""

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.utils.errors import UnauthorizedError


async def response_callback(response, _):
    """Response callback."""
    # pylint: disable=import-outside-toplevel
    results = await response.json()
    if (
        results
        and isinstance(results, list)
        and len(results) == 1
        and isinstance(results[0], str)
    ):
        if "access denied" in results[0].lower():
            raise UnauthorizedError(f"Unauthorized Benzinga request -> {results[0]}")
        raise OpenBBError(results[0])

    return results

```

## High-Level Overview

Benzinga Helpers.

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.utils.errors import UnauthorizedError


async def response_callback(response, _):
Response callback.
pylint: disable=import-outside-toplevel

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`response_callback`

**Imports** (4):
`openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.utils.errors`, `UnauthorizedError`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`

## Notes
- Generated: 2025-11-18T07:54:37.282270
- Generator: World's Best Repo Book Generator v1.0.0
