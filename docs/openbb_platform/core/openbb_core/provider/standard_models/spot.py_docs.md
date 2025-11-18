# Documentation: openbb_platform/core/openbb_core/provider/standard_models/spot.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/spot.py`
- **Size**: 1,293 characters, 45 lines
- **Words**: 118
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Spot Rate Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class SpotRateQueryParams(QueryParams):
    """Spot Rate Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    maturity: float | str = Field(default=10.0, description="Maturities in years.")
    category: str = Field(
        default="spot_rate",
        description="Rate category. Options: spot_rate, par_yield.",
    )

    @field_validator("category", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class SpotRateData(Data):
    """Spot Rate Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="Spot Rate.")

```

## High-Level Overview

Spot Rate Standard Model.

from datetime import (
date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class SpotRateQueryParams(QueryParams):
Spot Rate Query.
Convert field to lowercase.
return v.lower() if v else v


## Detailed Structure

### Python File Structure

**Classes** (2):
`SpotRateQueryParams`, `SpotRateData`

**Functions** (1):
`to_lower`

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `SpotRateQueryParams`**: Spot Rate Query.

**Class `SpotRateData`**: Spot Rate Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.743978
- Generator: World's Best Repo Book Generator v1.0.0
