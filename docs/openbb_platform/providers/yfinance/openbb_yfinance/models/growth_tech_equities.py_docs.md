# File Documentation: growth_tech_equities.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/growth_tech_equities.py`
- **Size**: 3,198 bytes
- **Lines**: 97
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Yahoo Finance Asset Performance Growth Tech Equities Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_performance import (
    EquityPerformanceQueryParams,
)
from openbb_yfinance.utils.references import YFPredefinedScreenerData
from pydantic import Field


class YFGrowthTechEquitiesQueryParams(EquityPerformanceQueryParams):
    """Yahoo Finance Growth Tech Stocks Query.

    Source: https://finance.yahoo.com/screener/predefined/growth_technology_stocks
    """

    limit: int | None = Field(
        default=200,
        description="Limit the number of results.",
    )


class YFGrowthTechEquitiesData(YFPredefinedScreenerData):
    """Yahoo Finance Growth Tech Stocks Data."""


class YFGrowthTechEquitiesFetcher(
    Fetcher[YFGrowthTechEquitiesQueryParams, list[YFGrowthTechEquitiesData]]
):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFGrowthTechEquitiesQueryParams:
        """Transform query params."""
        return YFGrowthTechEquitiesQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFGrowthTechEquitiesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from YF."""
        # pylint: disable=import-outside-toplevel
        from openbb_yfinance.utils.helpers import get_custom_screener

        body = {
            "offset": 0,
            "size": 250,
            "sortField": "eodvolume",
            "sortType": "desc",
            "quoteType": "equity",
            "query": {
                "operator": "and",
                "operands": [
                    {"operator": "gt", "operands": ["intradaymarketcap", 500000000]},
                    {
                        "operator": "or",
                        "operands": [
                            {"operator": "eq", "operands": ["exchange", "NMS"]},
                            {"operator": "eq", "operands": ["exchange", "NYQ"]},
                        ],
                    },
                    {
                        "operator": "gte",
                        "operands": ["quarterlyrevenuegrowth.quarterly", 25],
                    },
                    {"operator": "gte", "operands": ["epsgrowth.lasttwelvemonths", 25]},
                    {"operator": "eq", "operands": ["sector", "Technology"]},
                ],
            },
            "userId": "",
            "userIdType": "guid",
        }

        return await get_custom_screener(body=body, limit=query.limit)

    @staticmethod
    def transform_data(
        query: EquityPerformanceQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFGrowthTechEquitiesData]:
        """Transform data."""
        return [
            YFGrowthTechEquitiesData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: x["regularMarketChangePercent"],
                reverse=query.sort == "desc",
            )
        ]

```



---

## High-Level Overview

This is a **python** file named `growth_tech_equities.py`.

**Python Module**

- **Classes** (3): YFGrowthTechEquitiesQueryParams, YFGrowthTechEquitiesData, YFGrowthTechEquitiesFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFGrowthTechEquitiesQueryParams`**(EquityPerformanceQueryParams)
- **`YFGrowthTechEquitiesData`**(YFPredefinedScreenerData)
- **`YFGrowthTechEquitiesFetcher`**(
    Fetcher[YFGrowthTechEquitiesQueryParams, list[YFGrowthTechEquitiesData]]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Field`
- `YFPredefinedScreenerData`
- `get_custom_screener`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_performance`
- `openbb_yfinance.utils.helpers`
- `openbb_yfinance.utils.references`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.182024Z
**Generator**: World's Best Repo Book Generator v1.0
