# Documentation: openbb_platform/core/openbb_core/provider/standard_models/tmc.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/tmc.py`
- **Size**: 1,313 characters, 45 lines
- **Words**: 115
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Treasury Constant Maturity Model."""

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


class TreasuryConstantMaturityQueryParams(QueryParams):
    """Treasury Constant Maturity Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    maturity: Literal["3m", "2y"] | None = Field(
        default="3m",
        description="The maturity",
    )

    @field_validator("maturity", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class TreasuryConstantMaturityData(Data):
    """Treasury Constant Maturity Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="TreasuryConstantMaturity Rate.")

```

## High-Level Overview

Treasury Constant Maturity Model.

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


class TreasuryConstantMaturityQueryParams(QueryParams):
Treasury Constant Maturity Query.
Convert field to lowercase.
return v.lower() if v else v

## Detailed Structure

### Python File Structure

**Classes** (2):
`TreasuryConstantMaturityQueryParams`, `TreasuryConstantMaturityData`

**Functions** (1):
`to_lower`

**Imports** (10):
`datetime`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `TreasuryConstantMaturityQueryParams`**: Treasury Constant Maturity Query.

**Class `TreasuryConstantMaturityData`**: Treasury Constant Maturity Data.

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
- Generated: 2025-11-18T07:54:35.750351
- Generator: World's Best Repo Book Generator v1.0.0
