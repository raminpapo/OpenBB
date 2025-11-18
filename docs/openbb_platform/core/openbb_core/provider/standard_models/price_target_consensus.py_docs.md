# Documentation: openbb_platform/core/openbb_core/provider/standard_models/price_target_consensus.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/price_target_consensus.py`
- **Size**: 1,444 characters, 43 lines
- **Words**: 138
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Price Target Consensus Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class PriceTargetConsensusQueryParams(QueryParams):
Price Target Consensus Query.
Convert field to uppercase.
return v.upper() if v else None


class PriceTargetConsensusData(Data):
Price Target Consensus Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`PriceTargetConsensusQueryParams`, `PriceTargetConsensusData`

**Functions** (1):
`to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `PriceTargetConsensusQueryParams`**: Price Target Consensus Query.

**Class `PriceTargetConsensusData`**: Price Target Consensus Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.718073
- Generator: World's Best Repo Book Generator v1.0.0
