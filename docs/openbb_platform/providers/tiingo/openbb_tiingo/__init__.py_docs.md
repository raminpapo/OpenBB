# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/tiingo/openbb_tiingo/__init__.py`
- **Size**: 1,260 bytes
- **Lines**: 28
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Provider`
- `TiingoCompanyNewsFetcher`
- `TiingoCryptoHistoricalFetcher`
- `TiingoCurrencyHistoricalFetcher`
- `TiingoEquityHistoricalFetcher`
- `TiingoTrailingDivYieldFetcher`
- `TiingoWorldNewsFetcher`
- `openbb_core.provider.abstract.provider`
- `openbb_tiingo.models.company_news`
- `openbb_tiingo.models.crypto_historical`
- `openbb_tiingo.models.currency_historical`
- `openbb_tiingo.models.equity_historical`
- `openbb_tiingo.models.trailing_dividend_yield`
- `openbb_tiingo.models.world_news`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:53.003823Z
**Generator**: World's Best Repo Book Generator v1.0
