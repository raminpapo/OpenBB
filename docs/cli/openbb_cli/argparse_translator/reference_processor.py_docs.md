# Documentation: cli/openbb_cli/argparse_translator/reference_processor.py

## File Metadata
- **Path**: `cli/openbb_cli/argparse_translator/reference_processor.py`
- **Size**: 4,430 characters, 123 lines
- **Words**: 359
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Module for the ReferenceToArgumentsProcessor class."""

import re
from typing import Any, Literal, get_origin

from openbb_cli.argparse_translator.argparse_argument import (
    ArgparseArgumentGroupModel,
    ArgparseArgumentModel,
)


class ReferenceToArgumentsProcessor:
    """Class to process the reference and build custom argument groups."""

    def __init__(self, reference: dict[str, dict]):
        """Initialize the ReferenceToArgumentsProcessor."""
        self._reference = reference
        self._custom_groups: dict[str, list[ArgparseArgumentGroupModel]] = {}

        self._build_custom_groups()

    @property
    def custom_groups(self) -> dict[str, list[ArgparseArgumentGroupModel]]:
        """Get the custom groups."""
        return self._custom_groups

    @staticmethod
    def _parse_type(type_string: str) -> type:
        """Parse the type from the string representation."""
        # Handle Optional[T] or T | None
        if "Optional" in type_string or "|" in type_string:
            # Extract the inner type, defaulting to str if parsing fails
            match = re.search(r"Optional\[(\w+)]|(\w+)\s*\|\s*None", type_string)
            if match:
                type_string = next(
                    (group for group in match.groups() if group is not None), "str"
                )

        # Handle Literal types
        if "Literal" in type_string:
            return str  # Treat all Literal types as strings for simplicity

        # Handle Annotated types by extracting the base type
        if "Annotated" in type_string:
            match = re.search(r"Annotated\[(\w+),", type_string)
            if match:
                type_string = match.group(1)

        # Map common string representations to actual types
        type_map = {
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "date": str,
            "datetime": str,
            "time": str,
        }
        return type_map.get(type_string, str)

    def _get_nargs(self, type_: type) -> Literal["+"] | None:
        """Get the nargs for the given type."""
        if get_origin(type_) is list:
            return "+"
        return None

    def _get_choices(self, type_string: str, custom_choices: Any) -> tuple | None:
        """Get the choices for the given type."""
        if custom_choices:
            return tuple(custom_choices)

        # Find all occurrences of Literal[...]
        literal_matches = re.findall(r"Literal\[(.*?)\]", type_string)
        if not literal_matches:
            return None

        all_choices: list = []
        for match in literal_matches:
            # Split by comma and strip quotes and whitespace
            choices = [c.strip().strip("'\"") for c in match.split(",") if c.strip()]
            all_choices.extend(choices)

        return tuple(set(all_choices)) if all_choices else None

    def _build_custom_groups(self):
        """Build the custom groups from the reference."""
        for route, v in self._reference.items():
            for provider, args in v["parameters"].items():
                if provider == "standard":
                    continue

                custom_arguments = []
                for arg in args:
                    if arg.get("standard"):
                        continue

                    type_ = self._parse_type(arg["type"])

                    custom_arguments.append(
                        ArgparseArgumentModel(
                            name=arg["name"],
                            type=type_,
                            dest=arg["name"],
                            default=arg["default"],
                            required=not (arg["optional"]),
                            action="store" if type_ is not bool else "store_true",
                            help=arg["description"],
                            nargs=self._get_nargs(type_),
                            choices=self._get_choices(
                                arg["type"], custom_choices=arg["choices"]
                            ),
                        )
                    )

                group = ArgparseArgumentGroupModel(
                    name=provider, arguments=custom_arguments
                )

                if route not in self._custom_groups:
                    self._custom_groups[route] = []

                self._custom_groups[route].append(group)

```

## High-Level Overview

Module for the ReferenceToArgumentsProcessor class.

import re
from typing import Any, Literal, get_origin

from openbb_cli.argparse_translator.argparse_argument import (
ArgparseArgumentGroupModel,
ArgparseArgumentModel,
)


class ReferenceToArgumentsProcessor:
Class to process the reference and build custom argument groups.
Initialize the ReferenceToArgumentsProcessor.
self._reference = reference
self._custom_groups: dict[str, list[ArgparseArgumentGroupModel]] = {}

self._build_custom_groups()

@property

## Detailed Structure

### Python File Structure

**Classes** (1):
`ReferenceToArgumentsProcessor`

**Functions** (6):
`__init__`, `custom_groups`, `_parse_type`, `_get_nargs`, `_get_choices`, `_build_custom_groups`

**Imports** (6):
`re`, `typing`, `Any`, `openbb_cli.argparse_translator.argparse_argument`, `the`, `the`


## Key Components

**Class `ReferenceToArgumentsProcessor`**: Class to process the reference and build custom argument groups.

## Usage & Examples

See source code for usage details.

## Related Files

- `re`
- `typing`
- `openbb_cli.argparse_translator.argparse_argument`

## Notes
- Generated: 2025-11-18T07:54:34.620033
- Generator: World's Best Repo Book Generator v1.0.0
