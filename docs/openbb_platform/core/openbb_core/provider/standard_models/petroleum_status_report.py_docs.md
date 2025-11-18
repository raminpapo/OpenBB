# Documentation: openbb_platform/core/openbb_core/provider/standard_models/petroleum_status_report.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/petroleum_status_report.py`
- **Size**: 1,342 characters, 39 lines
- **Words**: 130
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Petroleum Status Report Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class PetroleumStatusReportQueryParams(QueryParams):
    """Petroleum Status Report Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class PetroleumStatusReportData(Data):
    """Petroleum Status Report Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    table: str | None = Field(description="Table name for the data.")
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    order: int | None = Field(
        default=None, description="Presented order of the data, relative to the table."
    )
    title: str | None = Field(default=None, description="Title of the data.")
    value: int | float = Field(description="Value of the data.")
    unit: str | None = Field(default=None, description="Unit or scale of the data.")

```

## High-Level Overview

Petroleum Status Report Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class PetroleumStatusReportQueryParams(QueryParams):
Petroleum Status Report Query.
Petroleum Status Report Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
table: str | None = Field(description="Table name for the data.")
symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`PetroleumStatusReportQueryParams`, `PetroleumStatusReportData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `PetroleumStatusReportQueryParams`**: Petroleum Status Report Query.

**Class `PetroleumStatusReportData`**: Petroleum Status Report Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.713555
- Generator: World's Best Repo Book Generator v1.0.0
