# File Documentation: short_volume.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/short_volume.py`
- **Size**: 1,419 bytes
- **Lines**: 49
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Short Volume Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class ShortVolumeQueryParams(QueryParams):
    """Short Volume Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol"))


class ShortVolumeData(Data):
    """Short Volume Data."""

    date: dateType | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )

    market: str | None = Field(
        default=None,
        description="Reporting Facility ID. N=NYSE TRF, Q=NASDAQ TRF Carteret, B=NASDAQ TRY Chicago, D=FINRA ADF",
    )

    short_volume: int | None = Field(
        default=None,
        description=(
            "Aggregate reported share volume of executed short sale "
            "and short sale exempt trades during regular trading hours"
        ),
    )

    short_exempt_volume: int | None = Field(
        default=None,
        description="Aggregate reported share volume of executed short sale exempt trades during regular trading hours",
    )

    total_volume: int | None = Field(
        default=None,
        description="Aggregate reported share volume of executed trades during regular trading hours",
    )

```



---

## High-Level Overview

This is a **python** file named `short_volume.py`.

**Python Module**

- **Classes** (2): ShortVolumeQueryParams, ShortVolumeData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ShortVolumeQueryParams`**(QueryParams)
- **`ShortVolumeData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.572814Z
**Generator**: World's Best Repo Book Generator v1.0
