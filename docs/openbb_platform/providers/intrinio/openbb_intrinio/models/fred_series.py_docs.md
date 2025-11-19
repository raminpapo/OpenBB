# File Documentation: fred_series.py

## Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/fred_series.py`
- **Size**: 3,905 bytes
- **Lines**: 120
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Intrinio FRED Series Model."""

# pylint: disable=unused-argument

import asyncio
from datetime import datetime
from typing import Any

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.fred_series import (
    SeriesData,
    SeriesQueryParams,
)
from openbb_core.provider.utils.helpers import (
    ClientResponse,
    ClientSession,
    amake_requests,
    get_querystring,
)
from pydantic import Field


class IntrinioFredSeriesQueryParams(SeriesQueryParams):
    """Intrinio FRED Series Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_economic_index_historical_data_v2
    """

    __alias_dict__ = {"limit": "page_size"}

    all_pages: bool | None = Field(
        default=False,
        description="Returns all pages of data from the API call at once.",
    )
    sleep: float | None = Field(
        default=1.0,
        description="Time to sleep between requests to avoid rate limiting.",
    )


class IntrinioFredSeriesData(SeriesData):
    """Intrinio FRED Series Data."""

    value: float | None = Field(default=None, description="Value of the index.")


class IntrinioFredSeriesFetcher(
    Fetcher[
        IntrinioFredSeriesQueryParams,
        list[IntrinioFredSeriesData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> IntrinioFredSeriesQueryParams:
        """Transform the query params."""
        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return IntrinioFredSeriesQueryParams(**transformed_params)

    @staticmethod
    async def aextract_data(
        query: IntrinioFredSeriesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""

        base_url = "https://api-v2.intrinio.com"
        query_str = get_querystring(
            query.model_dump(), ["symbol", "all_pages", "sleep"]
        )

        url = (
            f"{base_url}/indices/economic/${query.symbol.replace('$', '')}/historical_data/level"
            f"?{query_str}&api_key={api_key}"
        )

        async def callback(response: ClientResponse, session: ClientSession) -> list:
            """Return the response."""
            init_response: Any = await response.json()
            all_data: list = []
            init_data = init_response.get("historical_data", [])

            if init_data and isinstance(init_data, list):
                all_data.extend(init_data)

            if query.all_pages:
                next_page = init_response.get("next_page", None)
                while next_page:
                    if query.limit and query.limit > 100:
                        await asyncio.sleep(query.sleep or 1.0)

                    url = response.url.update_query(next_page=next_page).human_repr()
                    response_data = await session.get_json(url)

                    all_data.extend(response_data.get("historical_data", []))  # type: ignore
                    next_page = response_data.get("next_page", None)  # type: ignore

            return all_data

        return await amake_requests([url], callback, **kwargs)

    @staticmethod
    def transform_data(
        query: IntrinioFredSeriesQueryParams, data: list[dict], **kwargs: Any
    ) -> list[IntrinioFredSeriesData]:
        """Return the transformed data."""
        return [IntrinioFredSeriesData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `fred_series.py`.

**Python Module**

- **Classes** (3): IntrinioFredSeriesQueryParams, IntrinioFredSeriesData, IntrinioFredSeriesFetcher
- **Functions** (4): transform_query, aextract_data, callback, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IntrinioFredSeriesQueryParams`**(SeriesQueryParams)
- **`IntrinioFredSeriesData`**(SeriesData)
- **`IntrinioFredSeriesFetcher`**(
    Fetcher[
        IntrinioFredSeriesQueryParams,
        list[IntrinioFredSeriesData],
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
- `Field`
- `asyncio`
- `datetime`
- `dateutil.relativedelta`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.fred_series`
- `openbb_core.provider.utils.helpers`
- `pydantic`
- `relativedelta`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.437733Z
**Generator**: World's Best Repo Book Generator v1.0
