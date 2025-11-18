# Documentation: openbb_platform/core/openbb_core/provider/standard_models/options_unusual.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/options_unusual.py`
- **Size**: 1,035 characters, 35 lines
- **Words**: 90
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Unusual Options Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class OptionsUnusualQueryParams(QueryParams):
    """Unusual Options Query."""

    symbol: str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("symbol", "") + " (the underlying symbol)",
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper() if v else None


class OptionsUnusualData(Data):
    """Unusual Options Data."""

    underlying_symbol: str | None = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "") + " (the underlying symbol)",
        default=None,
    )
    contract_symbol: str = Field(description="Contract symbol for the option.")

```

## High-Level Overview

Unusual Options Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class OptionsUnusualQueryParams(QueryParams):
Unusual Options Query.
Convert field to uppercase.
return v.upper() if v else None


class OptionsUnusualData(Data):
Unusual Options Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`OptionsUnusualQueryParams`, `OptionsUnusualData`

**Functions** (1):
`to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `OptionsUnusualQueryParams`**: Unusual Options Query.

**Class `OptionsUnusualData`**: Unusual Options Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.708950
- Generator: World's Best Repo Book Generator v1.0.0
