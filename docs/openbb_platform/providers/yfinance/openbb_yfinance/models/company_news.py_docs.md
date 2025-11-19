# File Documentation: company_news.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/company_news.py`
- **Size**: 3,925 bytes
- **Lines**: 118
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Yahoo Finance Company News Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.company_news import (
    CompanyNewsData,
    CompanyNewsQueryParams,
)
from pydantic import Field, field_validator


class YFinanceCompanyNewsQueryParams(CompanyNewsQueryParams):
    """YFinance Company News Query.

    Source: https://finance.yahoo.com/news/
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def _symbol_mandatory(cls, v):
        """Symbol mandatory validator."""
        if not v:
            raise ValueError("Required field missing -> symbol")
        return v


class YFinanceCompanyNewsData(CompanyNewsData):
    """YFinance Company News Data."""

    source: str | None = Field(default=None, description="Source of the news article")


class YFinanceCompanyNewsFetcher(
    Fetcher[
        YFinanceCompanyNewsQueryParams,
        list[YFinanceCompanyNewsData],
    ]
):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFinanceCompanyNewsQueryParams:
        """Transform query params."""
        return YFinanceCompanyNewsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFinanceCompanyNewsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        from curl_adapter import CurlCffiAdapter
        from openbb_core.provider.utils.errors import EmptyDataError
        from openbb_core.provider.utils.helpers import get_requests_session
        from yfinance import Ticker

        results: list = []
        symbols = query.symbol.split(",")  # type: ignore
        session = get_requests_session()
        session.mount("https://", CurlCffiAdapter())
        session.mount("http://", CurlCffiAdapter())

        async def get_one(symbol):
            data = Ticker(symbol, session=session).get_news(
                count=query.limit,
                tab="all",
            )
            for d in data:
                new_content: dict = {}
                content = d.get("content")
                if not content:
                    continue
                if thumbnail := content.get("thumbnail"):
                    images = thumbnail.get("resolutions")
                    if images:
                        new_content["images"] = [
                            {k: str(v) for k, v in img.items()} for img in images
                        ]
                new_content["url"] = content.get("canonicalUrl", {}).get("url")
                new_content["source"] = content.get("provider", {}).get("displayName")
                new_content["title"] = content.get("title")
                new_content["date"] = content.get("pubDate")
                description = content.get("description")
                summary = content.get("summary")

                if description:
                    new_content["text"] = description
                elif summary:
                    new_content["text"] = summary

                results.append(new_content)

        tasks = [get_one(symbol) for symbol in symbols]

        await asyncio.gather(*tasks)

        if not results:
            raise EmptyDataError("No data was returned for the given symbol(s)")

        return results

    @staticmethod
    def transform_data(
        query: YFinanceCompanyNewsQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFinanceCompanyNewsData]:
        """Transform data."""
        return [YFinanceCompanyNewsData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `company_news.py`.

**Python Module**

- **Classes** (3): YFinanceCompanyNewsQueryParams, YFinanceCompanyNewsData, YFinanceCompanyNewsFetcher
- **Functions** (5): _symbol_mandatory, transform_query, aextract_data, get_one, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFinanceCompanyNewsQueryParams`**(CompanyNewsQueryParams)
- **`YFinanceCompanyNewsData`**(CompanyNewsData)
- **`YFinanceCompanyNewsFetcher`**(
    Fetcher[
        YFinanceCompanyNewsQueryParams,
        list[YFinanceCompanyNewsData],
    ]
)

#### Functions

- **`_symbol_mandatory(cls, v)`**
- **`get_one(symbol)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `CurlCffiAdapter`
- `EmptyDataError`
- `Fetcher`
- `Field`
- `Ticker`
- `asyncio`
- `curl_adapter`
- `get_requests_session`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.company_news`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.161470Z
**Generator**: World's Best Repo Book Generator v1.0
