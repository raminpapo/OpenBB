# Documentation: openbb_platform/core/openbb_core/provider/standard_models/key_executives.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/key_executives.py`
- **Size**: 1,185 characters, 32 lines
- **Words**: 114
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Key Executives Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class KeyExecutivesQueryParams(QueryParams):
    """Key Executives Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class KeyExecutivesData(Data):
    """Key Executives Data."""

    title: str = Field(description="Designation of the key executive.")
    name: str = Field(description="Name of the key executive.")
    pay: int | None = Field(default=None, description="Pay of the key executive.")
    currency_pay: str | None = Field(default=None, description="Currency of the pay.")
    gender: str | None = Field(default=None, description="Gender of the key executive.")
    year_born: int | None = Field(
        default=None, description="Birth year of the key executive."
    )

```

## High-Level Overview

Key Executives Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class KeyExecutivesQueryParams(QueryParams):
Key Executives Query.
Convert field to uppercase.
return v.upper()


class KeyExecutivesData(Data):
Key Executives Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`KeyExecutivesQueryParams`, `KeyExecutivesData`

**Functions** (1):
`to_upper`

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `KeyExecutivesQueryParams`**: Key Executives Query.

**Class `KeyExecutivesData`**: Key Executives Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.685890
- Generator: World's Best Repo Book Generator v1.0.0
