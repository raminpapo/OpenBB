# File Documentation: latest_financial_reports.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/latest_financial_reports.py`
- **Size**: 1,300 bytes
- **Lines**: 35
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `latest_financial_reports.py`.

**Python Module**

- **Classes** (2): LatestFinancialReportsQueryParams, LatestFinancialReportsData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`LatestFinancialReportsQueryParams`**(QueryParams)
- **`LatestFinancialReportsData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `DATA_DESCRIPTIONS`
- `Data`
- `Field`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.517873Z
**Generator**: World's Best Repo Book Generator v1.0
