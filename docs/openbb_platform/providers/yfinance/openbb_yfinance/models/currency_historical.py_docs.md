# File Documentation: currency_historical.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/currency_historical.py`
- **Size**: 3,816 bytes
- **Lines**: 136
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Yahoo Finance Currency Price Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.currency_historical import (
    CurrencyHistoricalData,
    CurrencyHistoricalQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_yfinance.utils.references import INTERVALS_DICT
from pydantic import Field


class YFinanceCurrencyHistoricalQueryParams(CurrencyHistoricalQueryParams):
    """Yahoo Finance Currency Price Query.

    Source: https://finance.yahoo.com/currencies/
    """

    __json_schema_extra__ = {
        "symbol": {"multiple_items_allowed": True},
        "interval": {
            "choices": [
                "1m",
                "2m",
                "5m",
                "15m",
                "30m",
                "60m",
                "90m",
                "1h",
                "1d",
                "5d",
                "1W",
                "1M",
                "1Q",
            ]
        },
    }

    interval: Literal[
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h",
        "1d",
        "5d",
        "1W",
        "1M",
        "1Q",
    ] = Field(
        default="1d",
        description=QUERY_DESCRIPTIONS.get("interval", ""),
    )


class YFinanceCurrencyHistoricalData(CurrencyHistoricalData):
    """Yahoo Finance Currency Price Data."""


class YFinanceCurrencyHistoricalFetcher(
    Fetcher[
        YFinanceCurrencyHistoricalQueryParams,
        list[YFinanceCurrencyHistoricalData],
    ]
):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> YFinanceCurrencyHistoricalQueryParams:
        """Transform the query."""
        # pylint: disable=import-outside-toplevel
        from dateutil.relativedelta import relativedelta

        transformed_params = params
        symbols = params["symbol"].split(",")
        new_symbols = [
            f"{s.upper()}=X" if "=X" not in s.upper() else s.upper() for s in symbols
        ]
        transformed_params["symbol"] = ",".join(new_symbols)

        now = datetime.now().date()

        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return YFinanceCurrencyHistoricalQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: YFinanceCurrencyHistoricalQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Yahoo Finance endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_yfinance.utils.helpers import yf_download

        data = yf_download(
            query.symbol,
            start_date=query.start_date,
            end_date=query.end_date,
            interval=INTERVALS_DICT.get(query.interval, "1d"),  # type: ignore
            auto_adjust=False,
            actions=False,
            prepost=True,
        )

        if data.empty:
            raise EmptyDataError()

        return data.to_dict("records")

    @staticmethod
    def transform_data(
        query: YFinanceCurrencyHistoricalQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFinanceCurrencyHistoricalData]:
        """Transform the data to the standard format."""
        return [YFinanceCurrencyHistoricalData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `currency_historical.py`.

**Python Module**

- **Classes** (3): YFinanceCurrencyHistoricalQueryParams, YFinanceCurrencyHistoricalData, YFinanceCurrencyHistoricalFetcher
- **Functions** (3): transform_query, extract_data, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFinanceCurrencyHistoricalQueryParams`**(CurrencyHistoricalQueryParams)
- **`YFinanceCurrencyHistoricalData`**(CurrencyHistoricalData)
- **`YFinanceCurrencyHistoricalFetcher`**(
    Fetcher[
        YFinanceCurrencyHistoricalQueryParams,
        list[YFinanceCurrencyHistoricalData],
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `EmptyDataError`
- `Fetcher`
- `Field`
- `INTERVALS_DICT`
- `QUERY_DESCRIPTIONS`
- `datetime`
- `dateutil.relativedelta`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.currency_historical`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.errors`
- `openbb_yfinance.utils.helpers`
- `openbb_yfinance.utils.references`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.165103Z
**Generator**: World's Best Repo Book Generator v1.0
