# File Documentation: undervalued_large_caps.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/undervalued_large_caps.py`
- **Size**: 3,166 bytes
- **Lines**: 97
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Yahoo Finance Asset Undervalued Large Caps Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_performance import (
    EquityPerformanceQueryParams,
)
from openbb_yfinance.utils.references import YFPredefinedScreenerData
from pydantic import Field


class YFUndervaluedLargeCapsQueryParams(EquityPerformanceQueryParams):
    """Yahoo Finance Undervalued Large Caps Query.

    Source: https://finance.yahoo.com/screener/predefined/undervalued_large_caps
    """

    limit: int | None = Field(
        default=200,
        description="Limit the number of results.",
    )


class YFUndervaluedLargeCapsData(YFPredefinedScreenerData):
    """Yahoo Finance Undervalued Large Caps Data."""


class YFUndervaluedLargeCapsFetcher(
    Fetcher[YFUndervaluedLargeCapsQueryParams, list[YFUndervaluedLargeCapsData]]
):
    """Yahoo Finance Undervalued Large Caps Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFUndervaluedLargeCapsQueryParams:
        """Transform query params."""
        return YFUndervaluedLargeCapsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFUndervaluedLargeCapsQueryParams,
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
                    {"operator": "gt", "operands": ["intradaymarketcap", 10000000000]},
                    {
                        "operator": "or",
                        "operands": [
                            {"operator": "eq", "operands": ["exchange", "NMS"]},
                            {"operator": "eq", "operands": ["exchange", "NYQ"]},
                        ],
                    },
                    {
                        "operator": "btwn",
                        "operands": ["peratio.lasttwelvemonths", 0, 20],
                    },
                    {"operator": "lt", "operands": ["pegratio_5y", 1]},
                    {"operator": "gte", "operands": ["epsgrowth.lasttwelvemonths", 25]},
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
    ) -> list[YFUndervaluedLargeCapsData]:
        """Transform data."""
        return [
            YFUndervaluedLargeCapsData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: x["regularMarketChangePercent"],
                reverse=query.sort == "desc",
            )
        ]

```



---

## High-Level Overview

This is a **python** file named `undervalued_large_caps.py`.

**Python Module**

- **Classes** (3): YFUndervaluedLargeCapsQueryParams, YFUndervaluedLargeCapsData, YFUndervaluedLargeCapsFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFUndervaluedLargeCapsQueryParams`**(EquityPerformanceQueryParams)
- **`YFUndervaluedLargeCapsData`**(YFPredefinedScreenerData)
- **`YFUndervaluedLargeCapsFetcher`**(
    Fetcher[YFUndervaluedLargeCapsQueryParams, list[YFUndervaluedLargeCapsData]]
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

**Generated**: 2025-11-19T02:16:55.204116Z
**Generator**: World's Best Repo Book Generator v1.0
