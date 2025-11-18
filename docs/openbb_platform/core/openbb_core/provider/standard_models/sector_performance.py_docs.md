# Documentation: openbb_platform/core/openbb_core/provider/standard_models/sector_performance.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/sector_performance.py`
- **Size**: 493 characters, 17 lines
- **Words**: 43
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Sector Performance Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class SectorPerformanceQueryParams(QueryParams):
    """Sector Performance Query."""


class SectorPerformanceData(Data):
    """Sector Performance Data."""

    sector: str = Field(description="The name of the sector.")
    change_percent: float = Field(description="The change in percent from open.")

```

## High-Level Overview

Sector Performance Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class SectorPerformanceQueryParams(QueryParams):
Sector Performance Query.
Sector Performance Data.

sector: str = Field(description="The name of the sector.")
change_percent: float = Field(description="The change in percent from open.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`SectorPerformanceQueryParams`, `SectorPerformanceData`

**Functions** (0):
None

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `pydantic`, `Field`, `open.`


## Key Components

**Class `SectorPerformanceQueryParams`**: Sector Performance Query.

**Class `SectorPerformanceData`**: Sector Performance Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.732542
- Generator: World's Best Repo Book Generator v1.0.0
