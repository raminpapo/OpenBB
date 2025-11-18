# Documentation: openbb_platform/core/openbb_core/provider/standard_models/ffrmc.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/ffrmc.py`
- **Size**: 1,396 characters, 45 lines
- **Words**: 125
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Selected Treasury Constant Maturity Standard Model."""

from datetime import (
    date as dateType,
)
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class SelectedTreasuryConstantMaturityQueryParams(QueryParams):
    """Selected Treasury Constant Maturity Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    maturity: Literal["10y", "5y", "1y", "6m", "3m"] | None = Field(
        default="10y",
        description="The maturity",
    )

    @field_validator("maturity", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class SelectedTreasuryConstantMaturityData(Data):
    """Selected Treasury Constant Maturity Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="Selected Treasury Constant Maturity Rate.")

```

## High-Level Overview

Selected Treasury Constant Maturity Standard Model.

from datetime import (
date as dateType,
)
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class SelectedTreasuryConstantMaturityQueryParams(QueryParams):
Selected Treasury Constant Maturity Query.
Convert field to lowercase.
return v.lower() if v else v

## Detailed Structure

### Python File Structure

**Classes** (2):
`SelectedTreasuryConstantMaturityQueryParams`, `SelectedTreasuryConstantMaturityData`

**Functions** (1):
`to_lower`

**Imports** (10):
`datetime`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `SelectedTreasuryConstantMaturityQueryParams`**: Selected Treasury Constant Maturity Query.

**Class `SelectedTreasuryConstantMaturityData`**: Selected Treasury Constant Maturity Data.

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
- Generated: 2025-11-18T07:54:35.630779
- Generator: World's Best Repo Book Generator v1.0.0
