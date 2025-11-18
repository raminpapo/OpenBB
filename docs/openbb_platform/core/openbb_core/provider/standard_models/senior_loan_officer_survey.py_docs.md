# Documentation: openbb_platform/core/openbb_core/provider/standard_models/senior_loan_officer_survey.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/senior_loan_officer_survey.py`
- **Size**: 1,113 characters, 38 lines
- **Words**: 97
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Senior Loan Officer Opinion Survey Standard Model.

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
Senior Loan Officer Opinion Survey Query.
Senior Loan Officer Opinion Survey Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`SeniorLoanOfficerSurveyQueryParams`, `SeniorLoanOfficerSurveyData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `SeniorLoanOfficerSurveyQueryParams`**: Senior Loan Officer Opinion Survey Query.

**Class `SeniorLoanOfficerSurveyData`**: Senior Loan Officer Opinion Survey Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.733895
- Generator: World's Best Repo Book Generator v1.0.0
