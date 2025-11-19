# File Documentation: cik_map.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/cik_map.py`
- **Size**: 783 bytes
- **Lines**: 30
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Cik Map Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class CikMapQueryParams(QueryParams):
    """CikMap Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class CikMapData(Data):
    """CikMap Data."""

    cik: str | int | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("cik", "")
    )

```



---

## High-Level Overview

This is a **python** file named `cik_map.py`.

**Python Module**

- **Classes** (2): CikMapQueryParams, CikMapData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CikMapQueryParams`**(QueryParams)
- **`CikMapData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.374803Z
**Generator**: World's Best Repo Book Generator v1.0
