# Documentation: openbb_platform/core/openbb_core/provider/standard_models/high_quality_market.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/high_quality_market.py`
- **Size**: 982 characters, 34 lines
- **Words**: 82
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""High Quality Market Corporate Bond Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class HighQualityMarketCorporateBondQueryParams(QueryParams):
    """High Quality Market Corporate Bond Query."""

    date: dateType | str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", ""),
    )


class HighQualityMarketCorporateBondData(Data):
    """High Quality Market Corporate Bond Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float = Field(
        description="Interest rate.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    maturity: str = Field(description="Maturity.")

```

## High-Level Overview

High Quality Market Corporate Bond Standard Model.

from datetime import (
date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class HighQualityMarketCorporateBondQueryParams(QueryParams):
High Quality Market Corporate Bond Query.
High Quality Market Corporate Bond Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`HighQualityMarketCorporateBondQueryParams`, `HighQualityMarketCorporateBondData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `HighQualityMarketCorporateBondQueryParams`**: High Quality Market Corporate Bond Query.

**Class `HighQualityMarketCorporateBondData`**: High Quality Market Corporate Bond Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.657860
- Generator: World's Best Repo Book Generator v1.0.0
