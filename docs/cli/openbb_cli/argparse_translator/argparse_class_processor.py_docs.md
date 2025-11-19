# File Documentation: argparse_class_processor.py

## Metadata
- **Path**: `cli/openbb_cli/argparse_translator/argparse_class_processor.py`
- **Size**: 4,828 bytes
- **Lines**: 148
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Module for the ArgparseClassProcessor class."""

import inspect
from typing import Any

# TODO: this needs to be done differently
from openbb_core.app.static.container import Container

from openbb_cli.argparse_translator.argparse_translator import ArgparseTranslator
from openbb_cli.argparse_translator.reference_processor import (
    ReferenceToArgumentsProcessor,
)


class ArgparseClassProcessor:
    """Process a target class to create ArgparseTranslators for its methods."""

    # reference variable used to create custom groups for the ArgpaseTranslators
    _reference: dict[str, Any] = {}

    def __init__(
        self,
        target_class: type,
        add_help: bool = False,
        reference: dict[str, Any] | None = None,
    ):
        """
        Initialize the ArgparseClassProcessor.

        Parameters
        ----------
        target_class : Type
            The target class whose methods will be processed.
        add_help : Optional[bool]
            Whether to add help to the ArgparseTranslators.
        """
        self._target_class: type = target_class
        self._add_help: bool = add_help
        self._translators: dict[str, ArgparseTranslator] = {}
        self._paths: dict[str, str] = {}

        ArgparseClassProcessor._reference = reference or {}

        self._translators = self._process_class(
            target=self._target_class, add_help=self._add_help
        )
        self._paths[self._get_class_name(self._target_class)] = "path"
        self._build_paths(target=self._target_class)

    @property
    def translators(self) -> dict[str, ArgparseTranslator]:
        """
        Get the ArgparseTranslators associated with the target class.

        Returns
        -------
        Dict[str, ArgparseTranslator]
            The ArgparseTranslators associated with the target class.
        """
        return self._translators

    @property
    def paths(self) -> dict[str, str]:
        """
        Get the paths associated with the target class.

        Returns
        -------
        Dict[str, str]
            The paths associated with the target class.
        """
        return self._paths

    @classmethod
    def _custom_groups_from_reference(cls, class_name: str, function_name: str) -> dict:
        route = f"/{class_name.replace('_', '/')}/{function_name}"
        reference = {route: cls._reference[route]} if route in cls._reference else {}
        if not reference:
            return {}
        rp = ReferenceToArgumentsProcessor(reference)
        return rp.custom_groups.get(route, {})  # type: ignore

    @classmethod
    def _process_class(
        cls,
        target: type,
        add_help: bool = False,
    ) -> dict[str, ArgparseTranslator]:
        methods = {}

        for name, member in inspect.getmembers(target):
            if name.startswith("__") or name.startswith("_"):
                continue
            if inspect.ismethod(member):
                class_name = cls._get_class_name(target)
                methods[f"{class_name}_{name}"] = ArgparseTranslator(
                    func=member,
                    add_help=add_help,
                    custom_argument_groups=cls._custom_groups_from_reference(  # type: ignore
                        class_name=class_name, function_name=name
                    ),
                )
            elif isinstance(member, Container):
                methods = {
                    **methods,
                    **cls._process_class(
                        target=getattr(target, name), add_help=add_help
                    ),
                }

        return methods

    @staticmethod
    def _get_class_name(target: type) -> str:
        return (
            str(type(target))
            .rsplit(".", maxsplit=1)[-1]
            .replace("'>", "")
            .replace("ROUTER_", "")
            .lower()
        )

    def get_translator(self, command: str) -> ArgparseTranslator:
        """
        Retrieve the ArgparseTranslator object associated with a specific menu and command.

        Parameters
        ----------
        command : str
            The command associated with the ArgparseTranslator.

        Returns
        -------
        ArgparseTranslator
            The ArgparseTranslator associated with the specified menu and command.
        """
        return self._translators[command]

    def _build_paths(self, target: type, depth: int = 1):
        for name, member in inspect.getmembers(target):
            if name.startswith("__") or name.startswith("_"):
                continue
            if inspect.ismethod(member):
                pass
            elif isinstance(member, Container):
                self._build_paths(target=getattr(target, name), depth=depth + 1)
                self._paths[f"{name}"] = "sub" * depth + "path"

```



---

## High-Level Overview

This is a **python** file named `argparse_class_processor.py`.

**Python Module**

- **Classes** (4): ArgparseClassProcessor, to, whose, self
- **Functions** (8): __init__, translators, paths, _custom_groups_from_reference, _process_class, _get_class_name, get_translator, _build_paths
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ArgparseClassProcessor`**

#### Functions

- **`__init__(
        self,
        target_class: type,
        add_help: bool = False,
        reference: dict[str, Any] | None = None,
    )`**
- **`_build_paths(self, target: type, depth: int = 1)`**

#### Decorators Used

classmethod, property, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `ArgparseTranslator`
- `Container`
- `inspect`
- `openbb_cli.argparse_translator.argparse_translator`
- `openbb_cli.argparse_translator.reference_processor`
- `openbb_core.app.static.container`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:15:18.818661Z
**Generator**: World's Best Repo Book Generator v1.0
