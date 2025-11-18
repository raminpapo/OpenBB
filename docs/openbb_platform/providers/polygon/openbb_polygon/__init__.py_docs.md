# Documentation: openbb_platform/providers/polygon/openbb_polygon/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/polygon/openbb_polygon/__init__.py`
- **Size**: 2,842 characters, 45 lines
- **Words**: 159
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Polygon provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_polygon.models.balance_sheet import PolygonBalanceSheetFetcher
from openbb_polygon.models.cash_flow import PolygonCashFlowStatementFetcher
from openbb_polygon.models.company_news import PolygonCompanyNewsFetcher
from openbb_polygon.models.crypto_historical import PolygonCryptoHistoricalFetcher
from openbb_polygon.models.currency_historical import PolygonCurrencyHistoricalFetcher
from openbb_polygon.models.currency_pairs import PolygonCurrencyPairsFetcher
from openbb_polygon.models.currency_snapshots import PolygonCurrencySnapshotsFetcher
from openbb_polygon.models.equity_historical import PolygonEquityHistoricalFetcher
from openbb_polygon.models.equity_nbbo import PolygonEquityNBBOFetcher
from openbb_polygon.models.income_statement import PolygonIncomeStatementFetcher
from openbb_polygon.models.index_historical import (
    PolygonIndexHistoricalFetcher,
)
from openbb_polygon.models.market_snapshots import PolygonMarketSnapshotsFetcher

polygon_provider = Provider(
    name="polygon",
    website="https://polygon.io",
    description="""The Polygon.io Stocks API provides REST endpoints that let you query
the latest market data from all US stock exchanges. You can also find data on
company financials, stock market holidays, corporate actions, and more.""",
    credentials=["api_key"],
    fetcher_dict={
        "BalanceSheet": PolygonBalanceSheetFetcher,
        "CashFlowStatement": PolygonCashFlowStatementFetcher,
        "CompanyNews": PolygonCompanyNewsFetcher,
        "CryptoHistorical": PolygonCryptoHistoricalFetcher,
        "CurrencyHistorical": PolygonCurrencyHistoricalFetcher,
        "CurrencyPairs": PolygonCurrencyPairsFetcher,
        "CurrencySnapshots": PolygonCurrencySnapshotsFetcher,
        "EquityHistorical": PolygonEquityHistoricalFetcher,
        "EquityNBBO": PolygonEquityNBBOFetcher,
        "EtfHistorical": PolygonEquityHistoricalFetcher,
        "IncomeStatement": PolygonIncomeStatementFetcher,
        "IndexHistorical": PolygonIndexHistoricalFetcher,
        "MarketSnapshots": PolygonMarketSnapshotsFetcher,
    },
    repr_name="Polygon.io",
    deprecated_credentials={"API_POLYGON_KEY": "polygon_api_key"},
    instructions='Go to: https://polygon.io\n\n![Polygon](https://user-images.githubusercontent.com/46355364/207825623-fcd7f0a3-131a-4294-808c-754c13e38e2a.png)\n\nClick on, "Get your Free API Key".\n\n![Polygon](https://user-images.githubusercontent.com/46355364/207825952-ca5540ec-6ed2-4cef-a0ed-bb50b813932c.png)\n\nAfter signing up, the API Key is found at the bottom of the account dashboard page.\n\n![Polygon](https://user-images.githubusercontent.com/46355364/207826258-b1f318fa-fd9c-41d9-bf5c-fe16722e6601.png)',  # noqa: E501  pylint: disable=line-too-long
)

```

## High-Level Overview

Polygon provider module.

from openbb_core.provider.abstract.provider import Provider
from openbb_polygon.models.balance_sheet import PolygonBalanceSheetFetcher
from openbb_polygon.models.cash_flow import PolygonCashFlowStatementFetcher
from openbb_polygon.models.company_news import PolygonCompanyNewsFetcher
from openbb_polygon.models.crypto_historical import PolygonCryptoHistoricalFetcher
from openbb_polygon.models.currency_historical import PolygonCurrencyHistoricalFetcher
from openbb_polygon.models.currency_pairs import PolygonCurrencyPairsFetcher
from openbb_polygon.models.currency_snapshots import PolygonCurrencySnapshotsFetcher
from openbb_polygon.models.equity_historical import PolygonEquityHistoricalFetcher
from openbb_polygon.models.equity_nbbo import PolygonEquityNBBOFetcher
from openbb_polygon.models.income_statement import PolygonIncomeStatementFetcher
from openbb_polygon.models.index_historical import (
PolygonIndexHistoricalFetcher,
)
from openbb_polygon.models.market_snapshots import PolygonMarketSnapshotsFetcher

polygon_provider = Provider(
name="polygon",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (26):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_polygon.models.balance_sheet`, `PolygonBalanceSheetFetcher`, `openbb_polygon.models.cash_flow`, `PolygonCashFlowStatementFetcher`, `openbb_polygon.models.company_news`, `PolygonCompanyNewsFetcher`, `openbb_polygon.models.crypto_historical`, `PolygonCryptoHistoricalFetcher`, `openbb_polygon.models.currency_historical`, `PolygonCurrencyHistoricalFetcher`, `openbb_polygon.models.currency_pairs`, `PolygonCurrencyPairsFetcher`, `openbb_polygon.models.currency_snapshots`, `PolygonCurrencySnapshotsFetcher`, `openbb_polygon.models.equity_historical`, `PolygonEquityHistoricalFetcher`, `openbb_polygon.models.equity_nbbo`, `PolygonEquityNBBOFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_polygon.models.balance_sheet`
- `openbb_polygon.models.cash_flow`
- `openbb_polygon.models.company_news`
- `openbb_polygon.models.crypto_historical`
- `openbb_polygon.models.currency_historical`
- `openbb_polygon.models.currency_pairs`
- `openbb_polygon.models.currency_snapshots`
- `openbb_polygon.models.equity_historical`
- `openbb_polygon.models.equity_nbbo`

## Notes
- Generated: 2025-11-18T07:54:40.488887
- Generator: World's Best Repo Book Generator v1.0.0
