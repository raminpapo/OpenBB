# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/company_news.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/company_news.py`
- **Size**: 3,404 characters, 115 lines
- **Words**: 288
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Company News Model."""

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.company_news import (
    CompanyNewsData,
    CompanyNewsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class FMPCompanyNewsQueryParams(CompanyNewsQueryParams):
    """FMP Company News Query.

    Source: https://site.financialmodelingprep.com/developer/docs/stock-news-api/
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

    page: int = Field(
        default=0,
        le=100,
        ge=0,
        description="Page number of the results. Use in combination with limit.",
    )
    press_release: bool | None = Field(
        default=None,
        description="When true, will return only press releases for the given symbol(s).",
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def _symbol_mandatory(cls, v):
        """Symbol mandatory validator."""
        if not v:
            raise ValueError("Required field missing -> symbol")
        return v


class FMPCompanyNewsData(CompanyNewsData):
    """FMP Company News Data."""

    __alias_dict__ = {
        "symbols": "symbol",
        "date": "publishedDate",
        "author": "publisher",
        "images": "image",
        "source": "site",
        "excerpt": "text",
    }

    source: str = Field(description="Name of the news site.")


class FMPCompanyNewsFetcher(
    Fetcher[
        FMPCompanyNewsQueryParams,
        list[FMPCompanyNewsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPCompanyNewsQueryParams:
        """Transform the query params."""
        return FMPCompanyNewsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPCompanyNewsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        limit = query.limit if query.limit else 250
        page = query.page if query.page else 0
        base_url = "https://financialmodelingprep.com/stable/news/"
        symbols = query.symbol

        if query.press_release:
            base_url += "press-releases?"
        else:
            base_url += "stock?"

        url = base_url + f"symbols={symbols}"

        if query.start_date:
            url += f"&from={query.start_date}"

        if query.end_date:
            url += f"&to={query.end_date}"

        url += f"&limit={limit}&page={page}&apikey={api_key}"

        response = await get_data_many(url, **kwargs)

        if not response:
            raise EmptyDataError()

        return sorted(response, key=lambda x: x["publishedDate"], reverse=True)

    # pylint: disable=unused-argument
    @staticmethod
    def transform_data(
        query: FMPCompanyNewsQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPCompanyNewsData]:
        """Return the transformed data."""
        return [FMPCompanyNewsData.model_validate(d) for d in data]

```

## High-Level Overview

FMP Company News Model.

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.company_news import (
CompanyNewsData,
CompanyNewsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class FMPCompanyNewsQueryParams(CompanyNewsQueryParams):
FMP Company News Query.


__json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

page: int = Field(

## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPCompanyNewsQueryParams`, `FMPCompanyNewsData`, `FMPCompanyNewsFetcher`

**Functions** (4):
`_symbol_mandatory`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (13):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.company_news`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `the`, `the`, `openbb_fmp.utils.helpers`, `get_data_many`


## Key Components

**Class `FMPCompanyNewsQueryParams`**: FMP Company News Query.

    Source: https://site.financialmodelingprep.com/developer/docs/stock-news-api/

**Class `FMPCompanyNewsData`**: FMP Company News Data.

**Class `FMPCompanyNewsFetcher`**: Transform the query, extract and transform the data from the FMP endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.company_news`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `openbb_fmp.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:39.331530
- Generator: World's Best Repo Book Generator v1.0.0
