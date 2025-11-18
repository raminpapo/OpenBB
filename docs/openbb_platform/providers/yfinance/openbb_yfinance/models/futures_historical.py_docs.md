# Documentation: openbb_platform/providers/yfinance/openbb_yfinance/models/futures_historical.py

## File Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/futures_historical.py`
- **Size**: 4,807 characters, 152 lines
- **Words**: 328
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Yahoo Finance Futures Historical Price Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.futures_historical import (
    FuturesHistoricalData,
    FuturesHistoricalQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_yfinance.utils.references import INTERVALS_DICT, MONTHS
from pydantic import Field, field_validator


class YFinanceFuturesHistoricalQueryParams(FuturesHistoricalQueryParams):
    """Yahoo Finance Futures historical Price Query.

    Source: https://finance.yahoo.com/crypto/
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

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


class YFinanceFuturesHistoricalData(FuturesHistoricalData):
    """Yahoo Finance Futures Historical Price Data."""

    @field_validator("date", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):
        """Return datetime object from string."""
        # pylint: disable=import-outside-toplevel
        from pandas import Timestamp

        if isinstance(v, Timestamp):
            return v.to_pydatetime()
        return v


class YFinanceFuturesHistoricalFetcher(
    Fetcher[
        YFinanceFuturesHistoricalQueryParams,
        list[YFinanceFuturesHistoricalData],
    ]
):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFinanceFuturesHistoricalQueryParams:
        """Transform the query."""
        # pylint: disable=import-outside-toplevel
        from dateutil.relativedelta import relativedelta
        from openbb_yfinance.utils.helpers import get_futures_data

        transformed_params = params.copy()

        symbols = params["symbol"].split(",")
        new_symbols = []
        futures_data = get_futures_data()
        for symbol in symbols:
            if params.get("expiration"):
                expiry_date = datetime.strptime(
                    transformed_params["expiration"], "%Y-%m"
                )
                if "." not in symbol:
                    exchange = futures_data[futures_data["Ticker"] == symbol][
                        "Exchange"
                    ].values[0]
                    new_symbol = f"{symbol}{MONTHS[expiry_date.month]}{str(expiry_date.year)[-2:]}.{exchange}"
                else:
                    new_symbol = symbol
                new_symbols.append(new_symbol)
            else:
                new_symbols.append(symbol)

        formatted_symbols = []
        for s in new_symbols:
            if "." not in s.upper() and "=F" not in s.upper():
                formatted_symbols.append(f"{s.upper()}=F")
            else:
                formatted_symbols.append(s.upper())

        transformed_params["symbol"] = ",".join(formatted_symbols)

        now = datetime.now()

        if params.get("start_date") is None:
            transformed_params["start_date"] = (now - relativedelta(years=1)).strftime(
                "%Y-%m-%d"
            )

        if params.get("end_date") is None:
            transformed_params["end_date"] = now.strftime("%Y-%m-%d")

        return YFinanceFuturesHistoricalQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: YFinanceFuturesHistoricalQueryParams,
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
            interval=INTERVALS_DICT[query.interval],  # type: ignore
            prepost=True,
            auto_adjust=False,
            actions=False,
        )

        if data.empty:
            raise EmptyDataError()

        return data.to_dict("records")

    @staticmethod
    def transform_data(
        query: YFinanceFuturesHistoricalQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFinanceFuturesHistoricalData]:
        """Transform the data to the standard format."""
        return [YFinanceFuturesHistoricalData.model_validate(d) for d in data]

```

## High-Level Overview

Yahoo Finance Futures Historical Price Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.futures_historical import (
FuturesHistoricalData,
FuturesHistoricalQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_yfinance.utils.references import INTERVALS_DICT, MONTHS
from pydantic import Field, field_validator


class YFinanceFuturesHistoricalQueryParams(FuturesHistoricalQueryParams):
Yahoo Finance Futures historical Price Query.

## Detailed Structure

### Python File Structure

**Classes** (3):
`YFinanceFuturesHistoricalQueryParams`, `YFinanceFuturesHistoricalData`, `YFinanceFuturesHistoricalFetcher`

**Functions** (4):
`date_validate`, `transform_query`, `extract_data`, `transform_data`

**Imports** (26):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.futures_historical`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `openbb_yfinance.utils.references`, `INTERVALS_DICT`, `pydantic`, `Field`, `string.`, `pandas`, `Timestamp`, `the`, `dateutil.relativedelta`


## Key Components

**Class `YFinanceFuturesHistoricalQueryParams`**: Yahoo Finance Futures historical Price Query.

    Source: https://finance.yahoo.com/crypto/

**Class `YFinanceFuturesHistoricalData`**: Yahoo Finance Futures Historical Price Data.

**Class `YFinanceFuturesHistoricalFetcher`**: Transform the query, extract and transform the data from the Yahoo Finance endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.futures_historical`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.errors`
- `openbb_yfinance.utils.references`
- `pydantic`
- `pandas`
- `dateutil.relativedelta`

## Notes
- Generated: 2025-11-18T07:54:43.575831
- Generator: World's Best Repo Book Generator v1.0.0
