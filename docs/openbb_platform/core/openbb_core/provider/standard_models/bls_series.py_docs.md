# File Documentation: bls_series.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/bls_series.py`
- **Size**: 1,325 bytes
- **Lines**: 43
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""BLS Series Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class SeriesQueryParams(QueryParams):
    """BLS Series Query."""

    symbol: str = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", ""),
    )
    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class SeriesData(Data):
    """BLS Series Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    title: str | None = Field(default=None, description="Title of the series.")
    value: float | None = Field(
        default=None, description="Observation value for the symbol and date."
    )

```



---

## High-Level Overview

This is a **python** file named `bls_series.py`.

**Python Module**

- **Classes** (2): SeriesQueryParams, SeriesData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SeriesQueryParams`**(QueryParams)
- **`SeriesData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.354467Z
**Generator**: World's Best Repo Book Generator v1.0
