# Documentation: openbb_platform/core/openbb_core/provider/standard_models/latest_attributes.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/latest_attributes.py`
- **Size**: 1,371 characters, 41 lines
- **Words**: 125
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Latest Attributes Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class LatestAttributesQueryParams(QueryParams):
    """Latest Attributes Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol"))
    tag: str = Field(description="Intrinio data tag ID or code.")

    @field_validator("tag", mode="before", check_fields=False)
    @classmethod
    def multiple_tags(cls, v: str | list[str] | set[str]):
        """Accept a comma-separated string or list of tags."""
        if isinstance(v, str):
            return v.lower()
        return ",".join([tag.lower() for tag in list(v)])

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class LatestAttributesData(Data):
    """Latest Attributes Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol"))
    tag: str | None = Field(default=None, description="Tag name for the fetched data.")
    value: str | float | None = Field(
        default=None, description="The value of the data."
    )

```

## High-Level Overview

Latest Attributes Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class LatestAttributesQueryParams(QueryParams):
Latest Attributes Query.
Accept a comma-separated string or list of tags.
if isinstance(v, str):
return v.lower()
return ",".join([tag.lower() for tag in list(v)])

@field_validator("symbol", mode="before", check_fields=False)
@classmethod

## Detailed Structure

### Python File Structure

**Classes** (2):
`LatestAttributesQueryParams`, `LatestAttributesData`

**Functions** (2):
`multiple_tags`, `to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `LatestAttributesQueryParams`**: Latest Attributes Query.

**Class `LatestAttributesData`**: Latest Attributes Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.688386
- Generator: World's Best Repo Book Generator v1.0.0
