# File Documentation: equity_nbbo.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_nbbo.py`
- **Size**: 1,391 bytes
- **Lines**: 48
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Equity NBBO Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class EquityNBBOQueryParams(QueryParams):
    """Equity NBBO Query."""

    symbol: str = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class EquityNBBOData(Data):
    """Equity NBBO Data."""

    ask_exchange: str = Field(
        description="The exchange ID for the ask.",
    )
    ask: float = Field(
        description="The last ask price.",
    )
    ask_size: int = Field(
        description="""
        The ask size. This represents the number of round lot orders at the given ask price.
        The normal round lot size is 100 shares.
        An ask size of 2 means there are 200 shares available to purchase at the given ask price.
        """,
    )
    bid_size: int = Field(
        description="The bid size in round lots.",
    )
    bid: float = Field(
        description="The last bid price.",
    )
    bid_exchange: str = Field(
        description="The exchange ID for the bid.",
    )

```



---

## High-Level Overview

This is a **python** file named `equity_nbbo.py`.

**Python Module**

- **Classes** (2): EquityNBBOQueryParams, EquityNBBOData
- **Functions** (1): to_upper
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EquityNBBOQueryParams`**(QueryParams)
- **`EquityNBBOData`**(Data)

#### Functions

- **`to_upper(cls, v: str)`**

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QUERY_DESCRIPTIONS`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.422920Z
**Generator**: World's Best Repo Book Generator v1.0
