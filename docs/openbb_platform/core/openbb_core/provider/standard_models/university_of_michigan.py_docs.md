# Documentation: openbb_platform/core/openbb_core/provider/standard_models/university_of_michigan.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/university_of_michigan.py`
- **Size**: 1,371 characters, 43 lines
- **Words**: 127
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""University Of Michigan Survey Standard Model."""

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


class UofMichiganQueryParams(QueryParams):
    """University Of Michigan Survey Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class UofMichiganData(Data):
    """University Of Michigan Survey Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    consumer_sentiment: float | None = Field(
        default=None,
        description="Index of the results of the University of Michigan's monthly Survey of Consumers,"
        + " which is used to estimate future spending and saving.  (1966:Q1=100).",
    )
    inflation_expectation: float | None = Field(
        default=None,
        description="Median expected price change next 12 months, Surveys of Consumers.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```

## High-Level Overview

University Of Michigan Survey Standard Model.

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


class UofMichiganQueryParams(QueryParams):
University Of Michigan Survey Query.
University Of Michigan Survey Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`UofMichiganQueryParams`, `UofMichiganData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `UofMichiganQueryParams`**: University Of Michigan Survey Query.

**Class `UofMichiganData`**: University Of Michigan Survey Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.761200
- Generator: World's Best Repo Book Generator v1.0.0
