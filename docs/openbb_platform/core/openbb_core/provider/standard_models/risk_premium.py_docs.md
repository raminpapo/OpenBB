# File Documentation: risk_premium.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/risk_premium.py`
- **Size**: 774 bytes
- **Lines**: 23
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `risk_premium.py`.

**Python Module**

- **Classes** (2): RiskPremiumQueryParams, RiskPremiumData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`RiskPremiumQueryParams`**(QueryParams)
- **`RiskPremiumData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.561302Z
**Generator**: World's Best Repo Book Generator v1.0
