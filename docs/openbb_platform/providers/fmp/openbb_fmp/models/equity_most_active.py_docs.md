# File Documentation: equity_most_active.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/equity_most_active.py`
- **Size**: 2,330 bytes
- **Lines**: 80
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP Equity Most Active Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_performance import (
    EquityPerformanceData,
    EquityPerformanceQueryParams,
)
from pydantic import Field, field_validator


class FMPEquityActiveQueryParams(EquityPerformanceQueryParams):
    """FMP Most Active Query.

    Source: https://site.financialmodelingprep.com/developer/docs#most-active
    """


class FMPEquityActiveData(EquityPerformanceData):
    """FMP Most Active Data."""

    __alias_dict__ = {
        "percent_change": "changesPercentage",
    }

    exchange: str = Field(
        description="Stock exchange where the security is listed.",
    )

    @field_validator("percent_change", mode="before", check_fields=False)
    @classmethod
    def _normalize_percent(cls, v):
        """Normalize percent change by removing % sign and converting to float."""
        return v / 100 if v else None


class FMPEquityActiveFetcher(
    Fetcher[FMPEquityActiveQueryParams, list[FMPEquityActiveData]]
):
    """FMP EquityActive Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPEquityActiveQueryParams:
        """Transform query params."""
        return FMPEquityActiveQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPEquityActiveQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Get the raw data from the FMP API."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        url = f"https://financialmodelingprep.com/stable/most-actives?apikey={api_key}"

        return await get_data_many(url)

    @staticmethod
    def transform_data(
        query: EquityPerformanceQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[FMPEquityActiveData]:
        """Transform data."""
        return [
            FMPEquityActiveData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: x["changesPercentage"],
                reverse=query.sort == "desc",
            )
        ]

```



---

## High-Level Overview

This is a **python** file named `equity_most_active.py`.

**Python Module**

- **Classes** (3): FMPEquityActiveQueryParams, FMPEquityActiveData, FMPEquityActiveFetcher
- **Functions** (4): _normalize_percent, transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPEquityActiveQueryParams`**(EquityPerformanceQueryParams)
- **`FMPEquityActiveData`**(EquityPerformanceData)
- **`FMPEquityActiveFetcher`**(
    Fetcher[FMPEquityActiveQueryParams, list[FMPEquityActiveData]]
)

#### Functions

- **`_normalize_percent(cls, v)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Field`
- `get_data_many`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_performance`
- `openbb_fmp.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.614675Z
**Generator**: World's Best Repo Book Generator v1.0
