# File Documentation: non_farm_payrolls.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/non_farm_payrolls.py`
- **Size**: 869 bytes
- **Lines**: 30
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""NonFarm Payrolls Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class NonFarmPayrollsQueryParams(QueryParams):
    """NonFarm Payrolls Query."""

    date: dateType | str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", "")
        + " Default is the latest report.",
    )


class NonFarmPayrollsData(Data):
    """NonFarm Payrolls Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    value: float = Field(description=DATA_DESCRIPTIONS.get("value", ""))

```



---

## High-Level Overview

This is a **python** file named `non_farm_payrolls.py`.

**Python Module**

- **Classes** (2): NonFarmPayrollsQueryParams, NonFarmPayrollsData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`NonFarmPayrollsQueryParams`**(QueryParams)
- **`NonFarmPayrollsData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.532000Z
**Generator**: World's Best Repo Book Generator v1.0
