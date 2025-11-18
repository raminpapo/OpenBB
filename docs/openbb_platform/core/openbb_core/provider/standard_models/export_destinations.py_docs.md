# Documentation: openbb_platform/core/openbb_core/provider/standard_models/export_destinations.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/export_destinations.py`
- **Size**: 826 characters, 28 lines
- **Words**: 66
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Export Destinations Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class ExportDestinationsQueryParams(QueryParams):
    """Export Destinations Query."""

    country: str = Field(description=QUERY_DESCRIPTIONS.get("country", ""))


class ExportDestinationsData(Data):
    """Export Destinations Data."""

    origin_country: str = Field(
        description="The country of origin.",
    )
    destination_country: str = Field(
        description="The destination country.",
    )
    value: float | int = Field(
        description="The value of the export.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )

```

## High-Level Overview

Export Destinations Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class ExportDestinationsQueryParams(QueryParams):
Export Destinations Query.
Export Destinations Data.

origin_country: str = Field(
description="The country of origin.",
)
destination_country: str = Field(
description="The destination country.",
)
value: float | int = Field(
description="The value of the export.",

## Detailed Structure

### Python File Structure

**Classes** (2):
`ExportDestinationsQueryParams`, `ExportDestinationsData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `ExportDestinationsQueryParams`**: Export Destinations Query.

**Class `ExportDestinationsData`**: Export Destinations Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.627120
- Generator: World's Best Repo Book Generator v1.0.0
