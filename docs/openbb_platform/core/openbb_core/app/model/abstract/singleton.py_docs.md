# Documentation: openbb_platform/core/openbb_core/app/model/abstract/singleton.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/abstract/singleton.py`
- **Size**: 545 characters, 21 lines
- **Words**: 57
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Singleton metaclass implementation."""

from typing import Generic, TypeVar

T = TypeVar("T")


class SingletonMeta(type, Generic[T]):
    """Singleton metaclass."""

    # TODO : check if we want to update this to be thread safe
    _instances: dict[T, T] = {}

    def __call__(cls: "SingletonMeta", *args, **kwargs):
        """Singleton pattern implementation."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

```

## High-Level Overview

Singleton metaclass implementation.

from typing import Generic, TypeVar

T = TypeVar("T")


class SingletonMeta(type, Generic[T]):
Singleton metaclass.
TODO : check if we want to update this to be thread safe
Singleton pattern implementation.
if cls not in cls._instances:
instance = super().__call__(*args, **kwargs)
cls._instances[cls] = instance

return cls._instances[cls]


## Detailed Structure

### Python File Structure

**Classes** (2):
`implementation`, `SingletonMeta`

**Functions** (1):
`__call__`

**Imports** (2):
`typing`, `Generic`


## Key Components

**Class `implementation`**: Singleton metaclass.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`

## Notes
- Generated: 2025-11-18T07:54:35.433790
- Generator: World's Best Repo Book Generator v1.0.0
