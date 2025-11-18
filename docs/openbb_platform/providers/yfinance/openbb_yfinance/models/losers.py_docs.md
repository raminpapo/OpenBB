# Documentation: openbb_platform/providers/yfinance/openbb_yfinance/models/losers.py

## File Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/losers.py`
- **Size**: 2,769 characters, 91 lines
- **Words**: 196
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Yahoo Finance Top Losers Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_performance import (
    EquityPerformanceQueryParams,
)
from openbb_yfinance.utils.references import YFPredefinedScreenerData
from pydantic import Field


class YFLosersQueryParams(EquityPerformanceQueryParams):
    """Yahoo Finance Losers Query.

    Source: https://finance.yahoo.com/screener/predefined/day_losers
    """

    limit: int | None = Field(
        default=200,
        description="Limit the number of results.",
    )


class YFLosersData(YFPredefinedScreenerData):
    """Yahoo Finance Losers Data."""


class YFLosersFetcher(Fetcher[YFLosersQueryParams, list[YFLosersData]]):
    """Yahoo Finance Losers Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFLosersQueryParams:
        """Transform query params."""
        return YFLosersQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFLosersQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from YF."""
        # pylint: disable=import-outside-toplevel
        from openbb_yfinance.utils.helpers import get_custom_screener

        body = {
            "offset": 0,
            "size": 250,
            "sortField": "percentchange",
            "sortType": "asc",
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
                    {"operator": "gt", "operands": ["percentchange", -3]},
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
    ) -> list[YFLosersData]:
        """Transform data."""
        return [
            YFLosersData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: x["regularMarketChangePercent"],
                reverse=query.sort == "desc",
            )
        ]

```

## High-Level Overview

Yahoo Finance Top Losers Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_performance import (
EquityPerformanceQueryParams,
)
from openbb_yfinance.utils.references import YFPredefinedScreenerData
from pydantic import Field


class YFLosersQueryParams(EquityPerformanceQueryParams):
Yahoo Finance Losers Query.


limit: int | None = Field(
default=200,

## Detailed Structure

### Python File Structure

**Classes** (3):
`YFLosersQueryParams`, `YFLosersData`, `YFLosersFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (12):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.equity_performance`, `openbb_yfinance.utils.references`, `YFPredefinedScreenerData`, `pydantic`, `Field`, `YF.`, `openbb_yfinance.utils.helpers`, `get_custom_screener`


## Key Components

**Class `YFLosersQueryParams`**: Yahoo Finance Losers Query.

    Source: https://finance.yahoo.com/screener/predefined/day_losers

**Class `YFLosersData`**: Yahoo Finance Losers Data.

**Class `YFLosersFetcher`**: Yahoo Finance Losers Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_performance`
- `openbb_yfinance.utils.references`
- `pydantic`
- `openbb_yfinance.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:43.588093
- Generator: World's Best Repo Book Generator v1.0.0
