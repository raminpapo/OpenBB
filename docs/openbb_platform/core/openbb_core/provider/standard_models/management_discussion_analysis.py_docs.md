# Documentation: openbb_platform/core/openbb_core/provider/standard_models/management_discussion_analysis.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/management_discussion_analysis.py`
- **Size**: 1,923 characters, 49 lines
- **Words**: 206
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Management Discussion & Analysis Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ManagementDiscussionAnalysisQueryParams(QueryParams):
    """Management Discussion & Analysis Query Parameters."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    calendar_year: int | None = Field(
        default=None,
        description="Calendar year of the report. By default, is the current year."
        + " If the calendar period is not provided, but the calendar year is, it will return the annual report.",
    )
    calendar_period: Literal["Q1", "Q2", "Q3", "Q4"] | None = Field(
        default=None,
        description="Calendar period of the report. By default, is the most recent report available for the symbol."
        + " If no calendar year and no calendar period are provided, it will return the most recent report.",
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class ManagementDiscussionAnalysisData(Data):
    """Management Discussion & Analysis Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    calendar_year: int = Field(description="The calendar year of the report.")
    calendar_period: int = Field(description="The calendar period of the report.")
    period_ending: dateType | None = Field(
        description="The end date of the reporting period.", default=None
    )
    content: str = Field(
        description="The content of the management discussion and analysis."
    )

```

## High-Level Overview

Management Discussion & Analysis Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ManagementDiscussionAnalysisQueryParams(QueryParams):
Management Discussion & Analysis Query Parameters.
Convert field to uppercase.
return v.upper()



## Detailed Structure

### Python File Structure

**Classes** (2):
`ManagementDiscussionAnalysisQueryParams`, `ManagementDiscussionAnalysisData`

**Functions** (1):
`to_upper`

**Imports** (11):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `ManagementDiscussionAnalysisQueryParams`**: Management Discussion & Analysis Query Parameters.

**Class `ManagementDiscussionAnalysisData`**: Management Discussion & Analysis Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.691997
- Generator: World's Best Repo Book Generator v1.0.0
