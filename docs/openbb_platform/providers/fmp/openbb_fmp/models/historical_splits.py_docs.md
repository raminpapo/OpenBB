# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/historical_splits.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/historical_splits.py`
- **Size**: 2,085 characters, 66 lines
- **Words**: 159
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Historical Splits Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.historical_splits import (
    HistoricalSplitsData,
    HistoricalSplitsQueryParams,
)
from openbb_fmp.utils.helpers import get_data_many
from pydantic import field_validator


class FMPHistoricalSplitsQueryParams(HistoricalSplitsQueryParams):
    """FMP Historical Splits Query.

    Source: https://site.financialmodelingprep.com/developer/docs#splits-company
    """


class FMPHistoricalSplitsData(HistoricalSplitsData):
    """FMP Historical Splits Data."""

    @field_validator("date", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v: str):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        return datetime.strptime(v, "%Y-%m-%d") if v else None


class FMPHistoricalSplitsFetcher(
    Fetcher[
        FMPHistoricalSplitsQueryParams,
        list[FMPHistoricalSplitsData],
    ]
):
    """FMP Historical Splits Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPHistoricalSplitsQueryParams:
        """Transform the query params."""
        return FMPHistoricalSplitsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPHistoricalSplitsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        url = f"https://financialmodelingprep.com/stable/splits?symbol={query.symbol}&apikey={api_key}"

        return await get_data_many(url, "historical", **kwargs)

    @staticmethod
    def transform_data(
        query: FMPHistoricalSplitsQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPHistoricalSplitsData]:
        """Return the transformed data."""
        return [FMPHistoricalSplitsData.model_validate(d) for d in data]

```

## High-Level Overview

FMP Historical Splits Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.historical_splits import (
HistoricalSplitsData,
HistoricalSplitsQueryParams,
)
from openbb_fmp.utils.helpers import get_data_many
from pydantic import field_validator


class FMPHistoricalSplitsQueryParams(HistoricalSplitsQueryParams):
FMP Historical Splits Query.



## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPHistoricalSplitsQueryParams`, `FMPHistoricalSplitsData`, `FMPHistoricalSplitsFetcher`

**Functions** (4):
`date_validate`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (12):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.historical_splits`, `openbb_fmp.utils.helpers`, `get_data_many`, `pydantic`, `field_validator`, `the`


## Key Components

**Class `FMPHistoricalSplitsQueryParams`**: FMP Historical Splits Query.

    Source: https://site.financialmodelingprep.com/developer/docs#splits-company

**Class `FMPHistoricalSplitsData`**: FMP Historical Splits Data.

**Class `FMPHistoricalSplitsFetcher`**: FMP Historical Splits Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.historical_splits`
- `openbb_fmp.utils.helpers`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:39.388414
- Generator: World's Best Repo Book Generator v1.0.0
