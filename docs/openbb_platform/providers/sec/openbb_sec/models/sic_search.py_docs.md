# File Documentation: sic_search.py

## Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/models/sic_search.py`
- **Size**: 3,788 bytes
- **Lines**: 112
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""SEC Standard Industrial Classification Code (SIC) Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cot_search import CotSearchQueryParams
from pydantic import Field


class SecSicSearchQueryParams(CotSearchQueryParams):
    """SEC Standard Industrial Classification Code (SIC) Query.

    Source: https://sec.gov/
    """

    use_cache: bool | None = Field(
        default=True,
        description="Whether or not to use cache.",
    )


class SecSicSearchData(Data):
    """SEC Standard Industrial Classification Code (SIC) Data."""

    __alias_dict__ = {
        "sic": "SIC Code",
        "industry": "Industry Title",
        "office": "Office",
    }

    sic: int = Field(description="Sector Industrial Code (SIC)")
    industry: str = Field(description="Industry title.")
    office: str = Field(
        description="Reporting office within the Corporate Finance Office"
    )


class SecSicSearchFetcher(
    Fetcher[
        SecSicSearchQueryParams,
        list[SecSicSearchData],
    ]
):
    """SEC SIC Search Fetcher."""

    @staticmethod
    def transform_query(
        params: dict[str, Any], **kwargs: Any
    ) -> SecSicSearchQueryParams:
        """Transform the query."""
        return SecSicSearchQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: SecSicSearchQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract data from the SEC website table."""
        # pylint: disable=import-outside-toplevel
        from aiohttp_client_cache import SQLiteBackend
        from aiohttp_client_cache.session import CachedSession
        from openbb_core.app.utils import get_user_cache_directory
        from openbb_core.provider.utils.helpers import amake_request
        from openbb_sec.utils.helpers import SEC_HEADERS, sec_callback
        from pandas import DataFrame, read_html

        data = DataFrame()
        results: list[dict] = []
        url = "https://www.sec.gov/corpfin/division-of-corporation-finance-standard-industrial-classification-sic-code-list"
        response: dict | list[dict] | str = {}
        if query.use_cache is True:
            cache_dir = f"{get_user_cache_directory()}/http/sec_sic"
            async with CachedSession(
                cache=SQLiteBackend(cache_dir, expire_after=3600 * 24 * 30)
            ) as session:
                try:
                    response = await amake_request(
                        url,
                        headers=SEC_HEADERS,
                        session=session,
                        response_callback=sec_callback,  # type: ignore
                    )
                finally:
                    await session.close()
        else:
            response = await amake_request(url, headers=SEC_HEADERS, response_callback=sec_callback)  # type: ignore

        data = read_html(response)[0].astype(str)
        if len(data) == 0:
            return results
        if query:
            data = data[
                data["SIC Code"].str.contains(query.query, case=False)
                | data["Office"].str.contains(query.query, case=False)
                | data["Industry Title"].str.contains(query.query, case=False)
            ]
        data["SIC Code"] = data["SIC Code"].astype(int)
        results = data.to_dict("records")

        return results

    @staticmethod
    def transform_data(
        query: SecSicSearchQueryParams, data: list[dict], **kwargs: Any
    ) -> list[SecSicSearchData]:
        """Transform the data."""
        return [SecSicSearchData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `sic_search.py`.

**Python Module**

- **Classes** (3): SecSicSearchQueryParams, SecSicSearchData, SecSicSearchFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SecSicSearchQueryParams`**(CotSearchQueryParams)
- **`SecSicSearchData`**(Data)
- **`SecSicSearchFetcher`**(
    Fetcher[
        SecSicSearchQueryParams,
        list[SecSicSearchData],
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `CachedSession`
- `CotSearchQueryParams`
- `Data`
- `DataFrame`
- `Fetcher`
- `Field`
- `SEC_HEADERS`
- `SQLiteBackend`
- `aiohttp_client_cache`
- `aiohttp_client_cache.session`
- `amake_request`
- `get_user_cache_directory`
- `openbb_core.app.utils`
- `openbb_core.provider.abstract.data`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:52.012232Z
**Generator**: World's Best Repo Book Generator v1.0
