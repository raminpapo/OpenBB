# File Documentation: field.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/field.py`
- **Size**: 1,032 bytes
- **Lines**: 29
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Custom field for OpenBB."""

from typing import Any

from pydantic.fields import FieldInfo


class OpenBBField(FieldInfo):
    """Custom field for OpenBB."""

    def __repr__(self):
        """Override FieldInfo __repr__."""
        # We use repr() to avoid decoding special characters like \n
        if self.choices:
            return f"OpenBBField(description={repr(self.description)}, choices={repr(self.choices)})"
        return f"OpenBBField(description={repr(self.description)})"

    def __init__(self, description: str, choices: list[Any] | None = None):
        """Initialize OpenBBField."""
        json_schema_extra = {"choices": choices} if choices else None
        super().__init__(description=description, json_schema_extra=json_schema_extra)  # type: ignore[arg-type]

    @property
    def choices(self) -> list[Any] | None:
        """Custom choices."""
        if self.json_schema_extra:
            return self.json_schema_extra.get("choices")  # type: ignore[union-attr,return-value]
        return None

```



---

## High-Level Overview

This is a **python** file named `field.py`.

**Python Module**

- **Classes** (1): OpenBBField
- **Functions** (3): __repr__, __init__, choices
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`OpenBBField`**(FieldInfo)

#### Functions

- **`__repr__(self)`**
- **`__init__(self, description: str, choices: list[Any] | None = None)`**

#### Decorators Used

property


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `FieldInfo`
- `pydantic.fields`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.256407Z
**Generator**: World's Best Repo Book Generator v1.0
