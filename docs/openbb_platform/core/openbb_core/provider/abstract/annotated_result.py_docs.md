# File Documentation: annotated_result.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/abstract/annotated_result.py`
- **Size**: 449 bytes
- **Lines**: 21
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `annotated_result.py`.

**Python Module**

- **Classes** (1): AnnotatedResult
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AnnotatedResult`**(BaseModel, Generic[T])


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `Generic`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.328871Z
**Generator**: World's Best Repo Book Generator v1.0
