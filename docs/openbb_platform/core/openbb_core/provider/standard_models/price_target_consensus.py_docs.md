# File Documentation: price_target_consensus.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/price_target_consensus.py`
- **Size**: 1,444 bytes
- **Lines**: 43
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Price Target Consensus Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class PriceTargetConsensusQueryParams(QueryParams):
    """Price Target Consensus Query."""

    symbol: str | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("symbol", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v):
        """Convert field to uppercase."""
        return v.upper() if v else None


class PriceTargetConsensusData(Data):
    """Price Target Consensus Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="The company name")
    target_high: float | None = Field(
        default=None, description="High target of the price target consensus."
    )
    target_low: float | None = Field(
        default=None, description="Low target of the price target consensus."
    )
    target_consensus: float | None = Field(
        default=None, description="Consensus target of the price target consensus."
    )
    target_median: float | None = Field(
        default=None, description="Median target of the price target consensus."
    )

```



---

## High-Level Overview

This is a **python** file named `price_target_consensus.py`.

**Python Module**

- **Classes** (2): PriceTargetConsensusQueryParams, PriceTargetConsensusData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`PriceTargetConsensusQueryParams`**(QueryParams)
- **`PriceTargetConsensusData`**(Data)

#### Functions

- **`to_upper(cls, v)`**

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.550139Z
**Generator**: World's Best Repo Book Generator v1.0
