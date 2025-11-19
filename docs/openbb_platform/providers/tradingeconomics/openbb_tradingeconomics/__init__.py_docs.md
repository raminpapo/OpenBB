# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/tradingeconomics/openbb_tradingeconomics/__init__.py`
- **Size**: 944 bytes
- **Lines**: 20
- **Category**: python
- **Extension**: .py

---

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
- `TEEconomicCalendarFetcher`
- `openbb_core.provider.abstract.provider`
- `openbb_tradingeconomics.models.economic_calendar`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.060517Z
**Generator**: World's Best Repo Book Generator v1.0
