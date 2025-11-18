# Documentation: openbb_platform/providers/econdb/openbb_econdb/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/econdb/openbb_econdb/__init__.py`
- **Size**: 1,730 characters, 37 lines
- **Words**: 130
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""EconDB provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_econdb.models.available_indicators import EconDbAvailableIndicatorsFetcher
from openbb_econdb.models.country_profile import EconDbCountryProfileFetcher
from openbb_econdb.models.economic_indicators import EconDbEconomicIndicatorsFetcher
from openbb_econdb.models.export_destinations import EconDbExportDestinationsFetcher
from openbb_econdb.models.gdp_nominal import EconDbGdpNominalFetcher
from openbb_econdb.models.gdp_real import EconDbGdpRealFetcher
from openbb_econdb.models.port_volume import EconDbPortVolumeFetcher
from openbb_econdb.models.yield_curve import EconDbYieldCurveFetcher

econdb_provider = Provider(
    name="EconDB",
    website="https://econdb.com",
    description="""The mission of the company is to process information in ways that
facilitate understanding of the economic situation at different granularity levels.

The sources of data include official statistics agencies and so-called alternative
data sources where we collect direct observations of the market and generate
aggregate statistics.""",
    credentials=[
        "api_key"
    ],  # Can be left as None, an attempt to use a temporary token will be made.
    fetcher_dict={
        "AvailableIndicators": EconDbAvailableIndicatorsFetcher,
        "CountryProfile": EconDbCountryProfileFetcher,
        "EconomicIndicators": EconDbEconomicIndicatorsFetcher,
        "ExportDestinations": EconDbExportDestinationsFetcher,
        "GdpNominal": EconDbGdpNominalFetcher,
        "GdpReal": EconDbGdpRealFetcher,
        "PortVolume": EconDbPortVolumeFetcher,
        "YieldCurve": EconDbYieldCurveFetcher,
    },
    repr_name="EconDB",
)

```

## High-Level Overview

EconDB provider module.

from openbb_core.provider.abstract.provider import Provider
from openbb_econdb.models.available_indicators import EconDbAvailableIndicatorsFetcher
from openbb_econdb.models.country_profile import EconDbCountryProfileFetcher
from openbb_econdb.models.economic_indicators import EconDbEconomicIndicatorsFetcher
from openbb_econdb.models.export_destinations import EconDbExportDestinationsFetcher
from openbb_econdb.models.gdp_nominal import EconDbGdpNominalFetcher
from openbb_econdb.models.gdp_real import EconDbGdpRealFetcher
from openbb_econdb.models.port_volume import EconDbPortVolumeFetcher
from openbb_econdb.models.yield_curve import EconDbYieldCurveFetcher

econdb_provider = Provider(
name="EconDB",
website="https://econdb.com",
description="""The mission of the company is to process information in ways that
facilitate understanding of the economic situation at different granularity levels.

The sources of data include official statistics agencies and so-called alternative
data sources where we collect direct observations of the market and generate

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (18):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_econdb.models.available_indicators`, `EconDbAvailableIndicatorsFetcher`, `openbb_econdb.models.country_profile`, `EconDbCountryProfileFetcher`, `openbb_econdb.models.economic_indicators`, `EconDbEconomicIndicatorsFetcher`, `openbb_econdb.models.export_destinations`, `EconDbExportDestinationsFetcher`, `openbb_econdb.models.gdp_nominal`, `EconDbGdpNominalFetcher`, `openbb_econdb.models.gdp_real`, `EconDbGdpRealFetcher`, `openbb_econdb.models.port_volume`, `EconDbPortVolumeFetcher`, `openbb_econdb.models.yield_curve`, `EconDbYieldCurveFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_econdb.models.available_indicators`
- `openbb_econdb.models.country_profile`
- `openbb_econdb.models.economic_indicators`
- `openbb_econdb.models.export_destinations`
- `openbb_econdb.models.gdp_nominal`
- `openbb_econdb.models.gdp_real`
- `openbb_econdb.models.port_volume`
- `openbb_econdb.models.yield_curve`

## Notes
- Generated: 2025-11-18T07:54:38.124842
- Generator: World's Best Repo Book Generator v1.0.0
