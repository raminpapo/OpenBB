# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/index_historical.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/index_historical.py`
- **Size**: 3,602 characters, 117 lines
- **Words**: 280
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Index Historical Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_historical import (
    IndexHistoricalData,
    IndexHistoricalQueryParams,
)
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class FMPIndexHistoricalQueryParams(IndexHistoricalQueryParams):
    """FMP Index Historical Query.

    Source: https://site.financialmodelingprep.com/developer/docs/historical-index-price-api/
    """

    __alias_dict__ = {"start_date": "from", "end_date": "to"}
    __json_schema_extra__ = {
        "symbol": {"multiple_items_allowed": True},
    }

    interval: Literal["1m", "5m", "1h", "1d"] = Field(
        default="1d", description=QUERY_DESCRIPTIONS.get("interval", "")
    )


class FMPIndexHistoricalData(IndexHistoricalData):
    """FMP Index Historical Data."""

    vwap: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("vwap", "")
    )
    change: float | None = Field(
        default=None,
        description="Change in the price from the previous close.",
    )
    change_percent: float | None = Field(
        default=None,
        description="Change in the price from the previous close, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

    @field_validator("change_percent", mode="before", check_fields=False)
    @classmethod
    def _normalize_percent(cls, v):
        """Normalize percent values."""
        return v / 100 if v else None


class FMPIndexHistoricalFetcher(
    Fetcher[
        FMPIndexHistoricalQueryParams,
        list[FMPIndexHistoricalData],
    ]
):
    """FMP Index Historical Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPIndexHistoricalQueryParams:
        """Transform the query params."""
        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return FMPIndexHistoricalQueryParams.model_validate(transformed_params)

    @staticmethod
    async def aextract_data(
        query: FMPIndexHistoricalQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_historical_ohlc

        return await get_historical_ohlc(query, credentials, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPIndexHistoricalQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[FMPIndexHistoricalData]:
        """Return the transformed data."""
        if not data:
            raise EmptyDataError()

        return [
            FMPIndexHistoricalData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: (
                    (x["date"], x["symbol"])
                    if len(query.symbol.split(",")) > 1
                    else x["date"]
                ),
                reverse=False,
            )
        ]

```

## High-Level Overview

FMP Index Historical Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_historical import (
IndexHistoricalData,
IndexHistoricalQueryParams,
)
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPIndexHistoricalQueryParams`, `FMPIndexHistoricalData`, `FMPIndexHistoricalFetcher`

**Functions** (4):
`_normalize_percent`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (19):
`datetime`, `datetime`, `typing`, `Any`, `dateutil.relativedelta`, `relativedelta`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.index_historical`, `openbb_core.provider.utils.descriptions`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `the`, `the`, `the`, `openbb_fmp.utils.helpers`, `get_historical_ohlc`


## Key Components

**Class `FMPIndexHistoricalQueryParams`**: FMP Index Historical Query.

    Source: https://site.financialmodelingprep.com/developer/docs/historical-index-price-api/

**Class `FMPIndexHistoricalData`**: FMP Index Historical Data.

**Class `FMPIndexHistoricalFetcher`**: FMP Index Historical Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `dateutil.relativedelta`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.index_historical`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `openbb_fmp.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:39.395835
- Generator: World's Best Repo Book Generator v1.0.0
