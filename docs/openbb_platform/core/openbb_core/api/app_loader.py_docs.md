# File Documentation: app_loader.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/api/app_loader.py`
- **Size**: 1,679 bytes
- **Lines**: 44
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""App loader module."""

from fastapi import APIRouter, FastAPI
from fastapi.exceptions import ResponseValidationError
from openbb_core.api.exception_handlers import ExceptionHandlers
from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.app.router import RouterLoader
from openbb_core.provider.utils.errors import EmptyDataError, UnauthorizedError
from pydantic import ValidationError


class AppLoader:
    """App loader."""

    @staticmethod
    def add_routers(app: FastAPI, routers: list[APIRouter | None], prefix: str):
        """Add routers."""
        for router in routers:
            if router:
                app.include_router(router=router, prefix=prefix)

    @staticmethod
    def add_openapi_tags(app: FastAPI):
        """Add openapi tags."""
        main_router = RouterLoader.from_extensions()
        # Add tag data for each router in the main router
        app.openapi_tags = [
            {
                "name": r,
                "description": main_router.get_attr(r, "description"),
            }
            for r in main_router.routers
        ]

    @staticmethod
    def add_exception_handlers(app: FastAPI):
        """Add exception handlers."""
        app.exception_handlers[Exception] = ExceptionHandlers.exception
        app.exception_handlers[ValidationError] = ExceptionHandlers.validation
        app.exception_handlers[ResponseValidationError] = ExceptionHandlers.validation
        app.exception_handlers[OpenBBError] = ExceptionHandlers.openbb
        app.exception_handlers[EmptyDataError] = ExceptionHandlers.empty_data
        app.exception_handlers[UnauthorizedError] = ExceptionHandlers.unauthorized

```



---

## High-Level Overview

This is a **python** file named `app_loader.py`.

**Python Module**

- **Classes** (1): AppLoader
- **Functions** (3): add_routers, add_openapi_tags, add_exception_handlers
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AppLoader`**

#### Functions

- **`add_routers(app: FastAPI, routers: list[APIRouter | None], prefix: str)`**
- **`add_openapi_tags(app: FastAPI)`**
- **`add_exception_handlers(app: FastAPI)`**

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `APIRouter`
- `EmptyDataError`
- `ExceptionHandlers`
- `OpenBBError`
- `ResponseValidationError`
- `RouterLoader`
- `ValidationError`
- `fastapi`
- `fastapi.exceptions`
- `openbb_core.api.exception_handlers`
- `openbb_core.app.model.abstract.error`
- `openbb_core.app.router`
- `openbb_core.provider.utils.errors`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.186173Z
**Generator**: World's Best Repo Book Generator v1.0
