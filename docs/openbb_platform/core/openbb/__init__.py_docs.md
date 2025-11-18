# Documentation: openbb_platform/core/openbb/__init__.py

## File Metadata
- **Path**: `openbb_platform/core/openbb/__init__.py`
- **Size**: 1,475 characters, 51 lines
- **Words**: 154
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OpenBB Platform."""

# flake8: noqa

from pathlib import Path
from typing import List, Optional, Union

from openbb_core.app.static.app_factory import (
    BaseApp as _BaseApp,
    create_app as _create_app,
)
from openbb_core.app.static.package_builder import PackageBuilder as _PackageBuilder
from openbb_core.app.static.reference_loader import ReferenceLoader as _ReferenceLoader

_this_dir = Path(__file__).parent.resolve()


def build(
    modules: Optional[Union[str, List[str]]] = None,
    lint: bool = True,
    verbose: bool = False,
) -> None:
    """Build extension modules.

    Parameters
    ----------
    modules : Optional[List[str]], optional
        The modules to rebuild, by default None
        For example: "/news" or ["/news", "/crypto"]
        If None, all modules are rebuilt.
    lint : bool, optional
        Whether to lint the code, by default True
    verbose : bool, optional
        Enable/disable verbose mode
    """
    _PackageBuilder(_this_dir, lint, verbose).build(modules)


_PackageBuilder(_this_dir).auto_build()
_ReferenceLoader(_this_dir)

try:
    # pylint: disable=import-outside-toplevel
    from openbb.package.__extensions__ import Extensions as _Extensions  # type: ignore

    obb: Union[_BaseApp, _Extensions] = _create_app(_Extensions)  # type: ignore
    sdk = obb
except (ImportError, ModuleNotFoundError):
    print("Failed to import extensions. Are any installed?")
    obb = sdk = _create_app()  # type: ignore

```

## High-Level Overview

OpenBB Platform.

# flake8: noqa

from pathlib import Path
from typing import List, Optional, Union

from openbb_core.app.static.app_factory import (
BaseApp as _BaseApp,
create_app as _create_app,
)
from openbb_core.app.static.package_builder import PackageBuilder as _PackageBuilder
from openbb_core.app.static.reference_loader import ReferenceLoader as _ReferenceLoader

_this_dir = Path(__file__).parent.resolve()


def build(
modules: Optional[Union[str, List[str]]] = None,
lint: bool = True,

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`build`

**Imports** (12):
`pathlib`, `Path`, `typing`, `List`, `openbb_core.app.static.app_factory`, `openbb_core.app.static.package_builder`, `PackageBuilder`, `openbb_core.app.static.reference_loader`, `ReferenceLoader`, `openbb.package.__extensions__`, `Extensions`, `extensions.`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pathlib`
- `typing`
- `openbb_core.app.static.app_factory`
- `openbb_core.app.static.package_builder`
- `openbb_core.app.static.reference_loader`
- `openbb.package.__extensions__`
- `extensions.`

## Notes
- Generated: 2025-11-18T07:54:35.386501
- Generator: World's Best Repo Book Generator v1.0.0
