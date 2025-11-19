# File Documentation: senior_loan_officer_survey.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/senior_loan_officer_survey.py`
- **Size**: 1,113 bytes
- **Lines**: 38
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Senior Loan Officer Opinion Survey Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class SeniorLoanOfficerSurveyQueryParams(QueryParams):
    """Senior Loan Officer Opinion Survey Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class SeniorLoanOfficerSurveyData(Data):
    """Senior Loan Officer Opinion Survey Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    value: float = Field(description="Survey value.")
    title: str | None = Field(description="Survey title.")

```



---

## High-Level Overview

This is a **python** file named `senior_loan_officer_survey.py`.

**Python Module**

- **Classes** (2): SeniorLoanOfficerSurveyQueryParams, SeniorLoanOfficerSurveyData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SeniorLoanOfficerSurveyQueryParams`**(QueryParams)
- **`SeniorLoanOfficerSurveyData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.567420Z
**Generator**: World's Best Repo Book Generator v1.0
