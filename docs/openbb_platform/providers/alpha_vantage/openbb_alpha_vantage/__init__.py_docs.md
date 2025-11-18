# Documentation: openbb_platform/providers/alpha_vantage/openbb_alpha_vantage/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/alpha_vantage/openbb_alpha_vantage/__init__.py`
- **Size**: 1,485 characters, 27 lines
- **Words**: 118
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Alpha Vantage Provider module.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (8):
`openbb_alpha_vantage.models.equity_historical`, `AVEquityHistoricalFetcher`, `openbb_alpha_vantage.models.historical_eps`, `AVHistoricalEpsFetcher`, `openbb_core.provider.abstract.provider`, `Provider`, `foreign`, `fundamental`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_alpha_vantage.models.equity_historical`
- `openbb_alpha_vantage.models.historical_eps`
- `openbb_core.provider.abstract.provider`

## Notes
- Generated: 2025-11-18T07:54:37.242264
- Generator: World's Best Repo Book Generator v1.0.0
