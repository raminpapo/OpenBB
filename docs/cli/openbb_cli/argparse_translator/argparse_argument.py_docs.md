# File Documentation: argparse_argument.py

## Metadata
- **Path**: `cli/openbb_cli/argparse_translator/argparse_argument.py`
- **Size**: 1,694 bytes
- **Lines**: 61
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `argparse_argument.py`.

**Python Module**

- **Classes** (2): ArgparseArgumentModel, ArgparseArgumentGroupModel
- **Functions** (3): validate_action, remove_props_on_store_true, model_dump
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ArgparseArgumentModel`**(BaseModel)
- **`ArgparseArgumentGroupModel`**(BaseModel)

#### Functions

- **`validate_action(cls, values: "ArgparseArgumentModel")`**
- **`remove_props_on_store_true(cls, values: "ArgparseArgumentModel")`**
- **`model_dump(self, **kwargs)`**

#### Decorators Used

classmethod, model_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:15:18.817302Z
**Generator**: World's Best Repo Book Generator v1.0
