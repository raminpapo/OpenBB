# File Documentation: institutional_ownership.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/institutional_ownership.py`
- **Size**: 1,054 bytes
- **Lines**: 35
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Institutional Ownership Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class InstitutionalOwnershipQueryParams(QueryParams):
    """Institutional Ownership Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class InstitutionalOwnershipData(Data):
    """Institutional Ownership Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    cik: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("cik", ""),
    )
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

```



---

## High-Level Overview

This is a **python** file named `institutional_ownership.py`.

**Python Module**

- **Classes** (2): InstitutionalOwnershipQueryParams, InstitutionalOwnershipData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`InstitutionalOwnershipQueryParams`**(QueryParams)
- **`InstitutionalOwnershipData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.511231Z
**Generator**: World's Best Repo Book Generator v1.0
