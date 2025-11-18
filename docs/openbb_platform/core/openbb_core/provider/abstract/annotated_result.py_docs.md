# Documentation: openbb_platform/core/openbb_core/provider/abstract/annotated_result.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/abstract/annotated_result.py`
- **Size**: 449 characters, 21 lines
- **Words**: 48
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Annotated result."""

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class AnnotatedResult(BaseModel, Generic[T]):
    """Annotated result allows fetchers to return metadata along with the data."""

    result: T | None = Field(
        default=None,
        description="Serializable results.",
    )
    metadata: dict | None = Field(
        default=None,
        description="Metadata.",
    )

```

## High-Level Overview

Annotated result.

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class AnnotatedResult(BaseModel, Generic[T]):
Annotated result allows fetchers to return metadata along with the data.

## Detailed Structure

### Python File Structure

**Classes** (1):
`AnnotatedResult`

**Functions** (0):
None

**Imports** (4):
`typing`, `Generic`, `pydantic`, `BaseModel`


## Key Components

**Class `AnnotatedResult`**: Annotated result allows fetchers to return metadata along with the data.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.509587
- Generator: World's Best Repo Book Generator v1.0.0
