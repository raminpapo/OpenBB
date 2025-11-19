# File Documentation: equity_search.py

## Metadata
- **Path**: `openbb_platform/providers/tmx/openbb_tmx/models/equity_search.py`
- **Size**: 2,215 bytes
- **Lines**: 73
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `equity_search.py`.

**Python Module**

- **Classes** (3): TmxEquitySearchQueryParams, TmxEquitySearchData, TmxEquitySearchFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TmxEquitySearchQueryParams`**(EquitySearchQueryParams)
- **`TmxEquitySearchData`**(EquitySearchData)
- **`TmxEquitySearchFetcher`**(
    Fetcher[
        TmxEquitySearchQueryParams,
        list[TmxEquitySearchData],
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `DataFrame`
- `Fetcher`
- `Field`
- `get_all_tmx_companies`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_search`
- `openbb_tmx.utils.helpers`
- `pandas`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:53.081173Z
**Generator**: World's Best Repo Book Generator v1.0
