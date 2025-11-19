# File Documentation: etf_countries.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_countries.py`
- **Size**: 1,148 bytes
- **Lines**: 37
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ETF Countries Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfCountriesQueryParams(QueryParams):
    """ETF Countries Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfCountriesData(Data):
    """ETF Countries Data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    country: str = Field(
        description="The country of the exposure.  Corresponding values are normalized percentage points."
    )
    weight: float = Field(
        description="The net exposure of the ETF to the country as a percentage of the total ETF assets.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```



---

## High-Level Overview

This is a **python** file named `etf_countries.py`.

**Python Module**

- **Classes** (2): EtfCountriesQueryParams, EtfCountriesData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EtfCountriesQueryParams`**(QueryParams)
- **`EtfCountriesData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.439544Z
**Generator**: World's Best Repo Book Generator v1.0
