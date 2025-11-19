# File Documentation: historical_dividends.py

## Metadata
- **Path**: `openbb_platform/providers/tmx/openbb_tmx/models/historical_dividends.py`
- **Size**: 3,678 bytes
- **Lines**: 112
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""TMX Stock Dividends Model"""

# pylint: disable=unused-argument

from datetime import date as dateType
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.historical_dividends import (
    HistoricalDividendsData,
    HistoricalDividendsQueryParams,
)
from pydantic import Field


class TmxHistoricalDividendsQueryParams(HistoricalDividendsQueryParams):
    """TMX Historical Dividends Query Params"""


class TmxHistoricalDividendsData(HistoricalDividendsData):
    """TMX Historical Dividends Data"""

    __alias_dict__ = {
        "ex_dividend_date": "exDate",
        "record_date": "recordDate",
        "payment_date": "payableDate",
        "declaration_date": "declarationDate",
    }
    currency: str | None = Field(
        default=None, description="The currency the dividend is paid in."
    )
    decalaration_date: dateType | None = Field(
        default=None, description="The date of the announcement."
    )
    record_date: dateType | None = Field(
        default=None,
        description="The record date of ownership for rights to the dividend.",
    )
    payment_date: dateType | None = Field(
        default=None, description="The date the dividend is paid."
    )


class TmxHistoricalDividendsFetcher(
    Fetcher[TmxHistoricalDividendsQueryParams, list[TmxHistoricalDividendsData]]
):
    """TMX Historical Dividends Fetcher"""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> TmxHistoricalDividendsQueryParams:
        """Transform the query."""
        return TmxHistoricalDividendsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: TmxHistoricalDividendsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the TMX endpoint."""
        # pylint: disable=import-outside-toplevel
        import json  # noqa
        from openbb_tmx.utils import gql  # noqa
        from openbb_tmx.utils.helpers import get_data_from_gql, get_random_agent  # noqa

        user_agent = get_random_agent()
        symbol = (
            query.symbol.upper()
            .replace("-", ".")
            .replace(".TO", "")
            .replace(".TSX", "")
        )
        data = []
        payload = gql.historical_dividends_payload.copy()
        payload["variables"]["symbol"] = symbol
        payload["variables"]["batch"] = 500
        payload["variables"]["page"] = 1

        url = "https://app-money.tmx.com/graphql"
        response = await get_data_from_gql(
            method="POST",
            url=url,
            data=json.dumps(payload),
            headers={
                "authority": "app-money.tmx.com",
                "referer": f"https://money.tmx.com/en/quote/{symbol}",
                "locale": "en",
                "Content-Type": "application/json",
                "User-Agent": user_agent,
                "Accept": "*/*",
            },
            timeout=5,
        )
        try:
            if response.get("data", {}).get("dividends"):  # type: ignore
                data = response["data"]["dividends"]  # type: ignore
                data = sorted(data["dividends"], key=lambda d: d["exDate"])  # type: ignore

        except Exception as e:
            raise RuntimeError(e) from e

        return data

    @staticmethod
    def transform_data(
        query: TmxHistoricalDividendsQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[TmxHistoricalDividendsData]:
        """Return the transformed data."""
        return [TmxHistoricalDividendsData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `historical_dividends.py`.

**Python Module**

- **Classes** (3): TmxHistoricalDividendsQueryParams, TmxHistoricalDividendsData, TmxHistoricalDividendsFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 5


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TmxHistoricalDividendsQueryParams`**(HistoricalDividendsQueryParams)
- **`TmxHistoricalDividendsData`**(HistoricalDividendsData)
- **`TmxHistoricalDividendsFetcher`**(
    Fetcher[TmxHistoricalDividendsQueryParams, list[TmxHistoricalDividendsData]]
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
- `date`
- `datetime`
- `get_data_from_gql`
- `gql`
- `json`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.historical_dividends`
- `openbb_tmx.utils`
- `openbb_tmx.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:53.095251Z
**Generator**: World's Best Repo Book Generator v1.0
