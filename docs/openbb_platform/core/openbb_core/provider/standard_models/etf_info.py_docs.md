# Documentation: openbb_platform/core/openbb_core/provider/standard_models/etf_info.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_info.py`
- **Size**: 1,303 characters, 40 lines
- **Words**: 134
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ETF Info Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfInfoQueryParams(QueryParams):
    """ETF Info Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfInfoData(Data):
    """ETF Info Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + " (ETF)")
    name: str | None = Field(description="Name of the ETF.")
    issuer: str | None = Field(default=None, description="Issuer of the ETF.")
    domicile: str | None = Field(default=None, description="Domicile of the ETF.")
    website: str | None = Field(default=None, description="Website of the ETF.")
    description: str | None = Field(
        default=None, description="Description of the fund."
    )
    inception_date: dateType | None = Field(
        default=None, description="Inception date of the ETF."
    )

```

## High-Level Overview

ETF Info Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfInfoQueryParams(QueryParams):
ETF Info Query.
Convert field to uppercase.
return v.upper()


class EtfInfoData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`EtfInfoQueryParams`, `EtfInfoData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EtfInfoQueryParams`**: ETF Info Query.

**Class `EtfInfoData`**: ETF Info Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.619402
- Generator: World's Best Repo Book Generator v1.0.0
