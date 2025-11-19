# File Documentation: app_factory.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/static/app_factory.py`
- **Size**: 1,833 bytes
- **Lines**: 64
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""App factory."""

from typing import TypeVar

from openbb_core.app.command_runner import CommandRunner
from openbb_core.app.model.system_settings import SystemSettings
from openbb_core.app.model.user_settings import UserSettings
from openbb_core.app.static.container import Container
from openbb_core.app.static.coverage import Coverage
from openbb_core.app.static.reference_loader import ReferenceLoader
from openbb_core.app.version import VERSION

E = TypeVar("E", bound=type[Container])
BASE_DOC = f"""OpenBB Platform v{VERSION}

Utilities:
    /user
    /system
    /coverage
"""


class BaseApp:
    """Base app."""

    def __init__(self, command_runner: CommandRunner):
        """Initialize the app."""
        command_runner.init_logging_service()
        self._command_runner = command_runner
        self._coverage = Coverage(self)
        self._reference = ReferenceLoader().reference

    @property
    def user(self) -> UserSettings:
        """User settings."""
        return self._command_runner.user_settings

    @property
    def system(self) -> SystemSettings:
        """System settings."""
        return self._command_runner.system_settings

    @property
    def coverage(self) -> Coverage:
        """Coverage menu."""
        return self._coverage

    @property
    def reference(self) -> dict[str, dict]:
        """Return reference data."""
        return self._reference


def create_app(extensions: E | None = None) -> type[BaseApp]:  # type: ignore
    """Create the app."""

    class App(BaseApp, extensions or object):  # type: ignore[misc]
        def __repr__(self) -> str:
            # pylint: disable=E1101
            ext_doc = extensions.__doc__ if extensions else ""
            return BASE_DOC + (ext_doc or "")

    return App(command_runner=CommandRunner())  # type: ignore[call-arg]

```



---

## High-Level Overview

This is a **python** file named `app_factory.py`.

**Python Module**

- **Classes** (2): BaseApp, App
- **Functions** (7): __init__, user, system, coverage, reference, create_app, __repr__
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`BaseApp`**
- **`App`**(BaseApp, extensions or object)

#### Functions

- **`__init__(self, command_runner: CommandRunner)`**

#### Decorators Used

property


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `CommandRunner`
- `Container`
- `Coverage`
- `ReferenceLoader`
- `SystemSettings`
- `TypeVar`
- `UserSettings`
- `VERSION`
- `openbb_core.app.command_runner`
- `openbb_core.app.model.system_settings`
- `openbb_core.app.model.user_settings`
- `openbb_core.app.static.container`
- `openbb_core.app.static.coverage`
- `openbb_core.app.static.reference_loader`
- `openbb_core.app.version`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.289797Z
**Generator**: World's Best Repo Book Generator v1.0
