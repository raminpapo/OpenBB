# File Documentation: equity_search.py

## Metadata
- **Path**: `openbb_platform/providers/cboe/openbb_cboe/models/equity_search.py`
- **Size**: 2,362 bytes
- **Lines**: 82
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""CBOE Equity Search Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_search import (
    EquitySearchData,
    EquitySearchQueryParams,
)
from pydantic import Field


class CboeEquitySearchQueryParams(EquitySearchQueryParams):
    """CBOE Equity Search Query.

    Source: https://www.cboe.com/
    """

    use_cache: bool = Field(
        default=True,
        description="Whether to use the cache or not.",
    )


class CboeEquitySearchData(EquitySearchData):
    """CBOE Equity Search Data."""

    __alias_dict__ = {
        "dpm_name": "DPM Name",
    }

    dpm_name: str | None = Field(
        default=None,
        description="Name of the primary market maker.",
    )
    post_station: str | None = Field(
        default=None, description="Post and station location on the CBOE trading floor."
    )


class CboeEquitySearchFetcher(
    Fetcher[
        CboeEquitySearchQueryParams,
        list[CboeEquitySearchData],
    ]
):
    """Transform the query, extract and transform the data from the CBOE endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> CboeEquitySearchQueryParams:
        """Transform the query."""
        return CboeEquitySearchQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: CboeEquitySearchQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Return the raw data from the CBOE endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_cboe.utils.helpers import get_company_directory

        data = {}
        symbols = await get_company_directory(query.use_cache, **kwargs)
        symbols = symbols.reset_index()
        target = "name" if query.is_symbol is False else "symbol"
        idx = symbols[target].str.contains(query.query, case=False)
        result = symbols[idx].to_dict("records")
        data.update({"results": result})

        return data

    @staticmethod
    def transform_data(
        query: CboeEquitySearchQueryParams, data: dict, **kwargs: Any
    ) -> list[CboeEquitySearchData]:
        """Transform the data to the standard format."""
        return [CboeEquitySearchData.model_validate(d) for d in data["results"]]

```



---

## High-Level Overview

This is a **python** file named `equity_search.py`.

**Python Module**

- **Classes** (3): CboeEquitySearchQueryParams, CboeEquitySearchData, CboeEquitySearchFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CboeEquitySearchQueryParams`**(EquitySearchQueryParams)
- **`CboeEquitySearchData`**(EquitySearchData)
- **`CboeEquitySearchFetcher`**(
    Fetcher[
        CboeEquitySearchQueryParams,
        list[CboeEquitySearchData],
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
- `get_company_directory`
- `openbb_cboe.utils.helpers`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_search`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.514502Z
**Generator**: World's Best Repo Book Generator v1.0
