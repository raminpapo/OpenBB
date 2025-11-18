# Documentation: openbb_platform/core/openbb_core/provider/registry.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/registry.py`
- **Size**: 1,681 characters, 56 lines
- **Words**: 133
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Provider Registry Module.

import traceback
import warnings
from functools import lru_cache

from openbb_core.app.extension_loader import ExtensionLoader
from openbb_core.app.model.abstract.warning import OpenBBWarning
from openbb_core.env import Env
from openbb_core.provider.abstract.provider import Provider


class Registry:
Maintain registry of providers.
Initialize the registry.
self._providers: dict[str, Provider] = {}

@property
def providers(self):
Return a dictionary of providers.

## Detailed Structure

### Python File Structure

**Classes** (3):
`Registry`, `LoadingError`, `RegistryLoader`

**Functions** (4):
`__init__`, `providers`, `include_provider`, `from_extensions`

**Imports** (15):
`traceback`, `warnings`, `functools`, `lru_cache`, `openbb_core.app.extension_loader`, `ExtensionLoader`, `openbb_core.app.model.abstract.warning`, `OpenBBWarning`, `openbb_core.env`, `Env`, `openbb_core.provider.abstract.provider`, `Provider`, `entry`, `entry`, `e`


## Key Components

**Class `Registry`**: Maintain registry of providers.

**Class `LoadingError`**: Error loading provider.

**Class `RegistryLoader`**: Load providers from entry points.

## Usage & Examples

See source code for usage details.

## Related Files

- `traceback`
- `warnings`
- `functools`
- `openbb_core.app.extension_loader`
- `openbb_core.app.model.abstract.warning`
- `openbb_core.env`
- `openbb_core.provider.abstract.provider`

## Notes
- Generated: 2025-11-18T07:54:35.518927
- Generator: World's Best Repo Book Generator v1.0.0
