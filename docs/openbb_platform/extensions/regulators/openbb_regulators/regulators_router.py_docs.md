# Documentation: openbb_platform/extensions/regulators/openbb_regulators/regulators_router.py

## File Metadata
- **Path**: `openbb_platform/extensions/regulators/openbb_regulators/regulators_router.py`
- **Size**: 418 characters, 16 lines
- **Words**: 39
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
# pylint: disable=import-outside-toplevel
# pylint: disable=unused-import
# ruff: noqa: F401
"""Regulators Router."""

from openbb_core.app.router import Router

from .cftc.cftc_router import (
    router as cftc_router,
)
from .sec.sec_router import router as sec_router

router = Router(prefix="", description="Financial market regulators data.")
router.include_router(sec_router)
router.include_router(cftc_router)

```

## High-Level Overview

pylint: disable=import-outside-toplevel
pylint: disable=unused-import
ruff: noqa: F401
Regulators Router.

from openbb_core.app.router import Router

from .cftc.cftc_router import (
router as cftc_router,
)
from .sec.sec_router import router as sec_router

router = Router(prefix="", description="Financial market regulators data.")
router.include_router(sec_router)
router.include_router(cftc_router)


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (5):
`openbb_core.app.router`, `Router`, `.cftc.cftc_router`, `.sec.sec_router`, `router`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.router`
- `.cftc.cftc_router`
- `.sec.sec_router`

## Notes
- Generated: 2025-11-18T07:54:36.344135
- Generator: World's Best Repo Book Generator v1.0.0
