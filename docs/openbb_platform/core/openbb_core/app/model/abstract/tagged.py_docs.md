# File Documentation: tagged.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/abstract/tagged.py`
- **Size**: 223 bytes
- **Lines**: 11
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OpenBB Core App Abstract Model Tagged."""

from pydantic import BaseModel, Field
from uuid_extensions import uuid7str


class Tagged(BaseModel):
    """Model for Tagged."""

    id: str = Field(default_factory=uuid7str)

```



---

## High-Level Overview

This is a **python** file named `tagged.py`.

**Python Module**

- **Classes** (1): Tagged
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Tagged`**(BaseModel)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `pydantic`
- `uuid7str`
- `uuid_extensions`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.274345Z
**Generator**: World's Best Repo Book Generator v1.0
