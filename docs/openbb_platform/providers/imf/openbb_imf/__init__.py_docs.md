# Documentation: openbb_platform/providers/imf/openbb_imf/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/imf/openbb_imf/__init__.py`
- **Size**: 1,347 characters, 29 lines
- **Words**: 73
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OpenBB IMF Provider Module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_imf.models.available_indicators import ImfAvailableIndicatorsFetcher
from openbb_imf.models.direction_of_trade import ImfDirectionOfTradeFetcher
from openbb_imf.models.economic_indicators import ImfEconomicIndicatorsFetcher
from openbb_imf.models.maritime_chokepoint_info import ImfMaritimeChokePointInfoFetcher
from openbb_imf.models.maritime_chokepoint_volume import (
    ImfMaritimeChokePointVolumeFetcher,
)
from openbb_imf.models.port_info import ImfPortInfoFetcher
from openbb_imf.models.port_volume import ImfPortVolumeFetcher

imf_provider = Provider(
    name="imf",
    website="https://datahelp.imf.org/knowledgebase/articles/667681-using-json-restful-web-service",
    description="Access International Monetary Fund (IMF) data APIs.",
    fetcher_dict={
        "AvailableIndicators": ImfAvailableIndicatorsFetcher,
        "DirectionOfTrade": ImfDirectionOfTradeFetcher,
        "EconomicIndicators": ImfEconomicIndicatorsFetcher,
        "MaritimeChokePointInfo": ImfMaritimeChokePointInfoFetcher,
        "MaritimeChokePointVolume": ImfMaritimeChokePointVolumeFetcher,
        "PortInfo": ImfPortInfoFetcher,
        "PortVolume": ImfPortVolumeFetcher,
    },
    repr_name="International Monetary Fund (IMF) Data APIs",
)

```

## High-Level Overview

OpenBB IMF Provider Module.

from openbb_core.provider.abstract.provider import Provider
from openbb_imf.models.available_indicators import ImfAvailableIndicatorsFetcher
from openbb_imf.models.direction_of_trade import ImfDirectionOfTradeFetcher
from openbb_imf.models.economic_indicators import ImfEconomicIndicatorsFetcher
from openbb_imf.models.maritime_chokepoint_info import ImfMaritimeChokePointInfoFetcher
from openbb_imf.models.maritime_chokepoint_volume import (
ImfMaritimeChokePointVolumeFetcher,
)
from openbb_imf.models.port_info import ImfPortInfoFetcher
from openbb_imf.models.port_volume import ImfPortVolumeFetcher

imf_provider = Provider(
name="imf",
website="https://datahelp.imf.org/knowledgebase/articles/667681-using-json-restful-web-service",
description="Access International Monetary Fund (IMF) data APIs.",
fetcher_dict={
"AvailableIndicators": ImfAvailableIndicatorsFetcher,
"DirectionOfTrade": ImfDirectionOfTradeFetcher,

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (15):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_imf.models.available_indicators`, `ImfAvailableIndicatorsFetcher`, `openbb_imf.models.direction_of_trade`, `ImfDirectionOfTradeFetcher`, `openbb_imf.models.economic_indicators`, `ImfEconomicIndicatorsFetcher`, `openbb_imf.models.maritime_chokepoint_info`, `ImfMaritimeChokePointInfoFetcher`, `openbb_imf.models.maritime_chokepoint_volume`, `openbb_imf.models.port_info`, `ImfPortInfoFetcher`, `openbb_imf.models.port_volume`, `ImfPortVolumeFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_imf.models.available_indicators`
- `openbb_imf.models.direction_of_trade`
- `openbb_imf.models.economic_indicators`
- `openbb_imf.models.maritime_chokepoint_info`
- `openbb_imf.models.maritime_chokepoint_volume`
- `openbb_imf.models.port_info`
- `openbb_imf.models.port_volume`

## Notes
- Generated: 2025-11-18T07:54:39.941035
- Generator: World's Best Repo Book Generator v1.0.0
