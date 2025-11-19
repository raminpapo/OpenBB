# File Documentation: mortgage_indices.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/mortgage_indices.py`
- **Size**: 1,197 bytes
- **Lines**: 45
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Mortgage Indices Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class MortgageIndicesQueryParams(QueryParams):
    """Mortgage Indices Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class MortgageIndicesData(Data):
    """Mortgage Indices Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    name: str | None = Field(
        default=None,
        description="Name of the index.",
    )
    rate: float = Field(
        description="Mortgage rate.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```



---

## High-Level Overview

This is a **python** file named `mortgage_indices.py`.

**Python Module**

- **Classes** (2): MortgageIndicesQueryParams, MortgageIndicesData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`MortgageIndicesQueryParams`**(QueryParams)
- **`MortgageIndicesData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.530723Z
**Generator**: World's Best Repo Book Generator v1.0
