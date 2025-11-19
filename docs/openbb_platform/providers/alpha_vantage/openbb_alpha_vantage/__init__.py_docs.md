# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/alpha_vantage/openbb_alpha_vantage/__init__.py`
- **Size**: 1,485 bytes
- **Lines**: 27
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Alpha Vantage Provider module."""

from openbb_alpha_vantage.models.equity_historical import AVEquityHistoricalFetcher
from openbb_alpha_vantage.models.historical_eps import AVHistoricalEpsFetcher
from openbb_core.provider.abstract.provider import Provider

alpha_vantage_provider = Provider(
    name="alpha_vantage",
    website="https://www.alphavantage.co",
    description="""Alpha Vantage provides realtime and historical
financial market data through a set of powerful and developer-friendly data APIs
and spreadsheets. From traditional asset classes (e.g., stocks, ETFs, mutual funds)
to economic indicators, from foreign exchange rates to commodities,
from fundamental data to technical indicators, Alpha Vantage
is your one-stop-shop for enterprise-grade global market data delivered through
cloud-based APIs, Excel, and Google Sheets. """,
    credentials=["api_key"],
    fetcher_dict={
        "EquityHistorical": AVEquityHistoricalFetcher,
        "HistoricalEps": AVHistoricalEpsFetcher,
        "EtfHistorical": AVEquityHistoricalFetcher,
    },
    repr_name="Alpha Vantage",
    deprecated_credentials={"API_KEY_ALPHAVANTAGE": "alpha_vantage_api_key"},
    instructions='Go to: https://www.alphavantage.co/support/#api-key\n\n![AlphaVantage](https://user-images.githubusercontent.com/46355364/207820936-46c2ba00-81ff-4cd3-98a4-4fa44412996f.png)\n\nFill out the form, pass Captcha, and click on, "GET FREE API KEY".',  # noqa: E501  pylint: disable=line-too-long
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
- `AVEquityHistoricalFetcher`
- `AVHistoricalEpsFetcher`
- `Provider`
- `openbb_alpha_vantage.models.equity_historical`
- `openbb_alpha_vantage.models.historical_eps`
- `openbb_core.provider.abstract.provider`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.243391Z
**Generator**: World's Best Repo Book Generator v1.0
