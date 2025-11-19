# File Documentation: key_metrics.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/key_metrics.py`
- **Size**: 1,429 bytes
- **Lines**: 46
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Key Metrics Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class KeyMetricsQueryParams(QueryParams):
    """Key Metrics Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class KeyMetricsData(Data):
    """Key Metrics Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    period_ending: dateType | None = Field(
        default=None, description="End date of the reporting period."
    )
    fiscal_year: int | None = Field(
        default=None, description="Fiscal year for the fiscal period, if available."
    )
    fiscal_period: str | None = Field(
        default=None, description="Fiscal period for the data, if available."
    )
    currency: str | None = Field(
        default=None,
        description="Currency in which the data is reported.",
    )
    market_cap: int | float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("market_cap", "")
    )

```



---

## High-Level Overview

This is a **python** file named `key_metrics.py`.

**Python Module**

- **Classes** (2): KeyMetricsQueryParams, KeyMetricsData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`KeyMetricsQueryParams`**(QueryParams)
- **`KeyMetricsData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.515090Z
**Generator**: World's Best Repo Book Generator v1.0
