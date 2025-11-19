# File Documentation: country_profile.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/country_profile.py`
- **Size**: 3,653 bytes
- **Lines**: 87
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Country Profile Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class CountryProfileQueryParams(QueryParams):
    """Country Profile Query."""

    country: str = Field(description=QUERY_DESCRIPTIONS.get("country", ""))

    @field_validator("country", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str) -> str:
        """Convert the country to lowercase."""
        return v.lower().replace(" ", "_")


class CountryProfileData(Data):
    """Country Profile Data."""

    country: str = Field(description=DATA_DESCRIPTIONS.get("country", ""))
    population: int | None = Field(default=None, description="Population.")
    gdp_usd: float | None = Field(
        default=None, description="Gross Domestic Product, in billions of USD."
    )
    gdp_qoq: float | None = Field(
        default=None,
        description="GDP growth quarter-over-quarter change, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    gdp_yoy: float | None = Field(
        default=None,
        description="GDP growth year-over-year change, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    cpi_yoy: float | None = Field(
        default=None,
        description="Consumer Price Index year-over-year change, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    core_yoy: float | None = Field(
        default=None,
        description="Core Consumer Price Index year-over-year change, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    retail_sales_yoy: float | None = Field(
        default=None,
        description="Retail Sales year-over-year change, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    industrial_production_yoy: float | None = Field(
        default=None,
        description="Industrial Production year-over-year change, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    policy_rate: float | None = Field(
        default=None,
        description="Short term policy rate, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    yield_10y: float | None = Field(
        default=None,
        description="10-year government bond yield, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    govt_debt_gdp: float | None = Field(
        default=None,
        description="Government debt as a percent (normalized) of GDP.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    current_account_gdp: float | None = Field(
        default=None,
        description="Current account balance as a percent (normalized) of GDP.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    jobless_rate: float | None = Field(
        default=None,
        description="Unemployment rate, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```



---

## High-Level Overview

This is a **python** file named `country_profile.py`.

**Python Module**

- **Classes** (2): CountryProfileQueryParams, CountryProfileData
- **Functions** (1): to_lower
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CountryProfileQueryParams`**(QueryParams)
- **`CountryProfileData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.394975Z
**Generator**: World's Best Repo Book Generator v1.0
