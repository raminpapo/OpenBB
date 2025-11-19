# File Documentation: index_historical.py

## Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/index_historical.py`
- **Size**: 3,654 bytes
- **Lines**: 102
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Intrinio Index Historical Model."""

from datetime import datetime
from typing import Any

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_historical import (
    IndexHistoricalData,
    IndexHistoricalQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import amake_requests, get_querystring
from pydantic import Field


class IntrinioIndexHistoricalQueryParams(IndexHistoricalQueryParams):
    """Intrinio Index Historical Query.

    Source:
    https://docs.intrinio.com/documentation/web_api/get_stock_market_index_historical_data_v2
    """

    __alias_dict__ = {"limit": "page_size", "sort": "sort_order"}
    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

    limit: int | None = Field(
        default=10000,
        description=QUERY_DESCRIPTIONS.get("limit", ""),
    )


class IntrinioIndexHistoricalData(IndexHistoricalData):
    """Intrinio Index Historical Data."""

    __alias_dict__ = {"close": "value"}


class IntrinioIndexHistoricalFetcher(
    Fetcher[
        IntrinioIndexHistoricalQueryParams,
        list[IntrinioIndexHistoricalData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> IntrinioIndexHistoricalQueryParams:
        """Transform the query params."""
        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return IntrinioIndexHistoricalQueryParams(**transformed_params)

    @staticmethod
    async def aextract_data(
        query: IntrinioIndexHistoricalQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Intrinio endpoint."""
        results = []
        api_key = credentials.get("intrinio_api_key") if credentials else ""
        symbols = query.symbol.replace("$", "").replace("^", "").split(",")
        base_url = "https://api-v2.intrinio.com/indices/stock_market"
        query_str = get_querystring(query.model_dump(by_alias=True), ["symbol"])
        urls = [
            f"{base_url}/${symbol}/historical_data/level?{query_str}&api_key={api_key}"
            for symbol in symbols
        ]

        async def callback(response, _) -> list[dict]:
            """Response callback."""
            _response = await response.json()
            data = _response.get("historical_data")
            symbol = _response["index"].get("symbol").replace("$", "")
            data = [d for d in data if d.get("value") is not None]
            data = [{"symbol": symbol, **d} for d in data] if len(symbols) > 1 else data
            return results.extend(data) if len(data) > 0 else results  # type: ignore

        await amake_requests(urls, callback, **kwargs)

        if len(results) == 0:
            raise EmptyDataError()
        return results

    @staticmethod
    def transform_data(
        query: IntrinioIndexHistoricalQueryParams,  # pylint: disable=unused-argument
        data: list[dict],
        **kwargs: Any,
    ) -> list[IntrinioIndexHistoricalData]:
        """Return the transformed data."""
        return [IntrinioIndexHistoricalData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `index_historical.py`.

**Python Module**

- **Classes** (3): IntrinioIndexHistoricalQueryParams, IntrinioIndexHistoricalData, IntrinioIndexHistoricalFetcher
- **Functions** (4): transform_query, aextract_data, callback, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IntrinioIndexHistoricalQueryParams`**(IndexHistoricalQueryParams)
- **`IntrinioIndexHistoricalData`**(IndexHistoricalData)
- **`IntrinioIndexHistoricalFetcher`**(
    Fetcher[
        IntrinioIndexHistoricalQueryParams,
        list[IntrinioIndexHistoricalData],
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `EmptyDataError`
- `Fetcher`
- `Field`
- `QUERY_DESCRIPTIONS`
- `amake_requests`
- `datetime`
- `dateutil.relativedelta`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.index_historical`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`
- `pydantic`
- `relativedelta`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.450746Z
**Generator**: World's Best Repo Book Generator v1.0
