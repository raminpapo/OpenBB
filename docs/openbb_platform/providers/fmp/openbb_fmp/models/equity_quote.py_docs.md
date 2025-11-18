# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/equity_quote.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/equity_quote.py`
- **Size**: 4,200 characters, 125 lines
- **Words**: 358
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Equity Quote Model."""

# pylint: disable=unused-argument

from datetime import date as dateType
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_quote import (
    EquityQuoteData,
    EquityQuoteQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class FMPEquityQuoteQueryParams(EquityQuoteQueryParams):
    """FMP Equity Quote Query.

    Source: https://site.financialmodelingprep.com/developer/docs#quote
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class FMPEquityQuoteData(EquityQuoteData):
    """FMP Equity Quote Data."""

    __alias_dict__ = {
        "ma50": "priceAvg50",
        "ma200": "priceAvg200",
        "last_timestamp": "timestamp",
        "high": "dayHigh",
        "low": "dayLow",
        "last_price": "price",
        "change_percent": "changePercentage",
        "prev_close": "previousClose",
    }
    ma50: float | None = Field(default=None, description="50 day moving average price.")
    ma200: float | None = Field(
        default=None, description="200 day moving average price."
    )
    market_cap: float | None = Field(
        default=None, description="Market cap of the company."
    )

    @field_validator("last_timestamp", mode="before", check_fields=False)
    @classmethod
    def validate_last_timestamp(cls, v: str | int) -> dateType | None:
        """Return the date as a datetime object."""
        # pylint: disable=import-outside-toplevel
        from datetime import timezone  # noqa
        from openbb_core.provider.utils.helpers import safe_fromtimestamp

        if v:
            v = int(v) if isinstance(v, str) else v
            return safe_fromtimestamp(v, tz=timezone.utc).replace(tzinfo=None)
        return None

    @field_validator("change_percent", mode="after", check_fields=False)
    @classmethod
    def _normalize_percent(cls, v):  # pylint: disable=E0213
        """Return the percent value as a normalized value."""
        return float(v) / 100 if v else None


class FMPEquityQuoteFetcher(
    Fetcher[
        FMPEquityQuoteQueryParams,
        list[FMPEquityQuoteData],
    ]
):
    """FMP Equity Quote Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPEquityQuoteQueryParams:
        """Transform the query params."""
        return FMPEquityQuoteQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPEquityQuoteQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        import warnings
        from openbb_core.provider.utils.helpers import amake_request
        from openbb_fmp.utils.helpers import response_callback

        api_key = credentials.get("fmp_api_key") if credentials else ""
        base_url = "https://financialmodelingprep.com/stable/quote?"
        symbols = query.symbol.split(",")
        results: list = []

        async def get_one(symbol):
            """Get data for one symbol."""
            url = f"{base_url}symbol={symbol}&apikey={api_key}"
            result = await amake_request(
                url, response_callback=response_callback, **kwargs
            )
            if not result or len(result) == 0:
                warnings.warn(f"Symbol Error: No data found for {symbol}")
            if result and len(result) > 0:
                results.extend(result)

        await asyncio.gather(*[get_one(s) for s in symbols])

        if not results:
            raise EmptyDataError("No data found for the given symbols.")

        return sorted(
            results,
            key=(lambda item: (symbols.index(item.get("symbol", len(symbols))))),
        )

    @staticmethod
    def transform_data(
        query: FMPEquityQuoteQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPEquityQuoteData]:
        """Return the transformed data."""
        return [FMPEquityQuoteData.model_validate(d) for d in data]

```

## High-Level Overview

FMP Equity Quote Model.

# pylint: disable=unused-argument

from datetime import date as dateType
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_quote import (
EquityQuoteData,
EquityQuoteQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class FMPEquityQuoteQueryParams(EquityQuoteQueryParams):
FMP Equity Quote Query.



## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPEquityQuoteQueryParams`, `FMPEquityQuoteData`, `FMPEquityQuoteFetcher`

**Functions** (6):
`validate_last_timestamp`, `_normalize_percent`, `transform_query`, `aextract_data`, `get_one`, `transform_data`

**Imports** (22):
`datetime`, `date`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.equity_quote`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `datetime`, `timezone`, `openbb_core.provider.utils.helpers`, `safe_fromtimestamp`, `the`, `asyncio`, `warnings`, `openbb_core.provider.utils.helpers`, `amake_request`


## Key Components

**Class `FMPEquityQuoteQueryParams`**: FMP Equity Quote Query.

    Source: https://site.financialmodelingprep.com/developer/docs#quote

**Class `FMPEquityQuoteData`**: FMP Equity Quote Data.

**Class `FMPEquityQuoteFetcher`**: FMP Equity Quote Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_quote`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `datetime`
- `openbb_core.provider.utils.helpers`
- `asyncio`
- `warnings`

## Notes
- Generated: 2025-11-18T07:54:39.357924
- Generator: World's Best Repo Book Generator v1.0.0
