# Documentation: openbb_platform/core/openbb_core/api/app_loader.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/api/app_loader.py`
- **Size**: 1,679 characters, 44 lines
- **Words**: 118
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

App loader module.

from fastapi import APIRouter, FastAPI
from fastapi.exceptions import ResponseValidationError
from openbb_core.api.exception_handlers import ExceptionHandlers
from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.app.router import RouterLoader
from openbb_core.provider.utils.errors import EmptyDataError, UnauthorizedError
from pydantic import ValidationError


class AppLoader:
App loader.
Add routers.
for router in routers:
if router:
app.include_router(router=router, prefix=prefix)

@staticmethod
def add_openapi_tags(app: FastAPI):

## Detailed Structure

### Python File Structure

**Classes** (1):
`AppLoader`

**Functions** (3):
`add_routers`, `add_openapi_tags`, `add_exception_handlers`

**Imports** (14):
`fastapi`, `APIRouter`, `fastapi.exceptions`, `ResponseValidationError`, `openbb_core.api.exception_handlers`, `ExceptionHandlers`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.app.router`, `RouterLoader`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `ValidationError`


## Key Components

**Class `AppLoader`**: App loader.

## Usage & Examples

See source code for usage details.

## Related Files

- `fastapi`
- `fastapi.exceptions`
- `openbb_core.api.exception_handlers`
- `openbb_core.app.model.abstract.error`
- `openbb_core.app.router`
- `openbb_core.provider.utils.errors`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.391391
- Generator: World's Best Repo Book Generator v1.0.0
