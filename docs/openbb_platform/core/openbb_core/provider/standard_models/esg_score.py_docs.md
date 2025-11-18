# Documentation: openbb_platform/core/openbb_core/provider/standard_models/esg_score.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/esg_score.py`
- **Size**: 1,822 characters, 55 lines
- **Words**: 178
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ESG Score Standard Model."""

from datetime import (
    date as dateType,
    datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EsgScoreQueryParams(QueryParams):
    """ESG Score Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EsgScoreData(Data):
    """ESG Score Data."""

    period_ending: dateType = Field(description="Period ending date of the report.")
    disclosure_date: dateType | datetime | None = Field(
        description="Date when the report was submitted."
    )
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    cik: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("cik", ""),
        coerce_numbers_to_str=True,
    )
    company_name: str | None = Field(
        default=None, description="Company name of the company."
    )
    form_type: str | None = Field(
        default=None, description="Form type where the disclosure was made."
    )
    environmental_score: float = Field(
        description="Environmental score of the company."
    )
    social_score: float = Field(description="Social score of the company.")
    governance_score: float = Field(description="Governance score of the company.")
    esg_score: float = Field(description="ESG score of the company.")
    url: str | None = Field(default=None, description="URL to the report or filing.")

```

## High-Level Overview

ESG Score Standard Model.

from datetime import (
date as dateType,
datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EsgScoreQueryParams(QueryParams):
ESG Score Query.
Convert field to uppercase.
return v.upper()

## Detailed Structure

### Python File Structure

**Classes** (2):
`EsgScoreQueryParams`, `EsgScoreData`

**Functions** (1):
`to_upper`

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EsgScoreQueryParams`**: ESG Score Query.

**Class `EsgScoreData`**: ESG Score Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.610662
- Generator: World's Best Repo Book Generator v1.0.0
