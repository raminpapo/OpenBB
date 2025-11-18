# Documentation: openbb_platform/providers/eia/openbb_us_eia/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/eia/openbb_us_eia/__init__.py`
- **Size**: 1,143 characters, 26 lines
- **Words**: 106
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OpenBB EIA Provider Module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_us_eia.models.petroleum_status_report import EiaPetroleumStatusReportFetcher
from openbb_us_eia.models.short_term_energy_outlook import (
    EiaShortTermEnergyOutlookFetcher,
)

eia_provider = Provider(
    name="eia",
    website="https://eia.gov/",
    description="The U.S. Energy Information Administration is committed to its free and open data"
    + " by making it available through an Application Programming Interface (API) and its open data tools."
    + " See https://www.eia.gov/opendata/ for more information.",
    credentials=[
        "api_key"
    ],  # This is not required for the Weekly Petroleum Status Report
    fetcher_dict={
        "PetroleumStatusReport": EiaPetroleumStatusReportFetcher,
        "ShortTermEnergyOutlook": EiaShortTermEnergyOutlookFetcher,
    },
    repr_name="U.S. Energy Information Administration (EIA) Open Data and API",
    instructions="""Credentials are required for functions calling the EIA's API.
    Register for a free key here: https://www.eia.gov/opendata/register.php""",
)

```

## High-Level Overview

OpenBB EIA Provider Module.

from openbb_core.provider.abstract.provider import Provider
from openbb_us_eia.models.petroleum_status_report import EiaPetroleumStatusReportFetcher
from openbb_us_eia.models.short_term_energy_outlook import (
EiaShortTermEnergyOutlookFetcher,
)

eia_provider = Provider(
name="eia",
website="https://eia.gov/",
description="The U.S. Energy Information Administration is committed to its free and open data"
+ " by making it available through an Application Programming Interface (API) and its open data tools."
+ " See https://www.eia.gov/opendata/ for more information.",
credentials=[
"api_key"
],  # This is not required for the Weekly Petroleum Status Report
fetcher_dict={
"PetroleumStatusReport": EiaPetroleumStatusReportFetcher,
"ShortTermEnergyOutlook": EiaShortTermEnergyOutlookFetcher,

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (5):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_us_eia.models.petroleum_status_report`, `EiaPetroleumStatusReportFetcher`, `openbb_us_eia.models.short_term_energy_outlook`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_us_eia.models.petroleum_status_report`
- `openbb_us_eia.models.short_term_energy_outlook`

## Notes
- Generated: 2025-11-18T07:54:38.263859
- Generator: World's Best Repo Book Generator v1.0.0
