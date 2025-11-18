# Documentation: openbb_platform/providers/finra/openbb_finra/models/equity_short_interest.py

## File Metadata
- **Path**: `openbb_platform/providers/finra/openbb_finra/models/equity_short_interest.py`
- **Size**: 2,985 characters, 89 lines
- **Words**: 225
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FINRA Equity Short Interest Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_short_interest import (
    ShortInterestData,
    ShortInterestQueryParams,
)


class FinraShortInterestQueryParams(ShortInterestQueryParams):
    """FINRA Equity Short Interest Query."""


class FinraShortInterestData(ShortInterestData):
    """FINRA Equity Short Interest Data."""

    __alias_dict__ = {
        "symbol": "symbolCode",
        "issue_name": "issueName",
        "market_class": "marketClassCode",
        "current_short_position": "currentShortPositionQuantity",
        "previous_short_position": "previousShortPositionQuantity",
        "avg_daily_volume": "averageDailyVolumeQuantity",
        "days_to_cover": "daysToCoverQuantity",
        "change": "changePreviousNumber",
        "change_pct": "changePercent",
        "settlement_date": "settlementDate",
    }


class FinraShortInterestFetcher(
    Fetcher[FinraShortInterestQueryParams, list[FinraShortInterestData]]
):
    """Transform the query, extract and transform the data from the FINRA endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FinraShortInterestQueryParams:
        """Transform query params."""
        return FinraShortInterestQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FinraShortInterestQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract the data from the Finra endpoint."""
        # pylint: disable=import-outside-toplevel
        import sqlite3  # noqa
        from openbb_finra.utils.data_storage import get_db_path, prepare_data  # noqa

        DB_PATH = get_db_path()
        # Put the data in the cache
        prepare_data()
        # Get the data from the cache
        cnx = sqlite3.connect(DB_PATH)
        cursor = cnx.cursor()
        cursor.execute(
            "SELECT * FROM short_interest where symbolCode = ?", (query.symbol,)
        )
        # TODO: Check if we should allow general queries, it's more than 500k rows
        # cursor.execute("SELECT * FROM short_interest")
        result = cursor.fetchall()

        titles = [
            "symbolCode",
            "issueName",
            "marketClassCode",
            "currentShortPositionQuantity",
            "previousShortPositionQuantity",
            "averageDailyVolumeQuantity",
            "daysToCoverQuantity",
            "changePercent",
            "changePreviousNumber",
            "settlementDate",
        ]
        return [dict(zip(titles, list(row)[1:])) for row in result]

    @staticmethod
    def transform_data(
        query: FinraShortInterestQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FinraShortInterestData]:
        """Transform the data."""
        return [FinraShortInterestData.model_validate(d) for d in data]

```

## High-Level Overview

FINRA Equity Short Interest Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_short_interest import (
ShortInterestData,
ShortInterestQueryParams,
)


class FinraShortInterestQueryParams(ShortInterestQueryParams):
FINRA Equity Short Interest Query.
FINRA Equity Short Interest Data.

__alias_dict__ = {
"symbol": "symbolCode",
"issue_name": "issueName",

## Detailed Structure

### Python File Structure

**Classes** (3):
`FinraShortInterestQueryParams`, `FinraShortInterestData`, `FinraShortInterestFetcher`

**Functions** (3):
`transform_query`, `extract_data`, `transform_data`

**Imports** (11):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.equity_short_interest`, `the`, `the`, `sqlite3`, `openbb_finra.utils.data_storage`, `get_db_path`, `the`


## Key Components

**Class `FinraShortInterestQueryParams`**: FINRA Equity Short Interest Query.

**Class `FinraShortInterestData`**: FINRA Equity Short Interest Data.

**Class `FinraShortInterestFetcher`**: Transform the query, extract and transform the data from the FINRA endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_short_interest`
- `sqlite3`
- `openbb_finra.utils.data_storage`

## Notes
- Generated: 2025-11-18T07:54:38.616110
- Generator: World's Best Repo Book Generator v1.0.0
