# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/discovery_filings.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/discovery_filings.py`
- **Size**: 3,797 characters, 118 lines
- **Words**: 317
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Discovery Filings Model."""

# pylint: disable=unused-argument

from datetime import datetime, timedelta
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.discovery_filings import (
    DiscoveryFilingsData,
    DiscoveryFilingsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, model_validator


class FMPDiscoveryFilingsQueryParams(DiscoveryFilingsQueryParams):
    """FMP Discovery Filings Query.

    Source: https://site.financialmodelingprep.com/developer/docs#search-by-form-type
    """

    __alias_dict__ = {
        "start_date": "from",
        "end_date": "to",
        "form_type": "formType",
    }

    limit: int | None = Field(
        default=None,
        description="The maximum number of results to return. Default is 10000.",
    )

    @model_validator(mode="before")
    @classmethod
    def _check_date_range(cls, values):
        """Validate date range."""
        start_date = values.get("start_date")
        end_date = values.get("end_date")

        # Validate date range
        if start_date and end_date and end_date - start_date > timedelta(days=90):
            raise ValueError("Date range cannot exceed 90 days.")

        return values


class FMPDiscoveryFilingsData(DiscoveryFilingsData):
    """FMP Discovery Filings Data."""

    final_link: str = Field(
        description="Direct URL to the main document of the filing."
    )


class FMPDiscoveryFilingsFetcher(
    Fetcher[
        FMPDiscoveryFilingsQueryParams,
        list[FMPDiscoveryFilingsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPDiscoveryFilingsQueryParams:
        """Transform the query."""
        return FMPDiscoveryFilingsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPDiscoveryFilingsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        import math  # noqa
        from openbb_core.provider.utils.helpers import amake_requests, get_querystring

        api_key = credentials.get("fmp_api_key") if credentials else ""
        data: list[dict] = []
        limit = query.limit or 10000
        base_url = (
            "https://financialmodelingprep.com/stable/sec-filings-search/form-type"
            if query.form_type
            else "https://financialmodelingprep.com/stable/sec-filings-financials/"
        )
        start_date = (
            query.start_date
            or (datetime.now() - timedelta(days=89 if query.form_type else 2)).date()
        )
        end_date = query.end_date or datetime.now().date()
        query.start_date = start_date
        query.end_date = end_date

        query_str = get_querystring(query.model_dump(by_alias=True), ["limit"])

        # FMP only allows 1000 results per page
        pages = math.ceil(limit / 1000)

        urls = [
            f"{base_url}?{query_str}&page={page}&limit=1000&apikey={api_key}"
            for page in range(pages)
        ]

        data = await amake_requests(urls, **kwargs)

        return sorted(data, key=lambda x: x["acceptedDate"], reverse=True)

    @staticmethod
    def transform_data(
        query: FMPDiscoveryFilingsQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPDiscoveryFilingsData]:
        """Return the transformed data."""
        if not data:
            raise EmptyDataError("No data was returned for the given query.")
        return [FMPDiscoveryFilingsData.model_validate(d) for d in data]

```

## High-Level Overview

FMP Discovery Filings Model.

# pylint: disable=unused-argument

from datetime import datetime, timedelta
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.discovery_filings import (
DiscoveryFilingsData,
DiscoveryFilingsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, model_validator


class FMPDiscoveryFilingsQueryParams(DiscoveryFilingsQueryParams):
FMP Discovery Filings Query.



## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPDiscoveryFilingsQueryParams`, `FMPDiscoveryFilingsData`, `FMPDiscoveryFilingsFetcher`

**Functions** (4):
`_check_date_range`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (16):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.discovery_filings`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `the`, `the`, `math`, `openbb_core.provider.utils.helpers`, `amake_requests`


## Key Components

**Class `FMPDiscoveryFilingsQueryParams`**: FMP Discovery Filings Query.

    Source: https://site.financialmodelingprep.com/developer/docs#search-by-form-type

**Class `FMPDiscoveryFilingsData`**: FMP Discovery Filings Data.

**Class `FMPDiscoveryFilingsFetcher`**: Transform the query, extract and transform the data from the FMP endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.discovery_filings`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `math`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:39.341854
- Generator: World's Best Repo Book Generator v1.0.0
