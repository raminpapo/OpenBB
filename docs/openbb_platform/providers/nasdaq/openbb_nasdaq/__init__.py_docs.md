# Documentation: openbb_platform/providers/nasdaq/openbb_nasdaq/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/nasdaq/openbb_nasdaq/__init__.py`
- **Size**: 2,327 characters, 36 lines
- **Words**: 130
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Nasdaq provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_nasdaq.models.calendar_dividend import NasdaqCalendarDividendFetcher
from openbb_nasdaq.models.calendar_earnings import NasdaqCalendarEarningsFetcher
from openbb_nasdaq.models.calendar_ipo import NasdaqCalendarIpoFetcher
from openbb_nasdaq.models.company_filings import NasdaqCompanyFilingsFetcher
from openbb_nasdaq.models.economic_calendar import NasdaqEconomicCalendarFetcher
from openbb_nasdaq.models.equity_screener import NasdaqEquityScreenerFetcher
from openbb_nasdaq.models.equity_search import NasdaqEquitySearchFetcher
from openbb_nasdaq.models.historical_dividends import NasdaqHistoricalDividendsFetcher
from openbb_nasdaq.models.top_retail import NasdaqTopRetailFetcher

nasdaq_provider = Provider(
    name="nasdaq",
    website="https://data.nasdaq.com",
    description="""Positioned at the nexus of technology and the capital markets, Nasdaq
provides premier platforms and services for global capital markets and beyond with
unmatched technology, insights and markets expertise.""",
    credentials=["api_key"],
    fetcher_dict={
        "CalendarDividend": NasdaqCalendarDividendFetcher,
        "CalendarEarnings": NasdaqCalendarEarningsFetcher,
        "CalendarIpo": NasdaqCalendarIpoFetcher,
        "CompanyFilings": NasdaqCompanyFilingsFetcher,
        "EconomicCalendar": NasdaqEconomicCalendarFetcher,
        "EquitySearch": NasdaqEquitySearchFetcher,
        "EquityScreener": NasdaqEquityScreenerFetcher,
        "HistoricalDividends": NasdaqHistoricalDividendsFetcher,
        "TopRetail": NasdaqTopRetailFetcher,
    },
    repr_name="NASDAQ",
    deprecated_credentials={"API_KEY_QUANDL": "nasdaq_api_key"},
    instructions='Go to: https://www.quandl.com\n\n![Quandl](https://user-images.githubusercontent.com/46355364/207823899-208a3952-f557-4b73-aee6-64ac00faedb7.png)\n\nClick on, "Sign Up", and register a new account.\n\n![Quandl](https://user-images.githubusercontent.com/46355364/207824214-4b6b2b74-e709-4ed4-adf2-14803e6f3568.png)\n\nFollow the sign-up instructions, and upon completion the API key will be assigned.\n\n![Quandl](https://user-images.githubusercontent.com/46355364/207824664-3c82befb-9c69-42df-8a82-510d85c19a97.png)',  # noqa: E501  pylint: disable=line-too-long
)

```

## High-Level Overview

Nasdaq provider module.

from openbb_core.provider.abstract.provider import Provider
from openbb_nasdaq.models.calendar_dividend import NasdaqCalendarDividendFetcher
from openbb_nasdaq.models.calendar_earnings import NasdaqCalendarEarningsFetcher
from openbb_nasdaq.models.calendar_ipo import NasdaqCalendarIpoFetcher
from openbb_nasdaq.models.company_filings import NasdaqCompanyFilingsFetcher
from openbb_nasdaq.models.economic_calendar import NasdaqEconomicCalendarFetcher
from openbb_nasdaq.models.equity_screener import NasdaqEquityScreenerFetcher
from openbb_nasdaq.models.equity_search import NasdaqEquitySearchFetcher
from openbb_nasdaq.models.historical_dividends import NasdaqHistoricalDividendsFetcher
from openbb_nasdaq.models.top_retail import NasdaqTopRetailFetcher

nasdaq_provider = Provider(
name="nasdaq",
website="https://data.nasdaq.com",
description="""Positioned at the nexus of technology and the capital markets, Nasdaq
provides premier platforms and services for global capital markets and beyond with
unmatched technology, insights and markets expertise.""",
credentials=["api_key"],

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (20):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_nasdaq.models.calendar_dividend`, `NasdaqCalendarDividendFetcher`, `openbb_nasdaq.models.calendar_earnings`, `NasdaqCalendarEarningsFetcher`, `openbb_nasdaq.models.calendar_ipo`, `NasdaqCalendarIpoFetcher`, `openbb_nasdaq.models.company_filings`, `NasdaqCompanyFilingsFetcher`, `openbb_nasdaq.models.economic_calendar`, `NasdaqEconomicCalendarFetcher`, `openbb_nasdaq.models.equity_screener`, `NasdaqEquityScreenerFetcher`, `openbb_nasdaq.models.equity_search`, `NasdaqEquitySearchFetcher`, `openbb_nasdaq.models.historical_dividends`, `NasdaqHistoricalDividendsFetcher`, `openbb_nasdaq.models.top_retail`, `NasdaqTopRetailFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_nasdaq.models.calendar_dividend`
- `openbb_nasdaq.models.calendar_earnings`
- `openbb_nasdaq.models.calendar_ipo`
- `openbb_nasdaq.models.company_filings`
- `openbb_nasdaq.models.economic_calendar`
- `openbb_nasdaq.models.equity_screener`
- `openbb_nasdaq.models.equity_search`
- `openbb_nasdaq.models.historical_dividends`
- `openbb_nasdaq.models.top_retail`

## Notes
- Generated: 2025-11-18T07:54:40.308457
- Generator: World's Best Repo Book Generator v1.0.0
