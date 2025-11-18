# Documentation: openbb_platform/core/openbb_core/provider/standard_models/dwpcr_rates.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/dwpcr_rates.py`
- **Size**: 989 characters, 34 lines
- **Words**: 85
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Discount Window Primary Credit Rate Standard Model."""

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


class DiscountWindowPrimaryCreditRateParams(QueryParams):
    """Discount Window Primary Credit Rate Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class DiscountWindowPrimaryCreditRateData(Data):
    """Discount Window Primary Credit Rate Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="Discount Window Primary Credit Rate.")

```

## High-Level Overview

Discount Window Primary Credit Rate Standard Model.

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


class DiscountWindowPrimaryCreditRateParams(QueryParams):
Discount Window Primary Credit Rate Query.
Discount Window Primary Credit Rate Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`DiscountWindowPrimaryCreditRateParams`, `DiscountWindowPrimaryCreditRateData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `DiscountWindowPrimaryCreditRateParams`**: Discount Window Primary Credit Rate Query.

**Class `DiscountWindowPrimaryCreditRateData`**: Discount Window Primary Credit Rate Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.583638
- Generator: World's Best Repo Book Generator v1.0.0
