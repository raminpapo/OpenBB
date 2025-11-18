# Documentation: openbb_platform/core/openbb_core/provider/standard_models/lbma_fixing.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/lbma_fixing.py`
- **Size**: 2,077 characters, 76 lines
- **Words**: 212
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""LBMA Fixing Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class LbmaFixingQueryParams(QueryParams):
    """
    LBMA Fixing Query.

    Source: https://www.lbma.org.uk/prices-and-data/precious-metal-prices#/table
    """

    asset: Literal["gold", "silver"] = Field(
        description="The metal to get price fixing rates for.",
        default="gold",
    )
    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class LbmaFixingData(Data):
    """LBMA Fixing Data.  Historical fixing prices in USD, GBP and EUR."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    usd_am: float | None = Field(
        default=None,
        description="AM fixing price in USD.",
    )
    usd_pm: float | None = Field(
        default=None,
        description="PM fixing price in USD.",
    )
    gbp_am: float | None = Field(
        default=None,
        description="AM fixing price in GBP.",
    )
    gbp_pm: float | None = Field(
        default=None,
        description="PM fixing price in GBP.",
    )
    euro_am: float | None = Field(
        default=None,
        description="AM fixing price in EUR.",
    )
    euro_pm: float | None = Field(
        default=None,
        description="PM fixing price in EUR.",
    )
    usd: float | None = Field(
        default=None,
        description="Daily fixing price in USD.",
    )
    gbp: float | None = Field(
        default=None,
        description="Daily fixing price in GBP.",
    )
    eur: float | None = Field(
        default=None,
        description="Daily fixing price in EUR.",
    )

```

## High-Level Overview

LBMA Fixing Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class LbmaFixingQueryParams(QueryParams):



asset: Literal["gold", "silver"] = Field(
description="The metal to get price fixing rates for.",

## Detailed Structure

### Python File Structure

**Classes** (2):
`LbmaFixingQueryParams`, `LbmaFixingData`

**Functions** (0):
None

**Imports** (11):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `LbmaFixingQueryParams`**: LBMA Fixing Query.

    Source: https://www.lbma.org.uk/prices-and-data/precious-metal-prices#/table

**Class `LbmaFixingData`**: LBMA Fixing Data.  Historical fixing prices in USD, GBP and EUR.

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
- Generated: 2025-11-18T07:54:35.690798
- Generator: World's Best Repo Book Generator v1.0.0
