# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/imf/openbb_imf/__init__.py`
- **Size**: 1,347 bytes
- **Lines**: 29
- **Category**: python
- **Extension**: .py

---

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
- `ImfAvailableIndicatorsFetcher`
- `ImfDirectionOfTradeFetcher`
- `ImfEconomicIndicatorsFetcher`
- `ImfMaritimeChokePointInfoFetcher`
- `ImfPortInfoFetcher`
- `ImfPortVolumeFetcher`
- `Provider`
- `openbb_core.provider.abstract.provider`
- `openbb_imf.models.available_indicators`
- `openbb_imf.models.direction_of_trade`
- `openbb_imf.models.economic_indicators`
- `openbb_imf.models.maritime_chokepoint_info`
- `openbb_imf.models.maritime_chokepoint_volume`
- `openbb_imf.models.port_info`
- `openbb_imf.models.port_volume`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.243929Z
**Generator**: World's Best Repo Book Generator v1.0
