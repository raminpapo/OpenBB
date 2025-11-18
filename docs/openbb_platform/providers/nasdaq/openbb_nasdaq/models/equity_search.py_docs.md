# Documentation: openbb_platform/providers/nasdaq/openbb_nasdaq/models/equity_search.py

## File Metadata
- **Path**: `openbb_platform/providers/nasdaq/openbb_nasdaq/models/equity_search.py`
- **Size**: 4,396 characters, 149 lines
- **Words**: 352
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Nasdaq Equity Search Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_search import (
    EquitySearchData,
    EquitySearchQueryParams,
)
from pydantic import Field


class NasdaqEquitySearchQueryParams(EquitySearchQueryParams):
    """Nasdaq Equity Search Query.

    Source: ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqtraded.txt
    """

    is_etf: bool = Field(
        default=False,
        description="If True, returns only ETFs.",
    )


class NasdaqEquitySearchData(EquitySearchData):
    """Nasdaq Equity Search Data."""

    __alias_dict__ = {
        "symbol": "Symbol",
        "name": "Security Name",
        "nasdaq_traded": "Nasdaq Traded",
        "exchange": "listing Exchange",
        "market_category": "Market Category",
        "etf": "ETF",
        "round_lot_size": "Round Lot Size",
        "test_issue": "Test Issue",
        "financial_status": "Financial Status",
        "cqs_symbol": "CQS Symbol",
        "nasdaq_symbol": "NASDAQ Symbol",
        "next_shares": "NextShares",
    }

    nasdaq_traded: str | None = Field(
        default=None,
        description="Is Nasdaq traded?",
    )
    exchange: str | None = Field(
        default=None,
        description="Primary Exchange",
    )
    market_category: str | None = Field(
        default=None,
        description="Market Category",
    )
    etf: str | None = Field(
        default=None,
        description="Is ETF?",
    )
    round_lot_size: float | None = Field(
        default=None,
        description="Round Lot Size",
    )
    test_issue: str | None = Field(
        default=None,
        description="Is test Issue?",
    )
    financial_status: str | None = Field(
        default=None,
        description="Financial Status",
    )
    cqs_symbol: str | None = Field(
        default=None,
        description="CQS Symbol",
    )
    nasdaq_symbol: str | None = Field(
        default=None,
        description="NASDAQ Symbol",
    )
    next_shares: str | None = Field(
        default=None,
        description="Is NextShares?",
    )


class NasdaqEquitySearchFetcher(
    Fetcher[NasdaqEquitySearchQueryParams, list[NasdaqEquitySearchData]]
):
    """Nasdaq Equity Search Fetcher."""

    require_credentials = False

    @staticmethod
    def transform_query(params: dict[str, Any]) -> NasdaqEquitySearchQueryParams:
        """Transform the query parameters."""
        return NasdaqEquitySearchQueryParams(**params)

    @staticmethod
    def extract_data(
        query: NasdaqEquitySearchQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> str:
        """Extract data from Nasdaq."""
        # pylint: disable=import-outside-toplevel
        from openbb_nasdaq.utils.helpers import get_nasdaq_directory

        return get_nasdaq_directory()

    @staticmethod
    def transform_data(
        query: NasdaqEquitySearchQueryParams,
        data: str,
        **kwargs: Any,
    ) -> list[NasdaqEquitySearchData]:
        """Transform the data and filter the results."""
        # pylint: disable=import-outside-toplevel
        from io import StringIO  # noqa
        from numpy import nan
        from pandas import read_csv

        directory = read_csv(StringIO(data), sep="|").iloc[:-1]

        if query.is_etf is True:
            directory = directory[directory["ETF"] == "Y"]
        if query.is_etf is False:
            directory = directory[directory["ETF"] == "N"]

        directory = directory[
            ~directory["Security Name"].str.contains("test", case=False)
        ]

        if query.query:
            directory = directory[
                directory["Symbol"].str.contains(query.query, case=False)
                | directory["Security Name"].str.contains(query.query, case=False)
                | directory["CQS Symbol"].str.contains(query.query, case=False)
                | directory["NASDAQ Symbol"].str.contains(query.query, case=False)
            ]
        directory["Market Category"] = directory["Market Category"].replace(" ", None)
        results = (
            directory.infer_objects(copy=False)
            .replace({nan: None})
            .to_dict(orient="records")
        )

        return [NasdaqEquitySearchData.model_validate(d) for d in results]

```

## High-Level Overview

Nasdaq Equity Search Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_search import (
EquitySearchData,
EquitySearchQueryParams,
)
from pydantic import Field


class NasdaqEquitySearchQueryParams(EquitySearchQueryParams):
Nasdaq Equity Search Query.


is_etf: bool = Field(
default=False,

## Detailed Structure

### Python File Structure

**Classes** (3):
`NasdaqEquitySearchQueryParams`, `NasdaqEquitySearchData`, `NasdaqEquitySearchFetcher`

**Functions** (3):
`transform_query`, `extract_data`, `transform_data`

**Imports** (16):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.equity_search`, `pydantic`, `Field`, `Nasdaq.`, `openbb_nasdaq.utils.helpers`, `get_nasdaq_directory`, `io`, `StringIO`, `numpy`, `nan`, `pandas`, `read_csv`


## Key Components

**Class `NasdaqEquitySearchQueryParams`**: Nasdaq Equity Search Query.

    Source: ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqtraded.txt

**Class `NasdaqEquitySearchData`**: Nasdaq Equity Search Data.

**Class `NasdaqEquitySearchFetcher`**: Nasdaq Equity Search Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_search`
- `pydantic`
- `openbb_nasdaq.utils.helpers`
- `io`
- `numpy`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:40.326122
- Generator: World's Best Repo Book Generator v1.0.0
