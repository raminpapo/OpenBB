# Documentation: openbb_platform/core/openbb_core/provider/standard_models/etf_sectors.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_sectors.py`
- **Size**: 1,043 characters, 35 lines
- **Words**: 92
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ETF Sectors Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfSectorsQueryParams(QueryParams):
    """ETF Sectors Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfSectorsData(Data):
    """ETF Sectors Data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    sector: str = Field(description="Sector of exposure.")
    weight: float = Field(
        description="Sector exposure for the ETF as a percent of total assets.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```

## High-Level Overview

ETF Sectors Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfSectorsQueryParams(QueryParams):
ETF Sectors Query.
Convert field to uppercase.
return v.upper()


class EtfSectorsData(Data):
ETF Sectors Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`EtfSectorsQueryParams`, `EtfSectorsData`

**Functions** (1):
`to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EtfSectorsQueryParams`**: ETF Sectors Query.

**Class `EtfSectorsData`**: ETF Sectors Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.623173
- Generator: World's Best Repo Book Generator v1.0.0
