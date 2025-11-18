# Documentation: openbb_platform/core/openbb_core/provider/standard_models/ecb_interest_rates.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/ecb_interest_rates.py`
- **Size**: 1,426 characters, 45 lines
- **Words**: 127
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""European Central Bank Interest Rates Standard Model."""

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


class EuropeanCentralBankInterestRatesParams(QueryParams):
    """European Central Bank Interest Rates Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    interest_rate_type: Literal["deposit", "lending", "refinancing"] = Field(
        default="lending",
        description="The type of interest rate.",
    )

    @field_validator("interest_rate_type", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class EuropeanCentralBankInterestRatesData(Data):
    """European Central Bank Interest Rates Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="European Central Bank Interest Rate.")

```

## High-Level Overview

European Central Bank Interest Rates Standard Model.

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


class EuropeanCentralBankInterestRatesParams(QueryParams):
European Central Bank Interest Rates Query.
Convert field to lowercase.
return v.lower() if v else v

## Detailed Structure

### Python File Structure

**Classes** (2):
`EuropeanCentralBankInterestRatesParams`, `EuropeanCentralBankInterestRatesData`

**Functions** (1):
`to_lower`

**Imports** (10):
`datetime`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EuropeanCentralBankInterestRatesParams`**: European Central Bank Interest Rates Query.

**Class `EuropeanCentralBankInterestRatesData`**: European Central Bank Interest Rates Data.

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
- Generated: 2025-11-18T07:54:35.586303
- Generator: World's Best Repo Book Generator v1.0.0
