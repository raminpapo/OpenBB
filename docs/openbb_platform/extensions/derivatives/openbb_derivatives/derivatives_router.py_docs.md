# Documentation: openbb_platform/extensions/derivatives/openbb_derivatives/derivatives_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/derivatives/openbb_derivatives/derivatives_router.py`
- **Size**: 372 characters, 11 lines
- **Words**: 26
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Derivatives Router."""

from openbb_core.app.router import Router

from openbb_derivatives.futures.futures_router import router as futures_router
from openbb_derivatives.options.options_router import router as options_router

router = Router(prefix="", description="Derivatives market data.")
router.include_router(options_router)
router.include_router(futures_router)

```

## High-Level Overview

Derivatives Router.

from openbb_core.app.router import Router

from openbb_derivatives.futures.futures_router import router as futures_router
from openbb_derivatives.options.options_router import router as options_router

router = Router(prefix="", description="Derivatives market data.")
router.include_router(options_router)
router.include_router(futures_router)


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (6):
`openbb_core.app.router`, `Router`, `openbb_derivatives.futures.futures_router`, `router`, `openbb_derivatives.options.options_router`, `router`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.router`
- `openbb_derivatives.futures.futures_router`
- `openbb_derivatives.options.options_router`

## Notes
- Generated: 2025-11-18T07:54:35.957500
- Generator: World's Best Repo Book Generator v1.0.0
