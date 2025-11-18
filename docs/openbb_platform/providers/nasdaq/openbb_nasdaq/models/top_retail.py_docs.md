# Documentation: openbb_platform/providers/nasdaq/openbb_nasdaq/models/top_retail.py

## File Metadata
- **Path**: `openbb_platform/providers/nasdaq/openbb_nasdaq/models/top_retail.py`
- **Size**: 2,739 characters, 84 lines
- **Words**: 204
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Nasdaq Top Retail Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.top_retail import (
    TopRetailData,
    TopRetailQueryParams,
)
from pydantic import field_validator


class NasdaqTopRetailQueryParams(TopRetailQueryParams):
    """Nasdaq Top Retail Query.

    Source: https://data.nasdaq.com/databases/RTAT/data
    """


class NasdaqTopRetailData(TopRetailData):
    """Nasdaq Top Retail Data."""

    @field_validator("date", mode="before", check_fields=False)
    def validate_date(cls, v: Any) -> Any:  # pylint: disable=E0213
        """Validate the date."""
        return datetime.strptime(v, "%Y-%m-%d").date()


class NasdaqTopRetailFetcher(
    Fetcher[NasdaqTopRetailQueryParams, list[NasdaqTopRetailData]]
):
    """Transform the query, extract and transform the data from the Nasdaq endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> NasdaqTopRetailQueryParams:
        """Transform the params to the provider-specific query."""
        return NasdaqTopRetailQueryParams(**params)

    @staticmethod
    def extract_data(
        query: NasdaqTopRetailQueryParams,  # pylint: disable=unused-argument
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from Nasdaq."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import make_request

        api_key = credentials.get("nasdaq_api_key") if credentials else None
        response = make_request(
            f"https://data.nasdaq.com/api/v3/datatables/NDAQ/RTAT10/?api_key={api_key}",
        )
        if response.status_code != 200:
            reason = getattr(response, "reason", "Unknown")
            raise OpenBBError(f"Failed to get data from Nasdaq -> {reason}")
        content = response.json()
        return content["datatable"]["data"][: query.limit]

    @staticmethod
    def transform_data(
        query: TopRetailQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[NasdaqTopRetailData]:
        """Transform the data."""
        transformed_data: list[NasdaqTopRetailData] = []
        for row in data:
            transformed_data.append(
                NasdaqTopRetailData.model_validate(
                    {
                        "date": row[0],
                        "symbol": row[1],
                        "activity": row[2],
                        "sentiment": row[3],
                    }
                )
            )

        return transformed_data

```

## High-Level Overview

Nasdaq Top Retail Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.top_retail import (
TopRetailData,
TopRetailQueryParams,
)
from pydantic import field_validator


class NasdaqTopRetailQueryParams(TopRetailQueryParams):
Nasdaq Top Retail Query.



## Detailed Structure

### Python File Structure

**Classes** (3):
`NasdaqTopRetailQueryParams`, `NasdaqTopRetailData`, `NasdaqTopRetailFetcher`

**Functions** (4):
`validate_date`, `transform_query`, `extract_data`, `transform_data`

**Imports** (16):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.top_retail`, `pydantic`, `field_validator`, `the`, `Nasdaq.`, `openbb_core.provider.utils.helpers`, `make_request`, `Nasdaq`


## Key Components

**Class `NasdaqTopRetailQueryParams`**: Nasdaq Top Retail Query.

    Source: https://data.nasdaq.com/databases/RTAT/data

**Class `NasdaqTopRetailData`**: Nasdaq Top Retail Data.

**Class `NasdaqTopRetailFetcher`**: Transform the query, extract and transform the data from the Nasdaq endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.top_retail`
- `pydantic`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:40.329628
- Generator: World's Best Repo Book Generator v1.0.0
