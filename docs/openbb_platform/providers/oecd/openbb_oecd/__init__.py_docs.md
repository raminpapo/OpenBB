# Documentation: openbb_platform/providers/oecd/openbb_oecd/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/oecd/openbb_oecd/__init__.py`
- **Size**: 1,555 characters, 34 lines
- **Words**: 92
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

OECD provider module.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (19):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_oecd.models.composite_leading_indicator`, `openbb_oecd.models.consumer_price_index`, `OECDCPIFetcher`, `openbb_oecd.models.country_interest_rates`, `OecdCountryInterestRatesFetcher`, `openbb_oecd.models.gdp_forecast`, `OECDGdpForecastFetcher`, `openbb_oecd.models.gdp_nominal`, `OECDGdpNominalFetcher`, `openbb_oecd.models.gdp_real`, `OECDGdpRealFetcher`, `openbb_oecd.models.house_price_index`, `OECDHousePriceIndexFetcher`, `openbb_oecd.models.share_price_index`, `OECDSharePriceIndexFetcher`, `openbb_oecd.models.unemployment`, `OECDUnemploymentFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_oecd.models.composite_leading_indicator`
- `openbb_oecd.models.consumer_price_index`
- `openbb_oecd.models.country_interest_rates`
- `openbb_oecd.models.gdp_forecast`
- `openbb_oecd.models.gdp_nominal`
- `openbb_oecd.models.gdp_real`
- `openbb_oecd.models.house_price_index`
- `openbb_oecd.models.share_price_index`
- `openbb_oecd.models.unemployment`

## Notes
- Generated: 2025-11-18T07:54:40.437423
- Generator: World's Best Repo Book Generator v1.0.0
