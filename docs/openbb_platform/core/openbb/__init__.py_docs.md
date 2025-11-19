# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/core/openbb/__init__.py`
- **Size**: 1,475 bytes
- **Lines**: 51
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Functions** (1): build
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Extensions`
- `List`
- `PackageBuilder`
- `Path`
- `ReferenceLoader`
- `extensions.`
- `openbb.package.__extensions__`
- `openbb_core.app.static.app_factory`
- `openbb_core.app.static.package_builder`
- `openbb_core.app.static.reference_loader`
- `pathlib`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.176095Z
**Generator**: World's Best Repo Book Generator v1.0
