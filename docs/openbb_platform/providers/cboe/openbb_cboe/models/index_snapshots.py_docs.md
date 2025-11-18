# Documentation: openbb_platform/providers/cboe/openbb_cboe/models/index_snapshots.py

## File Metadata
- **Path**: `openbb_platform/providers/cboe/openbb_cboe/models/index_snapshots.py`
- **Size**: 4,873 characters, 152 lines
- **Words**: 411
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""CBOE Index Snapshots Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_snapshots import (
    IndexSnapshotsData,
    IndexSnapshotsQueryParams,
)
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class CboeIndexSnapshotsQueryParams(IndexSnapshotsQueryParams):
    """CBOE Index Snapshots Query.

    Source: https://www.cboe.com/
    """

    region: Literal["us", "eu"] = Field(
        default="us",
    )

    @field_validator("region", mode="after", check_fields=False)
    @classmethod
    def validate_region(cls, v):
        """Validate region."""
        return v if v else "us"


class CboeIndexSnapshotsData(IndexSnapshotsData):
    """CBOE Index Snapshots Data."""

    __alias_dict__ = {
        "prev_close": "prev_day_close",
        "change": "price_change",
        "change_percent": "price_change_percent",
        "price": "current_price",
    }
    bid: float | None = Field(default=None, description="Current bid price.")
    ask: float | None = Field(default=None, description="Current ask price.")
    open: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("open", "")
    )
    high: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("high", "")
    )
    low: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("low", "")
    )
    close: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("close", "")
    )
    volume: int | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("volume", "")
    )
    prev_close: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("prev_close", "")
    )
    change: float | None = Field(default=None, description="Change in price.")
    change_percent: float | None = Field(
        default=None, description="Change in price as a normalized percentage."
    )
    last_trade_time: datetime | None = Field(
        default=None, description="Last trade timestamp for the symbol."
    )
    status: str | None = Field(
        default=None, description="Status of the market, open or closed."
    )


class CboeIndexSnapshotsFetcher(
    Fetcher[
        CboeIndexSnapshotsQueryParams,
        list[CboeIndexSnapshotsData],
    ]
):
    """Transform the query, extract and transform the data from the CBOE endpoints"""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> CboeIndexSnapshotsQueryParams:
        """Transform the query."""
        return CboeIndexSnapshotsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: CboeIndexSnapshotsQueryParams,
        credentials: dict[str, str] | None,  # pylint: disable=unused-argument
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Cboe endpoint"""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import amake_request

        url: str = ""
        if query.region == "us":
            url = "https://cdn.cboe.com/api/global/delayed_quotes/quotes/all_us_indices.json"
        if query.region == "eu":
            url = "https://cdn.cboe.com/api/global/european_indices/index_quotes/all-indices.json"

        data = await amake_request(url, **kwargs)
        return data.get("data")  # type: ignore

    @staticmethod
    def transform_data(
        query: CboeIndexSnapshotsQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[CboeIndexSnapshotsData]:
        """Transform the data to the standard format"""
        # pylint: disable=import-outside-toplevel
        from pandas import DataFrame

        if not data:
            raise EmptyDataError()
        df = DataFrame(data)
        percent_cols = [
            "price_change_percent",
            "iv30",
            "iv30_change",
            "iv30_change_percent",
        ]
        for col in percent_cols:
            if col in df.columns:
                df[col] = round(df[col] / 100, 6)
        df = (
            df.replace(0, None)
            .replace("", None)
            .dropna(how="all", axis=1)
            .fillna("N/A")
            .replace("N/A", None)
        )
        drop_cols = [
            "exchange_id",
            "seqno",
            "index",
            "security_type",
            "ask_size",
            "bid_size",
        ]
        for col in drop_cols:
            if col in df.columns:
                df = df.drop(columns=col)
        return [
            CboeIndexSnapshotsData.model_validate(d)
            for d in df.to_dict(orient="records")
        ]

```

## High-Level Overview

CBOE Index Snapshots Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_snapshots import (
IndexSnapshotsData,
IndexSnapshotsQueryParams,
)
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class CboeIndexSnapshotsQueryParams(IndexSnapshotsQueryParams):
CBOE Index Snapshots Query.


## Detailed Structure

### Python File Structure

**Classes** (3):
`CboeIndexSnapshotsQueryParams`, `CboeIndexSnapshotsData`, `CboeIndexSnapshotsFetcher`

**Functions** (4):
`validate_region`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (19):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.index_snapshots`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `the`, `the`, `openbb_core.provider.utils.helpers`, `amake_request`, `pandas`, `DataFrame`


## Key Components

**Class `CboeIndexSnapshotsQueryParams`**: CBOE Index Snapshots Query.

    Source: https://www.cboe.com/

**Class `CboeIndexSnapshotsData`**: CBOE Index Snapshots Data.

**Class `CboeIndexSnapshotsFetcher`**: Transform the query, extract and transform the data from the CBOE endpoints

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.index_snapshots`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `openbb_core.provider.utils.helpers`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:37.467975
- Generator: World's Best Repo Book Generator v1.0.0
