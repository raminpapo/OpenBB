# File Documentation: singleton.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/abstract/singleton.py`
- **Size**: 545 bytes
- **Lines**: 21
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `singleton.py`.

**Python Module**

- **Classes** (2): implementation, SingletonMeta
- **Functions** (1): __call__
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SingletonMeta`**(type, Generic[T])

#### Functions

- **`__call__(cls: "SingletonMeta", *args, **kwargs)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Generic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.272937Z
**Generator**: World's Best Repo Book Generator v1.0
