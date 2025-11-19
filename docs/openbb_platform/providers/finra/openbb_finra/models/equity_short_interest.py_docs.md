# File Documentation: equity_short_interest.py

## Metadata
- **Path**: `openbb_platform/providers/finra/openbb_finra/models/equity_short_interest.py`
- **Size**: 2,985 bytes
- **Lines**: 89
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `equity_short_interest.py`.

**Python Module**

- **Classes** (3): FinraShortInterestQueryParams, FinraShortInterestData, FinraShortInterestFetcher
- **Functions** (3): transform_query, extract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FinraShortInterestQueryParams`**(ShortInterestQueryParams)
- **`FinraShortInterestData`**(ShortInterestData)
- **`FinraShortInterestFetcher`**(
    Fetcher[FinraShortInterestQueryParams, list[FinraShortInterestData]]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `get_db_path`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_short_interest`
- `openbb_finra.utils.data_storage`
- `sqlite3`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:49.787678Z
**Generator**: World's Best Repo Book Generator v1.0
