# Documentation: openbb_platform/core/openbb_core/provider/standard_models/historical_attributes.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/historical_attributes.py`
- **Size**: 2,442 characters, 65 lines
- **Words**: 222
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Historical Attributes Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalAttributesQueryParams(QueryParams):
    """Historical Attributes Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol"))
    tag: str = Field(description="Intrinio data tag ID or code.")
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )
    frequency: Literal["daily", "weekly", "monthly", "quarterly", "yearly"] | None = (
        Field(default="yearly", description=QUERY_DESCRIPTIONS.get("frequency"))
    )
    limit: int | None = Field(default=1000, description=QUERY_DESCRIPTIONS.get("limit"))
    tag_type: str | None = Field(
        default=None, description="Filter by type, when applicable."
    )
    sort: Literal["asc", "desc"] | None = Field(
        default="desc", description="Sort order."
    )

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

    @field_validator("frequency", "sort", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class HistoricalAttributesData(Data):
    """Historical Attributes Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol"))
    tag: str | None = Field(default=None, description="Tag name for the fetched data.")
    value: float | None = Field(default=None, description="The value of the data.")

```

## High-Level Overview

Historical Attributes Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalAttributesQueryParams(QueryParams):
Historical Attributes Query.
Accept a comma-separated string or list of tags.
if isinstance(v, str):
return v.lower()
return ",".join([tag.lower() for tag in list(v)])

## Detailed Structure

### Python File Structure

**Classes** (2):
`HistoricalAttributesQueryParams`, `HistoricalAttributesData`

**Functions** (3):
`multiple_tags`, `to_upper`, `to_lower`

**Imports** (11):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `HistoricalAttributesQueryParams`**: Historical Attributes Query.

**Class `HistoricalAttributesData`**: Historical Attributes Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.659337
- Generator: World's Best Repo Book Generator v1.0.0
