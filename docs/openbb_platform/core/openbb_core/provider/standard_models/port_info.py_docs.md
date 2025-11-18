# Documentation: openbb_platform/core/openbb_core/provider/standard_models/port_info.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/port_info.py`
- **Size**: 410 characters, 16 lines
- **Words**: 38
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Port information and metadata."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class PortInfoQueryParams(QueryParams):
    """Port Information Query."""


class PortInfoData(Data):
    """Port Information Data."""

    port_code: str = Field(description="Unique ID assigned to the port by the source.")

```

## High-Level Overview

Port information and metadata.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class PortInfoQueryParams(QueryParams):
Port Information Query.
Port Information Data.

port_code: str = Field(description="Unique ID assigned to the port by the source.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`PortInfoQueryParams`, `PortInfoData`

**Functions** (0):
None

**Imports** (6):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `pydantic`, `Field`


## Key Components

**Class `PortInfoQueryParams`**: Port Information Query.

**Class `PortInfoData`**: Port Information Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.714602
- Generator: World's Best Repo Book Generator v1.0.0
