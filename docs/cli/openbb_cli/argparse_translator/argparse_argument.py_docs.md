# Documentation: cli/openbb_cli/argparse_translator/argparse_argument.py

## File Metadata
- **Path**: `cli/openbb_cli/argparse_translator/argparse_argument.py`
- **Size**: 1,694 characters, 61 lines
- **Words**: 178
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Pydantic models for argparse arguments and argument groups."""

from typing import (
    Any,
    Literal,
)

from pydantic import BaseModel, model_validator

SEP = "__"


class ArgparseArgumentModel(BaseModel):
    """Pydantic model for an argparse argument."""

    name: str
    type: Any
    dest: str
    default: Any
    required: bool
    action: Literal["store_true", "store"]
    help: str | None
    nargs: Literal["+"] | None
    choices: tuple | None

    @model_validator(mode="after")  # type: ignore
    @classmethod
    def validate_action(cls, values: "ArgparseArgumentModel"):
        """Validate the action based on the type."""
        if values.type is bool and values.action != "store_true":
            raise ValueError('If type is bool, action must be "store_true"')
        return values

    @model_validator(mode="after")  # type: ignore
    @classmethod
    def remove_props_on_store_true(cls, values: "ArgparseArgumentModel"):
        """Remove type, nargs, and choices if action is store_true."""
        if values.action == "store_true":
            values.type = None
            values.nargs = None
            values.choices = None
        return values

    # override
    def model_dump(self, **kwargs):
        """Override the model_dump method to remove empty choices."""
        res = super().model_dump(**kwargs)

        # Check if choices is present and if it's an empty tuple remove it
        if "choices" in res and not res["choices"]:
            del res["choices"]

        return res


class ArgparseArgumentGroupModel(BaseModel):
    """Pydantic model for a custom argument group."""

    name: str
    arguments: list[ArgparseArgumentModel]

```

## High-Level Overview

Pydantic models for argparse arguments and argument groups.

from typing import (
Any,
Literal,
)

from pydantic import BaseModel, model_validator

SEP = "__"


class ArgparseArgumentModel(BaseModel):
Pydantic model for an argparse argument.
Validate the action based on the type.
if values.type is bool and values.action != "store_true":
raise ValueError('If type is bool, action must be "store_true"')
return values

@model_validator(mode="after")  # type: ignore

## Detailed Structure

### Python File Structure

**Classes** (2):
`ArgparseArgumentModel`, `ArgparseArgumentGroupModel`

**Functions** (3):
`validate_action`, `remove_props_on_store_true`, `model_dump`

**Imports** (3):
`typing`, `pydantic`, `BaseModel`


## Key Components

**Class `ArgparseArgumentModel`**: Pydantic model for an argparse argument.

**Class `ArgparseArgumentGroupModel`**: Pydantic model for a custom argument group.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:34.613858
- Generator: World's Best Repo Book Generator v1.0.0
