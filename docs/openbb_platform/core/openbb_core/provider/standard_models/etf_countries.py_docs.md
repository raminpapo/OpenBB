# Documentation: openbb_platform/core/openbb_core/provider/standard_models/etf_countries.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_countries.py`
- **Size**: 1,148 characters, 37 lines
- **Words**: 105
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

ETF Countries Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfCountriesQueryParams(QueryParams):
ETF Countries Query.
Convert field to uppercase.
return v.upper()


class EtfCountriesData(Data):
ETF Countries Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`EtfCountriesQueryParams`, `EtfCountriesData`

**Functions** (1):
`to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EtfCountriesQueryParams`**: ETF Countries Query.

**Class `EtfCountriesData`**: ETF Countries Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.613089
- Generator: World's Best Repo Book Generator v1.0.0
