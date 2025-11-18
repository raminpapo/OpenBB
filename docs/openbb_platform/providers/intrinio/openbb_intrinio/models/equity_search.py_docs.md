# Documentation: openbb_platform/providers/intrinio/openbb_intrinio/models/equity_search.py

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/equity_search.py`
- **Size**: 2,946 characters, 91 lines
- **Words**: 256
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Intrinio Equity Search Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_search import (
    EquitySearchData,
    EquitySearchQueryParams,
)
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from openbb_core.provider.utils.helpers import get_querystring
from openbb_intrinio.utils.helpers import get_data_one
from pydantic import Field


class IntrinioEquitySearchQueryParams(EquitySearchQueryParams):
    """Intrinio Equity Search Query.

    Source: https://docs.intrinio.com/documentation/web_api/search_companies_v2
    """

    __alias_dict__ = {
        "limit": "page_size",
    }

    active: bool = Field(
        default=True,
        description="When true, return companies that are actively traded (having stock prices within the past 14 days)."
        + " When false, return companies that are not actively traded or never have been traded.",
    )
    limit: int | None = Field(
        default=10000,
        description=QUERY_DESCRIPTIONS.get("limit", ""),
    )


class IntrinioEquitySearchData(EquitySearchData):
    """Intrinio Equity Search Data."""

    __alias_dict__ = {
        "intrinio_id": "id",
        "symbol": "ticker",
    }

    cik: str | None = Field(description=DATA_DESCRIPTIONS.get("CIK", ""))
    lei: str | None = Field(
        description="The Legal Entity Identifier (LEI) of the company."
    )
    intrinio_id: str = Field(description="The Intrinio ID of the company.")


class IntrinioEquitySearchFetcher(
    Fetcher[
        IntrinioEquitySearchQueryParams,
        list[IntrinioEquitySearchData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> IntrinioEquitySearchQueryParams:
        """Transform the query."""
        return IntrinioEquitySearchQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: IntrinioEquitySearchQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Intrinio endpoint."""

        api_key = credentials.get("intrinio_api_key") if credentials else ""
        query_str = get_querystring(query.model_dump(by_alias=True), ["is_symbol"])
        base_url = "https://api-v2.intrinio.com/companies/search?"
        url = f"{base_url}{query_str}&api_key={api_key}"
        data = await get_data_one(url, **kwargs)
        return data  # type: ignore

    @staticmethod
    def transform_data(
        query: IntrinioEquitySearchQueryParams, data: dict, **kwargs: Any
    ) -> list[IntrinioEquitySearchData]:
        """Transform the data to the standard format."""
        return [IntrinioEquitySearchData.model_validate(d) for d in data["companies"]]

```

## High-Level Overview

Intrinio Equity Search Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_search import (
EquitySearchData,
EquitySearchQueryParams,
)
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from openbb_core.provider.utils.helpers import get_querystring
from openbb_intrinio.utils.helpers import get_data_one
from pydantic import Field



## Detailed Structure

### Python File Structure

**Classes** (3):
`IntrinioEquitySearchQueryParams`, `IntrinioEquitySearchData`, `IntrinioEquitySearchFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (14):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.equity_search`, `openbb_core.provider.utils.descriptions`, `openbb_core.provider.utils.helpers`, `get_querystring`, `openbb_intrinio.utils.helpers`, `get_data_one`, `pydantic`, `Field`, `the`, `the`


## Key Components

**Class `IntrinioEquitySearchQueryParams`**: Intrinio Equity Search Query.

    Source: https://docs.intrinio.com/documentation/web_api/search_companies_v2

**Class `IntrinioEquitySearchData`**: Intrinio Equity Search Data.

**Class `IntrinioEquitySearchFetcher`**: Transform the query, extract and transform the data from the Intrinio endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_search`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.helpers`
- `openbb_intrinio.utils.helpers`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:40.091974
- Generator: World's Best Repo Book Generator v1.0.0
