# Documentation: openbb_platform/core/openbb_core/provider/standard_models/latest_financial_reports.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/latest_financial_reports.py`
- **Size**: 1,300 characters, 35 lines
- **Words**: 127
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Latest Financial Reports Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class LatestFinancialReportsQueryParams(QueryParams):
    """Latest Financial Reports Query."""


class LatestFinancialReportsData(Data):
    """Latest Financial Reports Data."""

    filing_date: dateType = Field(description="The date of the filing.")
    period_ending: dateType | None = Field(
        default=None, description="Report for the period ending."
    )
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol")
    )
    name: str | None = Field(default=None, description="Name of the company.")
    cik: str | None = Field(default=None, description=DATA_DESCRIPTIONS.get("cik"))
    sic: str | None = Field(
        default=None, description="Standard Industrial Classification code."
    )
    report_type: str | None = Field(default=None, description="Type of filing.")
    description: str | None = Field(
        default=None, description="Description of the report."
    )
    url: str = Field(description="URL to the filing page.")

```

## High-Level Overview

Latest Financial Reports Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class LatestFinancialReportsQueryParams(QueryParams):
Latest Financial Reports Query.
Latest Financial Reports Data.

filing_date: dateType = Field(description="The date of the filing.")
period_ending: dateType | None = Field(
default=None, description="Report for the period ending."
)
symbol: str | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("symbol")

## Detailed Structure

### Python File Structure

**Classes** (2):
`LatestFinancialReportsQueryParams`, `LatestFinancialReportsData`

**Functions** (0):
None

**Imports** (10):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `LatestFinancialReportsQueryParams`**: Latest Financial Reports Query.

**Class `LatestFinancialReportsData`**: Latest Financial Reports Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.689535
- Generator: World's Best Repo Book Generator v1.0.0
