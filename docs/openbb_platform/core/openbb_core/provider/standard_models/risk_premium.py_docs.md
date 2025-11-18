# Documentation: openbb_platform/core/openbb_core/provider/standard_models/risk_premium.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/risk_premium.py`
- **Size**: 774 characters, 23 lines
- **Words**: 69
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Risk Premium Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field, NonNegativeFloat, PositiveFloat


class RiskPremiumQueryParams(QueryParams):
    """Risk Premium Query."""


class RiskPremiumData(Data):
    """Risk Premium Data."""

    country: str = Field(description="Market country.")
    continent: str | None = Field(default=None, description="Continent of the country.")
    total_equity_risk_premium: PositiveFloat | None = Field(
        default=None, description="Total equity risk premium for the country."
    )
    country_risk_premium: NonNegativeFloat | None = Field(
        default=None, description="Country-specific risk premium."
    )

```

## High-Level Overview

Risk Premium Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field, NonNegativeFloat, PositiveFloat


class RiskPremiumQueryParams(QueryParams):
Risk Premium Query.
Risk Premium Data.

country: str = Field(description="Market country.")
continent: str | None = Field(default=None, description="Continent of the country.")
total_equity_risk_premium: PositiveFloat | None = Field(
default=None, description="Total equity risk premium for the country."
)
country_risk_premium: NonNegativeFloat | None = Field(
default=None, description="Country-specific risk premium."
)


## Detailed Structure

### Python File Structure

**Classes** (2):
`RiskPremiumQueryParams`, `RiskPremiumData`

**Functions** (0):
None

**Imports** (6):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `pydantic`, `Field`


## Key Components

**Class `RiskPremiumQueryParams`**: Risk Premium Query.

**Class `RiskPremiumData`**: Risk Premium Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.728038
- Generator: World's Best Repo Book Generator v1.0.0
