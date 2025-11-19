# File Documentation: company_filings.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/company_filings.py`
- **Size**: 1,398 bytes
- **Lines**: 44
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `company_filings.py`.

**Python Module**

- **Classes** (2): CompanyFilingsQueryParams, CompanyFilingsData
- **Functions** (2): to_upper, convert_date
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CompanyFilingsQueryParams`**(QueryParams)
- **`CompanyFilingsData`**(Data)

#### Functions

- **`to_upper(cls, v: str | list[str] | set[str])`**
- **`convert_date(cls, v: str)`**

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `datetime`
- `dateutil`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `parser`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.379468Z
**Generator**: World's Best Repo Book Generator v1.0
