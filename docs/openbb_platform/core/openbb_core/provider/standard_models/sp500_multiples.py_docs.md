# File Documentation: sp500_multiples.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/sp500_multiples.py`
- **Size**: 2,106 bytes
- **Lines**: 79
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""SP500 Multiples Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field

SERIES_NAME = Literal[
    "shiller_pe_month",
    "shiller_pe_year",
    "pe_year",
    "pe_month",
    "dividend_year",
    "dividend_month",
    "dividend_growth_quarter",
    "dividend_growth_year",
    "dividend_yield_year",
    "dividend_yield_month",
    "earnings_year",
    "earnings_month",
    "earnings_growth_year",
    "earnings_growth_quarter",
    "real_earnings_growth_year",
    "real_earnings_growth_quarter",
    "earnings_yield_year",
    "earnings_yield_month",
    "real_price_year",
    "real_price_month",
    "inflation_adjusted_price_year",
    "inflation_adjusted_price_month",
    "sales_year",
    "sales_quarter",
    "sales_growth_year",
    "sales_growth_quarter",
    "real_sales_year",
    "real_sales_quarter",
    "real_sales_growth_year",
    "real_sales_growth_quarter",
    "price_to_sales_year",
    "price_to_sales_quarter",
    "price_to_book_value_year",
    "price_to_book_value_quarter",
    "book_value_year",
    "book_value_quarter",
]


class SP500MultiplesQueryParams(QueryParams):
    """SP500 Multiples Query."""

    series_name: SERIES_NAME | str = Field(
        description="The name of the series. Defaults to 'pe_month'.",
        default="pe_month",
    )
    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )


class SP500MultiplesData(Data):
    """SP500 Multiples Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    name: str = Field(
        description="Name of the series.",
    )
    value: int | float = Field(
        description="Value of the series.",
    )

```



---

## High-Level Overview

This is a **python** file named `sp500_multiples.py`.

**Python Module**

- **Classes** (2): SP500MultiplesQueryParams, SP500MultiplesData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SP500MultiplesQueryParams`**(QueryParams)
- **`SP500MultiplesData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `Literal`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.577091Z
**Generator**: World's Best Repo Book Generator v1.0
