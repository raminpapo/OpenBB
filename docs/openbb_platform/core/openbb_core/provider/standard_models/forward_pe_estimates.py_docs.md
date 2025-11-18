# Documentation: openbb_platform/core/openbb_core/provider/standard_models/forward_pe_estimates.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/forward_pe_estimates.py`
- **Size**: 1,594 characters, 52 lines
- **Words**: 159
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Forward PE Estimates Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ForwardPeEstimatesQueryParams(QueryParams):
    """Forward PE Estimates Query Parameters."""

    symbol: str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS["symbol"],
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v):
        """Convert field to uppercase."""
        return v.upper() if v else None


class ForwardPeEstimatesData(Data):
    """Forward PE Estimates Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="Name of the entity.")
    year1: float | None = Field(
        default=None,
        description="Estimated PE ratio for the next fiscal year.",
    )
    year2: float | None = Field(
        default=None,
        description="Estimated PE ratio two fiscal years from now.",
    )
    year3: float | None = Field(
        default=None,
        description="Estimated PE ratio three fiscal years from now.",
    )
    year4: float | None = Field(
        default=None,
        description="Estimated PE ratio four fiscal years from now.",
    )
    year5: float | None = Field(
        default=None,
        description="Estimated PE ratio five fiscal years from now.",
    )

```

## High-Level Overview

Forward PE Estimates Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ForwardPeEstimatesQueryParams(QueryParams):
Forward PE Estimates Query Parameters.
Convert field to uppercase.
return v.upper() if v else None


class ForwardPeEstimatesData(Data):
Forward PE Estimates Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`ForwardPeEstimatesQueryParams`, `ForwardPeEstimatesData`

**Functions** (1):
`to_upper`

**Imports** (11):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`, `now.`, `now.`, `now.`, `now.`


## Key Components

**Class `ForwardPeEstimatesQueryParams`**: Forward PE Estimates Query Parameters.

**Class `ForwardPeEstimatesData`**: Forward PE Estimates Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.639887
- Generator: World's Best Repo Book Generator v1.0.0
