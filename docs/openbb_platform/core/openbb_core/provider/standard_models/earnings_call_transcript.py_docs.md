# File Documentation: earnings_call_transcript.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/earnings_call_transcript.py`
- **Size**: 1,468 bytes
- **Lines**: 41
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `earnings_call_transcript.py`.

**Python Module**

- **Classes** (2): EarningsCallTranscriptQueryParams, EarningsCallTranscriptData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EarningsCallTranscriptQueryParams`**(QueryParams)
- **`EarningsCallTranscriptData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `Literal`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.410597Z
**Generator**: World's Best Repo Book Generator v1.0
