# Documentation: openbb_platform/core/openbb_core/app/static/coverage.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/static/coverage.py`
- **Size**: 1,901 characters, 62 lines
- **Words**: 147
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Coverage module."""

from typing import TYPE_CHECKING, Any

from openbb_core.api.router.helpers.coverage_helpers import get_route_schema_map
from openbb_core.app.provider_interface import ProviderInterface
from openbb_core.app.router import CommandMap
from openbb_core.app.static.reference_loader import ReferenceLoader

if TYPE_CHECKING:
    from openbb_core.app.static.app_factory import BaseApp


class Coverage:  # noqa: D205, D400
    """/coverage
    providers
    commands
    command_model
    command_schemas
    reference
    """

    def __init__(self, app: "BaseApp"):
        """Initialize coverage."""
        self._app = app
        self._command_map = CommandMap(coverage_sep=".")
        self._provider_interface = ProviderInterface()
        self._reference_loader = ReferenceLoader()

    def __repr__(self) -> str:
        """Return docstring."""
        return self.__doc__ or ""

    @property
    def providers(self) -> dict[str, list[str]]:
        """Return providers coverage."""
        return self._command_map.provider_coverage

    @property
    def commands(self) -> dict[str, list[str]]:
        """Return commands coverage."""
        return self._command_map.command_coverage

    @property
    def command_model(self) -> dict[str, dict[str, dict[str, dict[str, Any]]]]:
        """Return command to model mapping."""
        return {
            command: self._provider_interface.map[value]
            for command, value in self._command_map.commands_model.items()
        }

    @property
    def reference(self) -> dict[str, dict]:
        """Return reference data."""
        return self._reference_loader.reference

    def command_schemas(self, filter_by_provider: str | None = None):
        """Return route schema for a command."""
        return get_route_schema_map(
            self._app, self._command_map.commands_model, filter_by_provider
        )

```

## High-Level Overview

Coverage module.

from typing import TYPE_CHECKING, Any

from openbb_core.api.router.helpers.coverage_helpers import get_route_schema_map
from openbb_core.app.provider_interface import ProviderInterface
from openbb_core.app.router import CommandMap
from openbb_core.app.static.reference_loader import ReferenceLoader

if TYPE_CHECKING:
from openbb_core.app.static.app_factory import BaseApp


class Coverage:  # noqa: D205, D400
/coverage


def __init__(self, app: "BaseApp"):
Initialize coverage.
Return docstring.

## Detailed Structure

### Python File Structure

**Classes** (1):
`Coverage`

**Functions** (7):
`__init__`, `__repr__`, `providers`, `commands`, `command_model`, `reference`, `command_schemas`

**Imports** (12):
`typing`, `TYPE_CHECKING`, `openbb_core.api.router.helpers.coverage_helpers`, `get_route_schema_map`, `openbb_core.app.provider_interface`, `ProviderInterface`, `openbb_core.app.router`, `CommandMap`, `openbb_core.app.static.reference_loader`, `ReferenceLoader`, `openbb_core.app.static.app_factory`, `BaseApp`


## Key Components

**Class `Coverage`**: No documentation

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.api.router.helpers.coverage_helpers`
- `openbb_core.app.provider_interface`
- `openbb_core.app.router`
- `openbb_core.app.static.reference_loader`
- `openbb_core.app.static.app_factory`

## Notes
- Generated: 2025-11-18T07:54:35.482211
- Generator: World's Best Repo Book Generator v1.0.0
