# Documentation: openbb_platform/providers/intrinio/openbb_intrinio/models/share_statistics.py

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/share_statistics.py`
- **Size**: 3,142 characters, 96 lines
- **Words**: 231
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Intrinio Share Statistics Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.share_statistics import (
    ShareStatisticsData,
    ShareStatisticsQueryParams,
)
from openbb_core.provider.utils.helpers import (
    ClientResponse,
    amake_requests,
)
from pydantic import Field


class IntrinioShareStatisticsQueryParams(ShareStatisticsQueryParams):
    """Intrinio Share Statistics Query.

    Source: https://data.intrinio.com/data-tag/adjweightedavebasicdilutedsharesos
            https://data.intrinio.com/data-tag/weightedavebasicdilutedsharesos
            https://data.intrinio.com/data-tag/public_float
    """


class IntrinioShareStatisticsData(ShareStatisticsData):
    """Intrinio Share Statistics Data."""

    __alias_dict__ = {
        "outstanding_shares": "weightedavebasicdilutedsharesos",
        "adjusted_outstanding_shares": "adjweightedavebasicdilutedsharesos",
    }

    adjusted_outstanding_shares: float | None = Field(
        default=None,
        description="Total number of shares of a publicly-traded company, adjusted for splits.",
    )
    public_float: float | None = Field(
        default=None,
        description="Aggregate market value of the shares of a publicly-traded company.",
    )


class IntrinioShareStatisticsFetcher(
    Fetcher[
        IntrinioShareStatisticsQueryParams,
        list[IntrinioShareStatisticsData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> IntrinioShareStatisticsQueryParams:
        """Transform the query params."""
        return IntrinioShareStatisticsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: IntrinioShareStatisticsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""
        data = {"symbol": query.symbol, "date": datetime.now().date()}

        tags = [
            "public_float",
            "weightedavebasicdilutedsharesos",
            "adjweightedavebasicdilutedsharesos",
        ]

        urls = [
            f"https://api-v2.intrinio.com/companies/{query.symbol}/data_point/{tag}/number?api_key={api_key}"
            for tag in tags
        ]

        async def callback(response: ClientResponse, _: Any) -> dict:
            """Return the response."""
            return {response.url.parts[-2]: await response.json()}

        for result in await amake_requests(urls, callback, **kwargs):
            data.update(result)

        return [data]

    @staticmethod
    def transform_data(
        query: IntrinioShareStatisticsQueryParams, data: list[dict], **kwargs: Any
    ) -> list[IntrinioShareStatisticsData]:
        """Return the transformed data."""
        return [IntrinioShareStatisticsData.model_validate(d) for d in data]

```

## High-Level Overview

Intrinio Share Statistics Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.share_statistics import (
ShareStatisticsData,
ShareStatisticsQueryParams,
)
from openbb_core.provider.utils.helpers import (
ClientResponse,
amake_requests,
)
from pydantic import Field


class IntrinioShareStatisticsQueryParams(ShareStatisticsQueryParams):

## Detailed Structure

### Python File Structure

**Classes** (3):
`IntrinioShareStatisticsQueryParams`, `IntrinioShareStatisticsData`, `IntrinioShareStatisticsFetcher`

**Functions** (4):
`transform_query`, `aextract_data`, `callback`, `transform_data`

**Imports** (12):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.share_statistics`, `openbb_core.provider.utils.helpers`, `pydantic`, `Field`, `the`, `the`


## Key Components

**Class `IntrinioShareStatisticsQueryParams`**: Intrinio Share Statistics Query.

    Source: https://data.intrinio.com/data-tag/adjweightedavebasicdilutedsharesos
            https://data.intrinio.com/data-tag/weightedavebasicdilutedsharesos
     

**Class `IntrinioShareStatisticsData`**: Intrinio Share Statistics Data.

**Class `IntrinioShareStatisticsFetcher`**: Transform the query, extract and transform the data from the Intrinio endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.share_statistics`
- `openbb_core.provider.utils.helpers`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:40.150374
- Generator: World's Best Repo Book Generator v1.0.0
