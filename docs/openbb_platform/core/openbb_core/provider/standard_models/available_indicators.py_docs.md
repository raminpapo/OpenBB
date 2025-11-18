# Documentation: openbb_platform/core/openbb_core/provider/standard_models/available_indicators.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/available_indicators.py`
- **Size**: 1,329 characters, 41 lines
- **Words**: 141
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Available Indicators Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class AvailableIndicesQueryParams(QueryParams):
    """Available Indicators Query."""


class AvailableIndicatorsData(Data):
    """Available Indicators Data.

    Returns the list of available economic indicators from a provider.
    """

    symbol_root: str | None = Field(
        default=None, description="The root symbol representing the indicator."
    )
    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", "")
        + " The root symbol with additional codes.",
    )
    country: str | None = Field(
        default=None,
        description="The name of the country, region, or entity represented by the symbol.",
    )
    iso: str | None = Field(
        default=None,
        description="The ISO code of the country, region, or entity represented by the symbol.",
    )
    description: str | None = Field(
        default=None, description="The description of the indicator."
    )
    frequency: str | None = Field(
        default=None, description="The frequency of the indicator data."
    )

```

## High-Level Overview

Available Indicators Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class AvailableIndicesQueryParams(QueryParams):
Available Indicators Query.
Available Indicators Data.

Returns the list of available economic indicators from a provider.


## Detailed Structure

### Python File Structure

**Classes** (2):
`AvailableIndicesQueryParams`, `AvailableIndicatorsData`

**Functions** (0):
None

**Imports** (9):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`, `a`


## Key Components

**Class `AvailableIndicesQueryParams`**: Available Indicators Query.

**Class `AvailableIndicatorsData`**: Available Indicators Data.

    Returns the list of available economic indicators from a provider.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.527375
- Generator: World's Best Repo Book Generator v1.0.0
