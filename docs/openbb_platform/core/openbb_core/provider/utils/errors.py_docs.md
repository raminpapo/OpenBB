# Documentation: openbb_platform/core/openbb_core/provider/utils/errors.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/utils/errors.py`
- **Size**: 1,248 characters, 38 lines
- **Words**: 115
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Custom exceptions for the provider.

from openbb_core.app.model.abstract.error import OpenBBError


class EmptyDataError(OpenBBError):
Exception raised for empty data.
Initialize the exception.
self.message = message
super().__init__(self.message)


class UnauthorizedError(OpenBBError):
Exception raised for an unauthorized provider request response.
Initialize the exception.
if provider_name and provider_name != "<provider name>":
msg = message
if isinstance(msg, tuple):
msg = msg[0].replace("<provider name>", provider_name)
elif isinstance(msg, str):

## Detailed Structure

### Python File Structure

**Classes** (2):
`EmptyDataError`, `UnauthorizedError`

**Functions** (2):
`__init__`, `__init__`

**Imports** (2):
`openbb_core.app.model.abstract.error`, `OpenBBError`


## Key Components

**Class `EmptyDataError`**: Exception raised for empty data.

**Class `UnauthorizedError`**: Exception raised for an unauthorized provider request response.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.abstract.error`

## Notes
- Generated: 2025-11-18T07:54:35.769333
- Generator: World's Best Repo Book Generator v1.0.0
