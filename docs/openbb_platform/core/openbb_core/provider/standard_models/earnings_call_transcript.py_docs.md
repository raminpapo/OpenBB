# Documentation: openbb_platform/core/openbb_core/provider/standard_models/earnings_call_transcript.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/earnings_call_transcript.py`
- **Size**: 1,468 characters, 41 lines
- **Words**: 138
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Earnings Call Transcript Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EarningsCallTranscriptQueryParams(QueryParams):
    """Earnings Call Transcript rating Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    year: int | None = Field(
        default=None, description="Year of the earnings call transcript."
    )
    quarter: Literal[1, 2, 3, 4] | None = Field(
        default=None, description="Quarterly period of the earnings call transcript."
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EarningsCallTranscriptData(Data):
    """Earnings Call Transcript Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    year: int = Field(description="Year of the earnings call transcript.")
    quarter: str = Field(description="Quarter of the earnings call transcript.")
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    content: str = Field(description="Content of the earnings call transcript.")

```

## High-Level Overview

Earnings Call Transcript Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EarningsCallTranscriptQueryParams(QueryParams):
Earnings Call Transcript rating Query.
Convert field to uppercase.
return v.upper()



## Detailed Structure

### Python File Structure

**Classes** (2):
`EarningsCallTranscriptQueryParams`, `EarningsCallTranscriptData`

**Functions** (1):
`to_upper`

**Imports** (11):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EarningsCallTranscriptQueryParams`**: Earnings Call Transcript rating Query.

**Class `EarningsCallTranscriptData`**: Earnings Call Transcript Data.

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
- Generated: 2025-11-18T07:54:35.584877
- Generator: World's Best Repo Book Generator v1.0.0
