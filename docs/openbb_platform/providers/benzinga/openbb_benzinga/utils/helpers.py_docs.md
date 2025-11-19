# File Documentation: helpers.py

## Metadata
- **Path**: `openbb_platform/providers/benzinga/openbb_benzinga/utils/helpers.py`
- **Size**: 639 bytes
- **Lines**: 22
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `helpers.py`.

**Python Module**

- **Functions** (1): response_callback
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`response_callback(response, _)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `OpenBBError`
- `UnauthorizedError`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.290567Z
**Generator**: World's Best Repo Book Generator v1.0
