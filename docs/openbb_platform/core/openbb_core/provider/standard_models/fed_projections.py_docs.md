# Documentation: openbb_platform/core/openbb_core/provider/standard_models/fed_projections.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/fed_projections.py`
- **Size**: 1,184 characters, 32 lines
- **Words**: 116
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""PROJECTION Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class PROJECTIONQueryParams(QueryParams):
    """PROJECTION Query."""


class PROJECTIONData(Data):
    """PROJECTION Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    range_high: float | None = Field(description="High projection of rates.")
    central_tendency_high: float | None = Field(
        description="Central tendency of high projection of rates."
    )
    median: float | None = Field(description="Median projection of rates.")
    range_midpoint: float | None = Field(description="Midpoint projection of rates.")
    central_tendency_midpoint: float | None = Field(
        description="Central tendency of midpoint projection of rates."
    )
    range_low: float | None = Field(description="Low projection of rates.")
    central_tendency_low: float | None = Field(
        description="Central tendency of low projection of rates."
    )

```

## High-Level Overview

PROJECTION Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class PROJECTIONQueryParams(QueryParams):
PROJECTION Query.
PROJECTION Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
range_high: float | None = Field(description="High projection of rates.")
central_tendency_high: float | None = Field(
description="Central tendency of high projection of rates."
)
median: float | None = Field(description="Median projection of rates.")

## Detailed Structure

### Python File Structure

**Classes** (2):
`PROJECTIONQueryParams`, `PROJECTIONData`

**Functions** (0):
None

**Imports** (10):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `PROJECTIONQueryParams`**: PROJECTION Query.

**Class `PROJECTIONData`**: PROJECTION Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.628292
- Generator: World's Best Repo Book Generator v1.0.0
