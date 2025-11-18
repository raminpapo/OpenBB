# Documentation: openbb_platform/core/openbb_core/app/model/abstract/error.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/abstract/error.py`
- **Size**: 257 characters, 11 lines
- **Words**: 23
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OpenBB Error."""


class OpenBBError(Exception):
    """OpenBB Error."""

    def __init__(self, original: str | Exception | None = None):
        """Initialize the OpenBBError."""
        self.original = original
        super().__init__(str(original))

```

## High-Level Overview

OpenBB Error.


class OpenBBError(Exception):
OpenBB Error.
Initialize the OpenBBError.
self.original = original
super().__init__(str(original))


## Detailed Structure

### Python File Structure

**Classes** (1):
`OpenBBError`

**Functions** (1):
`__init__`

**Imports** (0):
None


## Key Components

**Class `OpenBBError`**: OpenBB Error.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.431473
- Generator: World's Best Repo Book Generator v1.0.0
