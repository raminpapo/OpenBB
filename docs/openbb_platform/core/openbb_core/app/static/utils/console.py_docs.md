# Documentation: openbb_platform/core/openbb_core/app/static/utils/console.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/static/utils/console.py`
- **Size**: 408 characters, 17 lines
- **Words**: 43
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Console module."""

from openbb_core.env import Env


class Console:
    """Console to be used by builder and linters."""

    def __init__(self, verbose: bool):
        """Initialize the console."""
        self.verbose = verbose

    def log(self, message: str, **kwargs):
        """Console log method."""
        if self.verbose or Env().DEBUG_MODE:
            print(message, **kwargs)  # noqa: T201

```

## High-Level Overview

Console module.

from openbb_core.env import Env


class Console:
Console to be used by builder and linters.
Initialize the console.
self.verbose = verbose

def log(self, message: str, **kwargs):
Console log method.

## Detailed Structure

### Python File Structure

**Classes** (1):
`Console`

**Functions** (2):
`__init__`, `log`

**Imports** (2):
`openbb_core.env`, `Env`


## Key Components

**Class `Console`**: Console to be used by builder and linters.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.env`

## Notes
- Generated: 2025-11-18T07:54:35.495155
- Generator: World's Best Repo Book Generator v1.0.0
