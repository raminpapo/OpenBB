# File Documentation: high_quality_market.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/high_quality_market.py`
- **Size**: 982 bytes
- **Lines**: 34
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""High Quality Market Corporate Bond Standard Model."""

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


class HighQualityMarketCorporateBondQueryParams(QueryParams):
    """High Quality Market Corporate Bond Query."""

    date: dateType | str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", ""),
    )


class HighQualityMarketCorporateBondData(Data):
    """High Quality Market Corporate Bond Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float = Field(
        description="Interest rate.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    maturity: str = Field(description="Maturity.")

```



---

## High-Level Overview

This is a **python** file named `high_quality_market.py`.

**Python Module**

- **Classes** (2): HighQualityMarketCorporateBondQueryParams, HighQualityMarketCorporateBondData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`HighQualityMarketCorporateBondQueryParams`**(QueryParams)
- **`HighQualityMarketCorporateBondData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.486939Z
**Generator**: World's Best Repo Book Generator v1.0
