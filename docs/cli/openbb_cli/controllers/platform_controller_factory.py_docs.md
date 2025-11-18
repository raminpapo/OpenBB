# Documentation: cli/openbb_cli/controllers/platform_controller_factory.py

## File Metadata
- **Path**: `cli/openbb_cli/controllers/platform_controller_factory.py`
- **Size**: 2,054 characters, 57 lines
- **Words**: 156
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Platform controller factory to create a platform controller."""

from openbb_cli.argparse_translator.argparse_class_processor import (
    ArgparseClassProcessor,
)
from openbb_cli.controllers.base_platform_controller import PlatformController


class PlatformControllerFactory:
    """Factory to create a platform controller."""

    def __init__(self, platform_router: type, **kwargs):
        """Create the controller name."""
        self.platform_router = platform_router
        self._translated_target = ArgparseClassProcessor(
            target_class=self.platform_router, reference=kwargs.get("reference", {})
        )
        self.router_name = (
            str(type(self.platform_router))
            .rsplit(".", maxsplit=1)[-1]
            .replace("'>", "")
            .replace("ROUTER_", "")
            .lower()
        )
        self.controller_name = f"{self.router_name.capitalize()}Controller"

    def create(self) -> type:
        """Create the platform controller."""
        ClassName = self.controller_name
        Parents = (PlatformController,)
        Attributes: dict[str, bool | list[str]] = {"CHOICES_GENERATION": True}

        # Menu and Command choices generation
        choices_menus: list[str] = []
        choices_commands: list[str] = []
        translators = self._translated_target.translators
        paths = self._translated_target.paths
        # menus
        for key, value in paths.items():
            if value == "path":
                continue
            choices_menus.append(key)
        # commands
        for name, _ in translators.items():
            if any(f"{self.router_name}_{path}" in name for path in paths):
                continue
            new_name = name.replace(f"{self.router_name}_", "")
            choices_commands.append(new_name)

        Attributes["CHOICES_MENUS"] = choices_menus
        Attributes["CHOICES_COMMANDS"] = choices_commands

        # Use type to create the class
        DynamicClass = type(ClassName, Parents, Attributes)

        return DynamicClass

```

## High-Level Overview

Platform controller factory to create a platform controller.

from openbb_cli.argparse_translator.argparse_class_processor import (
ArgparseClassProcessor,
)
from openbb_cli.controllers.base_platform_controller import PlatformController


class PlatformControllerFactory:
Factory to create a platform controller.
Create the controller name.
self.platform_router = platform_router
self._translated_target = ArgparseClassProcessor(
target_class=self.platform_router, reference=kwargs.get("reference", {})
)
self.router_name = (
str(type(self.platform_router))
.rsplit(".", maxsplit=1)[-1]
.replace("'>", "")
.replace("ROUTER_", "")

## Detailed Structure

### Python File Structure

**Classes** (2):
`PlatformControllerFactory`, `DynamicClass`

**Functions** (2):
`__init__`, `create`

**Imports** (3):
`openbb_cli.argparse_translator.argparse_class_processor`, `openbb_cli.controllers.base_platform_controller`, `PlatformController`


## Key Components

**Class `PlatformControllerFactory`**: Factory to create a platform controller.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_cli.argparse_translator.argparse_class_processor`
- `openbb_cli.controllers.base_platform_controller`

## Notes
- Generated: 2025-11-18T07:54:34.654935
- Generator: World's Best Repo Book Generator v1.0.0
