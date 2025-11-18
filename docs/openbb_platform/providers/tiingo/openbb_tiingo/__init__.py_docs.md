# Documentation: openbb_platform/providers/tiingo/openbb_tiingo/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/tiingo/openbb_tiingo/__init__.py`
- **Size**: 1,260 characters, 28 lines
- **Words**: 70
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tiingo provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_tiingo.models.company_news import TiingoCompanyNewsFetcher
from openbb_tiingo.models.crypto_historical import TiingoCryptoHistoricalFetcher
from openbb_tiingo.models.currency_historical import TiingoCurrencyHistoricalFetcher
from openbb_tiingo.models.equity_historical import TiingoEquityHistoricalFetcher
from openbb_tiingo.models.trailing_dividend_yield import TiingoTrailingDivYieldFetcher
from openbb_tiingo.models.world_news import TiingoWorldNewsFetcher

tiingo_provider = Provider(
    name="tiingo",
    website="https://tiingo.com",
    description="""A Reliable, Enterprise-Grade Financial Markets API. Tiingo's APIs
power hedge funds, tech companies, and individuals.""",
    credentials=["token"],
    fetcher_dict={
        "EquityHistorical": TiingoEquityHistoricalFetcher,
        "EtfHistorical": TiingoEquityHistoricalFetcher,
        "CompanyNews": TiingoCompanyNewsFetcher,
        "WorldNews": TiingoWorldNewsFetcher,
        "CryptoHistorical": TiingoCryptoHistoricalFetcher,
        "CurrencyHistorical": TiingoCurrencyHistoricalFetcher,
        "TrailingDividendYield": TiingoTrailingDivYieldFetcher,
    },
    repr_name="Tiingo",
)

```

## High-Level Overview

Tiingo provider module.

from openbb_core.provider.abstract.provider import Provider
from openbb_tiingo.models.company_news import TiingoCompanyNewsFetcher
from openbb_tiingo.models.crypto_historical import TiingoCryptoHistoricalFetcher
from openbb_tiingo.models.currency_historical import TiingoCurrencyHistoricalFetcher
from openbb_tiingo.models.equity_historical import TiingoEquityHistoricalFetcher
from openbb_tiingo.models.trailing_dividend_yield import TiingoTrailingDivYieldFetcher
from openbb_tiingo.models.world_news import TiingoWorldNewsFetcher

tiingo_provider = Provider(
name="tiingo",
website="https://tiingo.com",
description="""A Reliable, Enterprise-Grade Financial Markets API. Tiingo's APIs
power hedge funds, tech companies, and individuals.""",
credentials=["token"],
fetcher_dict={
"EquityHistorical": TiingoEquityHistoricalFetcher,
"EtfHistorical": TiingoEquityHistoricalFetcher,
"CompanyNews": TiingoCompanyNewsFetcher,

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (14):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_tiingo.models.company_news`, `TiingoCompanyNewsFetcher`, `openbb_tiingo.models.crypto_historical`, `TiingoCryptoHistoricalFetcher`, `openbb_tiingo.models.currency_historical`, `TiingoCurrencyHistoricalFetcher`, `openbb_tiingo.models.equity_historical`, `TiingoEquityHistoricalFetcher`, `openbb_tiingo.models.trailing_dividend_yield`, `TiingoTrailingDivYieldFetcher`, `openbb_tiingo.models.world_news`, `TiingoWorldNewsFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_tiingo.models.company_news`
- `openbb_tiingo.models.crypto_historical`
- `openbb_tiingo.models.currency_historical`
- `openbb_tiingo.models.equity_historical`
- `openbb_tiingo.models.trailing_dividend_yield`
- `openbb_tiingo.models.world_news`

## Notes
- Generated: 2025-11-18T07:54:41.709743
- Generator: World's Best Repo Book Generator v1.0.0
