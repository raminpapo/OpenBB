# Documentation: openbb_platform/core/openbb_core/app/static/app_factory.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/static/app_factory.py`
- **Size**: 1,833 characters, 64 lines
- **Words**: 155
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

App factory.

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


## Detailed Structure

### Python File Structure

**Classes** (2):
`BaseApp`, `App`

**Functions** (7):
`__init__`, `user`, `system`, `coverage`, `reference`, `create_app`, `__repr__`

**Imports** (16):
`typing`, `TypeVar`, `openbb_core.app.command_runner`, `CommandRunner`, `openbb_core.app.model.system_settings`, `SystemSettings`, `openbb_core.app.model.user_settings`, `UserSettings`, `openbb_core.app.static.container`, `Container`, `openbb_core.app.static.coverage`, `Coverage`, `openbb_core.app.static.reference_loader`, `ReferenceLoader`, `openbb_core.app.version`, `VERSION`


## Key Components

**Class `BaseApp`**: Base app.

**Class `App`**: No documentation

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.app.command_runner`
- `openbb_core.app.model.system_settings`
- `openbb_core.app.model.user_settings`
- `openbb_core.app.static.container`
- `openbb_core.app.static.coverage`
- `openbb_core.app.static.reference_loader`
- `openbb_core.app.version`

## Notes
- Generated: 2025-11-18T07:54:35.479268
- Generator: World's Best Repo Book Generator v1.0.0
