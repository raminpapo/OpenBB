# Documentation: openbb_platform/core/openbb_core/provider/standard_models/institutional_ownership.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/institutional_ownership.py`
- **Size**: 1,054 characters, 35 lines
- **Words**: 81
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Institutional Ownership Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class InstitutionalOwnershipQueryParams(QueryParams):
    """Institutional Ownership Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class InstitutionalOwnershipData(Data):
    """Institutional Ownership Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    cik: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("cik", ""),
    )
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

```

## High-Level Overview

Institutional Ownership Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class InstitutionalOwnershipQueryParams(QueryParams):
Institutional Ownership Query.
Convert field to uppercase.
return v.upper()


class InstitutionalOwnershipData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`InstitutionalOwnershipQueryParams`, `InstitutionalOwnershipData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `InstitutionalOwnershipQueryParams`**: Institutional Ownership Query.

**Class `InstitutionalOwnershipData`**: Institutional Ownership Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.683456
- Generator: World's Best Repo Book Generator v1.0.0
