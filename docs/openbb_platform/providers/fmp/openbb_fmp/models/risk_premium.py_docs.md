# File Documentation: risk_premium.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/risk_premium.py`
- **Size**: 1,700 bytes
- **Lines**: 59
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP Risk Premium Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.risk_premium import (
    RiskPremiumData,
    RiskPremiumQueryParams,
)


class FMPRiskPremiumQueryParams(RiskPremiumQueryParams):
    """FMP Risk Premium Query.

    Source: https://site.financialmodelingprep.com/developer/docs#market-risk-premium
    """


class FMPRiskPremiumData(RiskPremiumData):
    """FMP Risk Premium Data."""


class FMPRiskPremiumFetcher(
    Fetcher[
        FMPRiskPremiumQueryParams,
        list[FMPRiskPremiumData],
    ]
):
    """FMP Risk Premium Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPRiskPremiumQueryParams:
        """Transform the query params."""
        return FMPRiskPremiumQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPRiskPremiumQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        url = f"https://financialmodelingprep.com/stable/market-risk-premium?apikey={api_key}"

        return await get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPRiskPremiumQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPRiskPremiumData]:
        """Return the transformed data."""
        return [FMPRiskPremiumData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `risk_premium.py`.

**Python Module**

- **Classes** (3): FMPRiskPremiumQueryParams, FMPRiskPremiumData, FMPRiskPremiumFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPRiskPremiumQueryParams`**(RiskPremiumQueryParams)
- **`FMPRiskPremiumData`**(RiskPremiumData)
- **`FMPRiskPremiumFetcher`**(
    Fetcher[
        FMPRiskPremiumQueryParams,
        list[FMPRiskPremiumData],
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `get_data_many`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.risk_premium`
- `openbb_fmp.utils.helpers`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.691828Z
**Generator**: World's Best Repo Book Generator v1.0
