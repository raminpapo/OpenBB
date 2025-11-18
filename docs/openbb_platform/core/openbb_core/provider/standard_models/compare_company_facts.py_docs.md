# Documentation: openbb_platform/core/openbb_core/provider/standard_models/compare_company_facts.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/compare_company_facts.py`
- **Size**: 1,668 characters, 55 lines
- **Words**: 173
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Compare Company Facts Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CompareCompanyFactsQueryParams(QueryParams):
    """Compare Company Facts Query."""

    symbol: str | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("symbol", "")
    )
    fact: str = Field(
        default="",
        description="The fact to lookup, typically a GAAP-reporting measure. Choices vary by provider.",
    )


class CompareCompanyFactsData(Data):
    """Compare Company Facts Data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    name: str | None = Field(default=None, description="Name of the entity.")
    value: float = Field(
        description="The reported value of the fact or concept.",
    )
    reported_date: dateType | None = Field(
        default=None, description="The date when the report was filed."
    )
    period_beginning: dateType | None = Field(
        default=None,
        description="The start date of the reporting period.",
    )
    period_ending: dateType | None = Field(
        default=None,
        description="The end date of the reporting period.",
    )
    fiscal_year: int | None = Field(
        default=None,
        description="The fiscal year.",
    )
    fiscal_period: str | None = Field(
        default=None,
        description="The fiscal period of the fiscal year.",
    )

```

## High-Level Overview

Compare Company Facts Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CompareCompanyFactsQueryParams(QueryParams):
Compare Company Facts Query.
Compare Company Facts Data.

symbol: str | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
)

## Detailed Structure

### Python File Structure

**Classes** (2):
`CompareCompanyFactsQueryParams`, `CompareCompanyFactsData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CompareCompanyFactsQueryParams`**: Compare Company Facts Query.

**Class `CompareCompanyFactsData`**: Compare Company Facts Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.561647
- Generator: World's Best Repo Book Generator v1.0.0
