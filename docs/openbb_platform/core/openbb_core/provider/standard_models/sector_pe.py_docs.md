# Documentation: openbb_platform/core/openbb_core/provider/standard_models/sector_pe.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/sector_pe.py`
- **Size**: 784 characters, 26 lines
- **Words**: 81
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Sector P/E Ratio Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class SectorPEQueryParams(QueryParams):
    """Sector P/E Ratio Query."""


class SectorPEData(Data):
    """Sector P/E Ratio Data."""

    date: dateType | None = Field(
        description=DATA_DESCRIPTIONS.get("date", ""), default=None
    )
    exchange: str | None = Field(
        default=None, description="The exchange where the data is from."
    )
    sector: str = Field(description="The name of the sector.")
    pe: float = Field(description="The P/E ratio of the sector.")

```

## High-Level Overview

Sector P/E Ratio Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class SectorPEQueryParams(QueryParams):
Sector P/E Ratio Query.
Sector P/E Ratio Data.

date: dateType | None = Field(
description=DATA_DESCRIPTIONS.get("date", ""), default=None
)
exchange: str | None = Field(
default=None, description="The exchange where the data is from."
)

## Detailed Structure

### Python File Structure

**Classes** (2):
`SectorPEQueryParams`, `SectorPEData`

**Functions** (0):
None

**Imports** (10):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `SectorPEQueryParams`**: Sector P/E Ratio Query.

**Class `SectorPEData`**: Sector P/E Ratio Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.731409
- Generator: World's Best Repo Book Generator v1.0.0
