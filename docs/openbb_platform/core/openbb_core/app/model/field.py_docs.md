# Documentation: openbb_platform/core/openbb_core/app/model/field.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/field.py`
- **Size**: 1,032 characters, 29 lines
- **Words**: 84
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Custom field for OpenBB.

from typing import Any

from pydantic.fields import FieldInfo


class OpenBBField(FieldInfo):
Custom field for OpenBB.
Override FieldInfo __repr__.
# We use repr() to avoid decoding special characters like \n
if self.choices:
return f"OpenBBField(description={repr(self.description)}, choices={repr(self.choices)})"
return f"OpenBBField(description={repr(self.description)})"

def __init__(self, description: str, choices: list[Any] | None = None):
Initialize OpenBBField.
Custom choices.
if self.json_schema_extra:
return self.json_schema_extra.get("choices")  # type: ignore[union-attr,return-value]

## Detailed Structure

### Python File Structure

**Classes** (1):
`OpenBBField`

**Functions** (3):
`__repr__`, `__init__`, `choices`

**Imports** (4):
`typing`, `Any`, `pydantic.fields`, `FieldInfo`


## Key Components

**Class `OpenBBField`**: Custom field for OpenBB.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `pydantic.fields`

## Notes
- Generated: 2025-11-18T07:54:35.452305
- Generator: World's Best Repo Book Generator v1.0.0
