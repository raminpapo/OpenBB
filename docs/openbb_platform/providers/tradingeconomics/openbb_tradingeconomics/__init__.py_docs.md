# Documentation: openbb_platform/providers/tradingeconomics/openbb_tradingeconomics/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/tradingeconomics/openbb_tradingeconomics/__init__.py`
- **Size**: 944 characters, 20 lines
- **Words**: 94
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Trading Economics provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_tradingeconomics.models.economic_calendar import TEEconomicCalendarFetcher

tradingeconomics_provider = Provider(
    name="tradingeconomics",
    website="https://tradingeconomics.com",
    description="""Trading Economics provides its users with accurate information for
196 countries including historical data and forecasts for more than 20 million economic
indicators, exchange rates, stock market indexes, government bond yields and commodity
prices. Our data for economic indicators is based on official sources, not third party
data providers, and our facts are regularly checked for inconsistencies.
Trading Economics has received nearly 2 billion page views from all around the
world.""",
    credentials=["api_key"],
    fetcher_dict={"EconomicCalendar": TEEconomicCalendarFetcher},
    repr_name="Trading Economics",
)

```

## High-Level Overview

Trading Economics provider module.

from openbb_core.provider.abstract.provider import Provider
from openbb_tradingeconomics.models.economic_calendar import TEEconomicCalendarFetcher

tradingeconomics_provider = Provider(
name="tradingeconomics",
website="https://tradingeconomics.com",
description="""Trading Economics provides its users with accurate information for
196 countries including historical data and forecasts for more than 20 million economic
indicators, exchange rates, stock market indexes, government bond yields and commodity
prices. Our data for economic indicators is based on official sources, not third party
data providers, and our facts are regularly checked for inconsistencies.
Trading Economics has received nearly 2 billion page views from all around the
world.""",
credentials=["api_key"],
fetcher_dict={"EconomicCalendar": TEEconomicCalendarFetcher},
repr_name="Trading Economics",
)


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (5):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_tradingeconomics.models.economic_calendar`, `TEEconomicCalendarFetcher`, `all`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_tradingeconomics.models.economic_calendar`

## Notes
- Generated: 2025-11-18T07:54:43.476156
- Generator: World's Best Repo Book Generator v1.0.0
