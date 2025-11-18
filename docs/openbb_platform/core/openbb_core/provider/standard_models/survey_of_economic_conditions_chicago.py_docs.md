# Documentation: openbb_platform/core/openbb_core/provider/standard_models/survey_of_economic_conditions_chicago.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/survey_of_economic_conditions_chicago.py`
- **Size**: 1,941 characters, 56 lines
- **Words**: 177
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Survey Of Economic Conditions - Chicago - Standard Model."""

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


class SurveyOfEconomicConditionsChicagoQueryParams(QueryParams):
    """Survey Of Economic Conditions - Chicago - Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class SurveyOfEconomicConditionsChicagoData(Data):
    """Survey Of Economic Conditions - Chicago - Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    activity_index: float | None = Field(default=None, description="Activity Index.")
    one_year_outlook: float | None = Field(
        default=None, description="One Year Outlook Index."
    )
    manufacturing_activity: float | None = Field(
        default=None, description="Manufacturing Activity Index."
    )
    non_manufacturing_activity: float | None = Field(
        default=None, description="Non-Manufacturing Activity Index."
    )
    capital_expenditures_expectations: float | None = Field(
        default=None, description="Capital Expenditures Expectations Index."
    )
    hiring_expectations: float | None = Field(
        default=None, description="Hiring Expectations Index."
    )
    current_hiring: float | None = Field(
        default=None, description="Current Hiring Index."
    )
    labor_costs: float | None = Field(default=None, description="Labor Costs Index.")
    non_labor_costs: float | None = Field(
        default=None, description="Non-Labor Costs Index."
    )

```

## High-Level Overview

Survey Of Economic Conditions - Chicago - Standard Model.

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


class SurveyOfEconomicConditionsChicagoQueryParams(QueryParams):
Survey Of Economic Conditions - Chicago - Query.
Survey Of Economic Conditions - Chicago - Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`SurveyOfEconomicConditionsChicagoQueryParams`, `SurveyOfEconomicConditionsChicagoData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `SurveyOfEconomicConditionsChicagoQueryParams`**: Survey Of Economic Conditions - Chicago - Query.

**Class `SurveyOfEconomicConditionsChicagoData`**: Survey Of Economic Conditions - Chicago - Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.745254
- Generator: World's Best Repo Book Generator v1.0.0
