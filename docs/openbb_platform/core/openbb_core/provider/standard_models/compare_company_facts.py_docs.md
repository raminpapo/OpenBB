# File Documentation: compare_company_facts.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/compare_company_facts.py`
- **Size**: 1,668 bytes
- **Lines**: 55
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `compare_company_facts.py`.

**Python Module**

- **Classes** (2): CompareCompanyFactsQueryParams, CompareCompanyFactsData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CompareCompanyFactsQueryParams`**(QueryParams)
- **`CompareCompanyFactsData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
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

**Generated**: 2025-11-19T02:16:46.383390Z
**Generator**: World's Best Repo Book Generator v1.0
