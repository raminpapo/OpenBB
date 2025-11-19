# File Documentation: historical_splits.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/historical_splits.py`
- **Size**: 1,169 bytes
- **Lines**: 42
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Historical Splits Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalSplitsQueryParams(QueryParams):
    """Historical Splits Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class HistoricalSplitsData(Data):
    """Historical Splits Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    numerator: float | None = Field(
        default=None,
        description="Numerator of the split.",
    )
    denominator: float | None = Field(
        default=None,
        description="Denominator of the split.",
    )
    split_ratio: str | None = Field(
        default=None,
        description="Split ratio.",
    )

```



---

## High-Level Overview

This is a **python** file named `historical_splits.py`.

**Python Module**

- **Classes** (2): HistoricalSplitsQueryParams, HistoricalSplitsData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`HistoricalSplitsQueryParams`**(QueryParams)
- **`HistoricalSplitsData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.494910Z
**Generator**: World's Best Repo Book Generator v1.0
