# File Documentation: auth_service.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/service/auth_service.py`
- **Size**: 2,620 bytes
- **Lines**: 77
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Auth service."""

import logging
from collections.abc import Awaitable, Callable
from importlib import import_module
from types import ModuleType

from fastapi import APIRouter
from openbb_core.api.router.user import (
    auth_hook as default_auth_hook,
    router as default_router,
    user_settings_hook as default_user_settings_hook,
)
from openbb_core.app.extension_loader import ExtensionLoader
from openbb_core.app.model.abstract.singleton import SingletonMeta
from openbb_core.app.model.user_settings import UserSettings
from openbb_core.env import Env

EXT_NAME = Env().API_AUTH_EXTENSION

logger = logging.getLogger("uvicorn.error")


class AuthServiceError(Exception):
    """Authentication service error."""


class AuthService(metaclass=SingletonMeta):
    """Auth service."""

    def __init__(self, ext_name: str | None = EXT_NAME) -> None:
        """Initialize AuthService."""
        if not self._load_extension(ext_name):
            self._router = default_router
            self._auth_hook = default_auth_hook
            self._user_settings_hook = default_user_settings_hook

    @property
    def router(self) -> APIRouter:
        """Get router."""
        return self._router

    @property
    def auth_hook(self) -> Callable[..., Awaitable[None]]:
        """Get general authentication hook."""
        return self._auth_hook

    @property
    def user_settings_hook(self) -> Callable[..., Awaitable[UserSettings]]:
        """Get user settings hook."""
        return self._user_settings_hook

    @staticmethod
    def _is_installed(ext_name: str) -> bool:
        """Check if auth_extension is installed."""
        extension = ExtensionLoader().get_core_entry_point(ext_name) or False
        return extension and ext_name == extension.name  # type: ignore

    @staticmethod
    def _get_entry_mod(ext_name: str) -> ModuleType:
        """Get the module of the given auth_extension."""
        extension = ExtensionLoader().get_core_entry_point(ext_name)
        if not extension:
            raise AuthServiceError(f"Extension '{ext_name}' is not installed.")
        return import_module(extension.module)

    def _load_extension(self, ext_name: str | None) -> bool:
        """Load auth extension."""
        if ext_name and self._is_installed(ext_name):
            entry_mod = self._get_entry_mod(ext_name)
            self._router = entry_mod.router
            self._auth_hook = entry_mod.auth_hook
            self._user_settings_hook = entry_mod.user_settings_hook
            logger.info("Loaded auth_extension: %s", ext_name)
            return True
        return False

```



---

## High-Level Overview

This is a **python** file named `auth_service.py`.

**Python Module**

- **Classes** (2): AuthServiceError, AuthService
- **Functions** (7): __init__, router, auth_hook, user_settings_hook, _is_installed, _get_entry_mod, _load_extension
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AuthServiceError`**(Exception)
- **`AuthService`**(metaclass=SingletonMeta)

#### Decorators Used

property, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `APIRouter`
- `Awaitable`
- `Env`
- `ExtensionLoader`
- `ModuleType`
- `SingletonMeta`
- `UserSettings`
- `collections.abc`
- `fastapi`
- `import_module`
- `importlib`
- `logging`
- `openbb_core.api.router.user`
- `openbb_core.app.extension_loader`
- `openbb_core.app.model.abstract.singleton`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.283422Z
**Generator**: World's Best Repo Book Generator v1.0
