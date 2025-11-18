# Documentation: openbb_platform/core/openbb_core/provider/standard_models/personal_consumption_expenditures.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/personal_consumption_expenditures.py`
- **Size**: 952 characters, 30 lines
- **Words**: 76
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Personal Consumption Expenditures Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class PersonalConsumptionExpendituresQueryParams(QueryParams):
    """Personal Consumption Expenditures Query."""

    date: dateType | str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", "")
        + " Default is the latest report.",
    )


class PersonalConsumptionExpendituresData(Data):
    """Personal Consumption Expenditures Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    value: float = Field(description=DATA_DESCRIPTIONS.get("value", ""))

```

## High-Level Overview

Personal Consumption Expenditures Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class PersonalConsumptionExpendituresQueryParams(QueryParams):
Personal Consumption Expenditures Query.
Personal Consumption Expenditures Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
value: float = Field(description=DATA_DESCRIPTIONS.get("value", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`PersonalConsumptionExpendituresQueryParams`, `PersonalConsumptionExpendituresData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `PersonalConsumptionExpendituresQueryParams`**: Personal Consumption Expenditures Query.

**Class `PersonalConsumptionExpendituresData`**: Personal Consumption Expenditures Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.712477
- Generator: World's Best Repo Book Generator v1.0.0
