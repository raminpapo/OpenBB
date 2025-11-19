# File Documentation: country_interest_rates.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/country_interest_rates.py`
- **Size**: 1,265 bytes
- **Lines**: 42
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Country Interest Rates Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CountryInterestRatesQueryParams(QueryParams):
    """Country Interest Rates Query."""

    country: str = Field(
        default="united_states",
        description=QUERY_DESCRIPTIONS.get("country"),
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class CountryInterestRatesData(Data):
    """Country Interest Rates Data."""

    date: dateType = Field(default=None, description=DATA_DESCRIPTIONS.get("date"))
    value: float = Field(
        default=None,
        description="The interest rate value.",
        json_schema_extra={"x-unit_measurment": "percent", "x-frontend_multiply": 100},
    )
    country: str | None = Field(
        default=None,
        description="Country for which the interest rate is given.",
    )

```



---

## High-Level Overview

This is a **python** file named `country_interest_rates.py`.

**Python Module**

- **Classes** (2): CountryInterestRatesQueryParams, CountryInterestRatesData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CountryInterestRatesQueryParams`**(QueryParams)
- **`CountryInterestRatesData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.393082Z
**Generator**: World's Best Repo Book Generator v1.0
