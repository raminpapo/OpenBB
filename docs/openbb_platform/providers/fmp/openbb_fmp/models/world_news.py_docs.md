# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/world_news.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/world_news.py`
- **Size**: 3,333 characters, 109 lines
- **Words**: 275
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP World News Model."""

# pylint: disable=unused-argument

import warnings
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.world_news import (
    WorldNewsData,
    WorldNewsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FMPWorldNewsQueryParams(WorldNewsQueryParams):
    """FMP World News Query.

    Source: https://site.financialmodelingprep.com/developer/docs/general-news-api/
    """

    topic: Literal[
        "fmp_articles", "general", "press_releases", "stocks", "forex", "crypto"
    ] = Field(
        default="general",
        description="The topic of the news to be fetched.",
    )

    page: int | None = Field(
        default=None,
        le=100,
        ge=0,
        description="Page number of the results. Use in combination with limit.",
    )


class FMPWorldNewsData(WorldNewsData):
    """FMP World News Data."""

    __alias_dict__ = {
        "date": "publishedDate",
        "images": "image",
        "excerpt": "text",
        "source": "site",
        "author": "publisher",
        "symbols": "symbol",
    }

    source: str = Field(description="News source.")


class FMPWorldNewsFetcher(
    Fetcher[
        FMPWorldNewsQueryParams,
        list[FMPWorldNewsData],
    ]
):
    """FMP World News Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPWorldNewsQueryParams:
        """Transform the query params."""
        if params.get("start_date") or params.get("end_date"):
            warnings.warn(
                "start_date and end_date are not supported for this endpoint."
            )
        return FMPWorldNewsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPWorldNewsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        base_url = "https://financialmodelingprep.com/stable/"

        if query.topic == "fmp_articles":
            base_url = f"{base_url}news/fmp-articles?"
            url = (
                base_url
                + f"page={query.page}&limit={query.limit if query.limit else 20}&apikey={api_key}"
            )
        else:
            base_url = f"{base_url}news/{query.topic.replace('_', '-')}-latest?"
            url = (
                base_url
                + f"from={query.start_date}&to={query.end_date}"
                + f"&limit={query.limit if query.limit else 250}&page={query.page if query.page else 0}&apikey={api_key}"
            )

        results: list = await get_data_many(url, **kwargs)

        return sorted(results, key=lambda x: x["publishedDate"], reverse=True)

    @staticmethod
    def transform_data(
        query: FMPWorldNewsQueryParams, data: list, **kwargs: Any
    ) -> list[FMPWorldNewsData]:
        """Return the transformed data."""
        if not data:
            raise EmptyDataError("No data was returned from FMP query.")
        return [FMPWorldNewsData.model_validate(d) for d in data]

```

## High-Level Overview

FMP World News Model.

# pylint: disable=unused-argument

import warnings
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.world_news import (
WorldNewsData,
WorldNewsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FMPWorldNewsQueryParams(WorldNewsQueryParams):
FMP World News Query.



## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPWorldNewsQueryParams`, `FMPWorldNewsData`, `FMPWorldNewsFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (14):
`warnings`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.world_news`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `the`, `openbb_fmp.utils.helpers`, `get_data_many`, `FMP`


## Key Components

**Class `FMPWorldNewsQueryParams`**: FMP World News Query.

    Source: https://site.financialmodelingprep.com/developer/docs/general-news-api/

**Class `FMPWorldNewsData`**: FMP World News Data.

**Class `FMPWorldNewsFetcher`**: FMP World News Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `warnings`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.world_news`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `openbb_fmp.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:39.425262
- Generator: World's Best Repo Book Generator v1.0.0
