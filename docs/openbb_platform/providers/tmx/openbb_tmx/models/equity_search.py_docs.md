# Documentation: openbb_platform/providers/tmx/openbb_tmx/models/equity_search.py

## File Metadata
- **Path**: `openbb_platform/providers/tmx/openbb_tmx/models/equity_search.py`
- **Size**: 2,215 characters, 73 lines
- **Words**: 171
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""TMX Equity Search fetcher."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_search import (
    EquitySearchData,
    EquitySearchQueryParams,
)
from pydantic import Field


class TmxEquitySearchQueryParams(EquitySearchQueryParams):
    """TMX Equity Search query.

    Source: https://www.tmx.com/
    """

    use_cache: bool = Field(
        default=True,
        description="Whether to use a cached request. The list of companies is cached for two days.",
    )


class TmxEquitySearchData(EquitySearchData):
    """TMX Equity Search Data."""


class TmxEquitySearchFetcher(
    Fetcher[
        TmxEquitySearchQueryParams,
        list[TmxEquitySearchData],
    ]
):
    """TMX Equity Search Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> TmxEquitySearchQueryParams:
        """Transform the query."""
        return TmxEquitySearchQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: TmxEquitySearchQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the TMX endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_tmx.utils.helpers import get_all_tmx_companies
        from pandas import DataFrame

        companies = await get_all_tmx_companies(use_cache=query.use_cache)
        results = DataFrame(index=companies, data=companies.values(), columns=["name"])
        results = results.reset_index().rename(columns={"index": "symbol"})

        if query:
            results = results[
                results["name"].str.contains(query.query, case=False)
                | results["symbol"].str.contains(query.query, case=False)
            ]

        return results.reset_index(drop=True).astype(str).to_dict("records")

    @staticmethod
    def transform_data(
        query: TmxEquitySearchQueryParams, data: list[dict], **kwargs: Any
    ) -> list[TmxEquitySearchData]:
        """Transform the data to the standard format."""
        return [TmxEquitySearchData.model_validate(d) for d in data]

```

## High-Level Overview

TMX Equity Search fetcher.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_search import (
EquitySearchData,
EquitySearchQueryParams,
)
from pydantic import Field


class TmxEquitySearchQueryParams(EquitySearchQueryParams):
TMX Equity Search query.


use_cache: bool = Field(
default=True,

## Detailed Structure

### Python File Structure

**Classes** (3):
`TmxEquitySearchQueryParams`, `TmxEquitySearchData`, `TmxEquitySearchFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (12):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.equity_search`, `pydantic`, `Field`, `the`, `openbb_tmx.utils.helpers`, `get_all_tmx_companies`, `pandas`, `DataFrame`


## Key Components

**Class `TmxEquitySearchQueryParams`**: TMX Equity Search query.

    Source: https://www.tmx.com/

**Class `TmxEquitySearchData`**: TMX Equity Search Data.

**Class `TmxEquitySearchFetcher`**: TMX Equity Search Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_search`
- `pydantic`
- `openbb_tmx.utils.helpers`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:41.779949
- Generator: World's Best Repo Book Generator v1.0.0
