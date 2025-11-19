# File Documentation: dwpcr_rates.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/dwpcr_rates.py`
- **Size**: 989 bytes
- **Lines**: 34
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Discount Window Primary Credit Rate Standard Model."""

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


class DiscountWindowPrimaryCreditRateParams(QueryParams):
    """Discount Window Primary Credit Rate Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class DiscountWindowPrimaryCreditRateData(Data):
    """Discount Window Primary Credit Rate Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="Discount Window Primary Credit Rate.")

```



---

## High-Level Overview

This is a **python** file named `dwpcr_rates.py`.

**Python Module**

- **Classes** (2): DiscountWindowPrimaryCreditRateParams, DiscountWindowPrimaryCreditRateData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`DiscountWindowPrimaryCreditRateParams`**(QueryParams)
- **`DiscountWindowPrimaryCreditRateData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.409058Z
**Generator**: World's Best Repo Book Generator v1.0
