# Documentation: openbb_platform/core/openbb_core/provider/standard_models/maritime_chokepoint_info.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/maritime_chokepoint_info.py`
- **Size**: 491 characters, 18 lines
- **Words**: 39
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Maritime chokepoint information and metadata."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class MaritimeChokePointInfoQueryParams(QueryParams):
    """MaritimeChokepointInfo Query."""


class MaritimeChokePointInfoData(Data):
    """MaritimeChokepointInfo Data."""

    chokepoint_code: str = Field(
        description="Unique ID assigned to the chokepoint by the source."
    )

```

## High-Level Overview

Maritime chokepoint information and metadata.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class MaritimeChokePointInfoQueryParams(QueryParams):
MaritimeChokepointInfo Query.
MaritimeChokepointInfo Data.

chokepoint_code: str = Field(
description="Unique ID assigned to the chokepoint by the source."
)


## Detailed Structure

### Python File Structure

**Classes** (2):
`MaritimeChokePointInfoQueryParams`, `MaritimeChokePointInfoData`

**Functions** (0):
None

**Imports** (6):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `pydantic`, `Field`


## Key Components

**Class `MaritimeChokePointInfoQueryParams`**: MaritimeChokepointInfo Query.

**Class `MaritimeChokePointInfoData`**: MaritimeChokepointInfo Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.694538
- Generator: World's Best Repo Book Generator v1.0.0
