# Documentation: openbb_platform/core/openbb_core/provider/standard_models/company_filings.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/company_filings.py`
- **Size**: 1,398 characters, 44 lines
- **Words**: 131
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Company Filings Standard Model."""

from datetime import (
    date as dateType,
)

from dateutil import parser
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class CompanyFilingsQueryParams(QueryParams):
    """Company Filings Query."""

    symbol: str | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("symbol", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str | list[str] | set[str]):
        """Convert field to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)]) if v else None


class CompanyFilingsData(Data):
    """Company Filings Data."""

    filing_date: dateType = Field(description="The date of the filing.")
    report_type: str | None = Field(default=None, description="Type of filing.")
    report_url: str = Field(description="URL to the actual report.")

    @field_validator("filing_date", "accepted_date", mode="before", check_fields=False)
    @classmethod
    def convert_date(cls, v: str):
        """Convert date to date type."""
        return parser.parse(str(v)).date() if v else None

```

## High-Level Overview

Company Filings Standard Model.

from datetime import (
date as dateType,
)

from dateutil import parser
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class CompanyFilingsQueryParams(QueryParams):
Company Filings Query.
Convert field to uppercase.
if isinstance(v, str):
return v.upper()

## Detailed Structure

### Python File Structure

**Classes** (2):
`CompanyFilingsQueryParams`, `CompanyFilingsData`

**Functions** (2):
`to_upper`, `convert_date`

**Imports** (10):
`datetime`, `dateutil`, `parser`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CompanyFilingsQueryParams`**: Company Filings Query.

**Class `CompanyFilingsData`**: Company Filings Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `dateutil`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.558957
- Generator: World's Best Repo Book Generator v1.0.0
