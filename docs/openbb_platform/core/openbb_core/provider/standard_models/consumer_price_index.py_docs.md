# Documentation: openbb_platform/core/openbb_core/provider/standard_models/consumer_price_index.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/consumer_price_index.py`
- **Size**: 1,903 characters, 56 lines
- **Words**: 156
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""CPI Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ConsumerPriceIndexQueryParams(QueryParams):
    """CPI Query."""

    country: str = Field(
        description=QUERY_DESCRIPTIONS.get("country"),
        default="united_states",
    )
    transform: Literal["index", "yoy", "period"] = Field(
        description="Transformation of the CPI data. Period represents the change since previous."
        + " Defaults to change from one year ago (yoy).",
        default="yoy",
        json_schema_extra={"choices": ["index", "yoy", "period"]},
    )
    frequency: Literal["annual", "quarter", "monthly"] = Field(
        default="monthly",
        description=QUERY_DESCRIPTIONS.get("frequency"),
        json_schema_extra={"choices": ["annual", "quarter", "monthly"]},
    )
    harmonized: bool = Field(
        default=False, description="If true, returns harmonized data."
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )

    @field_validator("country", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v):
        """Convert country to lower case."""
        return v.replace(" ", "_").lower()


class ConsumerPriceIndexData(Data):
    """CPI data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
    country: str = Field(description=DATA_DESCRIPTIONS.get("country"))
    value: float = Field(description="CPI index value or period change.")

```

## High-Level Overview

CPI Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ConsumerPriceIndexQueryParams(QueryParams):
CPI Query.
Convert country to lower case.
return v.replace(" ", "_").lower()



## Detailed Structure

### Python File Structure

**Classes** (2):
`ConsumerPriceIndexQueryParams`, `ConsumerPriceIndexData`

**Functions** (1):
`to_lower`

**Imports** (12):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`, `one`


## Key Components

**Class `ConsumerPriceIndexQueryParams`**: CPI Query.

**Class `ConsumerPriceIndexData`**: CPI data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.565781
- Generator: World's Best Repo Book Generator v1.0.0
