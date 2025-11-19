# File Documentation: registry.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/registry.py`
- **Size**: 1,681 bytes
- **Lines**: 56
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Provider Registry Module."""

import traceback
import warnings
from functools import lru_cache

from openbb_core.app.extension_loader import ExtensionLoader
from openbb_core.app.model.abstract.warning import OpenBBWarning
from openbb_core.env import Env
from openbb_core.provider.abstract.provider import Provider


class Registry:
    """Maintain registry of providers."""

    def __init__(self) -> None:
        """Initialize the registry."""
        self._providers: dict[str, Provider] = {}

    @property
    def providers(self):
        """Return a dictionary of providers."""
        return self._providers

    def include_provider(self, provider: Provider) -> None:
        """Include a provider in the registry."""
        self._providers[provider.name.lower()] = provider


class LoadingError(Exception):
    """Error loading provider."""


class RegistryLoader:
    """Load providers from entry points."""

    @staticmethod
    @lru_cache
    def from_extensions() -> Registry:
        """Load providers from entry points."""
        registry = Registry()

        for name, entry in ExtensionLoader().provider_objects.items():  # type: ignore[attr-defined]
            try:
                registry.include_provider(provider=entry)
            except Exception as e:
                msg = f"Error loading extension: {name}\n"
                if Env().DEBUG_MODE:
                    traceback.print_exception(type(e), e, e.__traceback__)
                    raise LoadingError(msg + f"\033[91m{e}\033[0m") from e
                warnings.warn(
                    message=msg,
                    category=OpenBBWarning,
                )
        return registry

```



---

## High-Level Overview

This is a **python** file named `registry.py`.

**Python Module**

- **Classes** (3): Registry, LoadingError, RegistryLoader
- **Functions** (4): __init__, providers, include_provider, from_extensions
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Registry`**
- **`LoadingError`**(Exception)
- **`RegistryLoader`**

#### Functions

- **`providers(self)`**

#### Decorators Used

lru_cache, property, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Env`
- `ExtensionLoader`
- `OpenBBWarning`
- `Provider`
- `functools`
- `lru_cache`
- `openbb_core.app.extension_loader`
- `openbb_core.app.model.abstract.warning`
- `openbb_core.env`
- `openbb_core.provider.abstract.provider`
- `traceback`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.324101Z
**Generator**: World's Best Repo Book Generator v1.0
