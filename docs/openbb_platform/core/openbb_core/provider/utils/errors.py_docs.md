# File Documentation: errors.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/utils/errors.py`
- **Size**: 1,248 bytes
- **Lines**: 38
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Custom exceptions for the provider."""

from openbb_core.app.model.abstract.error import OpenBBError


class EmptyDataError(OpenBBError):
    """Exception raised for empty data."""

    def __init__(
        self, message: str = "No results found. Try adjusting the query parameters."
    ):
        """Initialize the exception."""
        self.message = message
        super().__init__(self.message)


class UnauthorizedError(OpenBBError):
    """Exception raised for an unauthorized provider request response."""

    def __init__(
        self,
        message: str | tuple[str] = (
            "Unauthorized <provider name> API request."
            " Please check your <provider name> credentials and subscription access.",
        ),
        provider_name: str = "<provider name>",
    ):
        """Initialize the exception."""
        if provider_name and provider_name != "<provider name>":
            msg = message
            if isinstance(msg, tuple):
                msg = msg[0].replace("<provider name>", provider_name)
            elif isinstance(msg, str):
                msg = msg.replace("<provider name>", provider_name)
            message = msg
        self.message = message
        super().__init__(str(self.message))

```



---

## High-Level Overview

This is a **python** file named `errors.py`.

**Python Module**

- **Classes** (2): EmptyDataError, UnauthorizedError
- **Functions** (2): __init__, __init__
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EmptyDataError`**(OpenBBError)
- **`UnauthorizedError`**(OpenBBError)

#### Functions

- **`__init__(
        self, message: str = "No results found. Try adjusting the query parameters."
    )`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `OpenBBError`
- `openbb_core.app.model.abstract.error`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.605658Z
**Generator**: World's Best Repo Book Generator v1.0
