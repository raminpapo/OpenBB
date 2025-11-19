# File Documentation: overnight_bank_funding_rate.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/overnight_bank_funding_rate.py`
- **Size**: 2,215 bytes
- **Lines**: 64
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Overnight Bank Funding Rate Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class OvernightBankFundingRateQueryParams(QueryParams):
    """Overnight Bank Funding Rate Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class OvernightBankFundingRateData(Data):
    """Overnight Bank Funding Rate Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float = Field(
        description="Overnight Bank Funding Rate.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    percentile_1: float | None = Field(
        default=None,
        description="1st percentile of the distribution.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    percentile_25: float | None = Field(
        default=None,
        description="25th percentile of the distribution.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    percentile_75: float | None = Field(
        default=None,
        description="75th percentile of the distribution.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    percentile_99: float | None = Field(
        default=None,
        description="99th percentile of the distribution.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    volume: float | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("volume", "")
        + "The notional volume of transactions (Billions of $).",
        json_schema_extra={
            "x-unit_measurement": "currency",
            "x-frontend_multiply": 1e9,
        },
    )

```



---

## High-Level Overview

This is a **python** file named `overnight_bank_funding_rate.py`.

**Python Module**

- **Classes** (2): OvernightBankFundingRateQueryParams, OvernightBankFundingRateData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`OvernightBankFundingRateQueryParams`**(QueryParams)
- **`OvernightBankFundingRateData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.542241Z
**Generator**: World's Best Repo Book Generator v1.0
