# Documentation: openbb_platform/core/openbb_core/provider/standard_models/esg_risk_rating.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/esg_risk_rating.py`
- **Size**: 1,640 characters, 46 lines
- **Words**: 154
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ESG Risk Rating Standard Model."""

from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ESGRiskRatingQueryParams(QueryParams):
    """ESG Risk Rating Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class ESGRiskRatingData(Data):
    """ESG Risk Rating Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    cik: str = Field(description=DATA_DESCRIPTIONS.get("cik", ""))
    company_name: str = Field(description="Company name of the company.")
    industry: str = Field(description="Industry of the company.")
    year: int = Field(description="Year of the ESG risk rating.")
    esg_risk_rating: Literal[
        "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"
    ] = Field(description="ESG risk rating of the company.")
    industry_rank: str = Field(description="Industry rank of the company.")

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str | list[str] | set[str]):
        """Convert field to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])

```

## High-Level Overview

ESG Risk Rating Standard Model.

from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ESGRiskRatingQueryParams(QueryParams):
ESG Risk Rating Query.
Convert field to uppercase.
return v.upper()


class ESGRiskRatingData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`ESGRiskRatingQueryParams`, `ESGRiskRatingData`

**Functions** (2):
`to_upper`, `to_upper`

**Imports** (9):
`typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `ESGRiskRatingQueryParams`**: ESG Risk Rating Query.

**Class `ESGRiskRatingData`**: ESG Risk Rating Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.609344
- Generator: World's Best Repo Book Generator v1.0.0
