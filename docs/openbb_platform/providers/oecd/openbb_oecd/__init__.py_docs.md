# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/oecd/openbb_oecd/__init__.py`
- **Size**: 1,555 bytes
- **Lines**: 34
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OECD provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_oecd.models.composite_leading_indicator import (
    OECDCompositeLeadingIndicatorFetcher,
)
from openbb_oecd.models.consumer_price_index import OECDCPIFetcher
from openbb_oecd.models.country_interest_rates import OecdCountryInterestRatesFetcher
from openbb_oecd.models.gdp_forecast import OECDGdpForecastFetcher
from openbb_oecd.models.gdp_nominal import OECDGdpNominalFetcher
from openbb_oecd.models.gdp_real import OECDGdpRealFetcher
from openbb_oecd.models.house_price_index import OECDHousePriceIndexFetcher
from openbb_oecd.models.share_price_index import OECDSharePriceIndexFetcher
from openbb_oecd.models.unemployment import OECDUnemploymentFetcher

oecd_provider = Provider(
    name="oecd",
    website="https://data-explorer.oecd.org/",
    description="""OECD Data Explorer includes data and metadata for OECD countries and selected
non-member economies.""",
    fetcher_dict={
        "CompositeLeadingIndicator": OECDCompositeLeadingIndicatorFetcher,
        "ConsumerPriceIndex": OECDCPIFetcher,
        "CountryInterestRates": OecdCountryInterestRatesFetcher,
        "GdpNominal": OECDGdpNominalFetcher,
        "GdpReal": OECDGdpRealFetcher,
        "GdpForecast": OECDGdpForecastFetcher,
        "HousePriceIndex": OECDHousePriceIndexFetcher,
        "SharePriceIndex": OECDSharePriceIndexFetcher,
        "Unemployment": OECDUnemploymentFetcher,
    },
    repr_name="Organization for Economic Co-operation and Development (OECD)",
)

```



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `OECDCPIFetcher`
- `OECDGdpForecastFetcher`
- `OECDGdpNominalFetcher`
- `OECDGdpRealFetcher`
- `OECDHousePriceIndexFetcher`
- `OECDSharePriceIndexFetcher`
- `OECDUnemploymentFetcher`
- `OecdCountryInterestRatesFetcher`
- `Provider`
- `openbb_core.provider.abstract.provider`
- `openbb_oecd.models.composite_leading_indicator`
- `openbb_oecd.models.consumer_price_index`
- `openbb_oecd.models.country_interest_rates`
- `openbb_oecd.models.gdp_forecast`
- `openbb_oecd.models.gdp_nominal`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.789300Z
**Generator**: World's Best Repo Book Generator v1.0
