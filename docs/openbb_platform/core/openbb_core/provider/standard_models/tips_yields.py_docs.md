# File Documentation: tips_yields.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/tips_yields.py`
- **Size**: 1,370 bytes
- **Lines**: 48
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""TIPS (Treasury Inflation-Protected Securities) Yields Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TipsYieldsQueryParams(QueryParams):
    """TIPS Yields Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class TipsYieldsData(Data):
    """TIPS Yields Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    due: dateType | None = Field(
        default=None,
        description="The due date (maturation date) of the security.",
    )
    name: str | None = Field(
        default=None,
        description="The name of the security.",
    )
    value: float = Field(
        default=None,
        description="The yield value.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```



---

## High-Level Overview

This is a **python** file named `tips_yields.py`.

**Python Module**

- **Classes** (2): TipsYieldsQueryParams, TipsYieldsData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TipsYieldsQueryParams`**(QueryParams)
- **`TipsYieldsData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.583467Z
**Generator**: World's Best Repo Book Generator v1.0
