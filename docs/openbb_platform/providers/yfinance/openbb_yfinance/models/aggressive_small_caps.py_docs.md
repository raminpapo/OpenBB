# File Documentation: aggressive_small_caps.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/aggressive_small_caps.py`
- **Size**: 3,119 bytes
- **Lines**: 90
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Yahoo Finance Aggressive Small Caps Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_performance import (
    EquityPerformanceQueryParams,
)
from openbb_yfinance.utils.references import YFPredefinedScreenerData
from pydantic import Field


class YFAggressiveSmallCapsQueryParams(EquityPerformanceQueryParams):
    """Yahoo Finance Aggressive Small Caps Query.

    Source: https://finance.yahoo.com/screener/predefined/aggressive_small_caps
    """

    limit: int | None = Field(
        default=None,
        description="Limit the number of results. Default is all.",
    )


class YFAggressiveSmallCapsData(YFPredefinedScreenerData):
    """Yahoo Finance Aggressive Small Caps Data."""


class YFAggressiveSmallCapsFetcher(
    Fetcher[YFAggressiveSmallCapsQueryParams, list[YFAggressiveSmallCapsData]]
):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFAggressiveSmallCapsQueryParams:
        """Transform query params."""
        return YFAggressiveSmallCapsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFAggressiveSmallCapsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from YF."""
        # pylint: disable=import-outside-toplevel
        from openbb_yfinance.utils.helpers import get_custom_screener

        # The predefined screener doesn't match what yFinance has for the settings. We'll have to create our own.
        body = {
            "offset": 0,
            "size": 250,
            "sortField": "totalrevenues1yrgrowth.lasttwelvemonths",
            "sortType": "desc",
            "quoteType": "equity",
            "query": {
                "operator": "and",
                "operands": [
                    {"operator": "lt", "operands": ["intradaymarketcap", 2000000000]},
                    {
                        "operator": "or",
                        "operands": [
                            {"operator": "eq", "operands": ["exchange", "NMS"]},
                            {"operator": "eq", "operands": ["exchange", "NYQ"]},
                        ],
                    },
                    {"operator": "gt", "operands": ["epsgrowth.lasttwelvemonths", 25]},
                    {"operator": "gt", "operands": ["intradayprice", 5]},
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
    ) -> list[YFAggressiveSmallCapsData]:
        """Transform data."""
        return sorted(
            [YFAggressiveSmallCapsData.model_validate(d) for d in data],
            key=lambda x: x.percent_change,
            reverse=query.sort == "desc",
        )

```



---

## High-Level Overview

This is a **python** file named `aggressive_small_caps.py`.

**Python Module**

- **Classes** (3): YFAggressiveSmallCapsQueryParams, YFAggressiveSmallCapsData, YFAggressiveSmallCapsFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFAggressiveSmallCapsQueryParams`**(EquityPerformanceQueryParams)
- **`YFAggressiveSmallCapsData`**(YFPredefinedScreenerData)
- **`YFAggressiveSmallCapsFetcher`**(
    Fetcher[YFAggressiveSmallCapsQueryParams, list[YFAggressiveSmallCapsData]]
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

**Generated**: 2025-11-19T02:16:55.153883Z
**Generator**: World's Best Repo Book Generator v1.0
