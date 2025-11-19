# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/__init__.py`
- **Size**: 1,161 bytes
- **Lines**: 27
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Finviz provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_finviz.models.compare_groups import FinvizCompareGroupsFetcher
from openbb_finviz.models.equity_profile import FinvizEquityProfileFetcher
from openbb_finviz.models.equity_screener import FinvizEquityScreenerFetcher
from openbb_finviz.models.key_metrics import FinvizKeyMetricsFetcher
from openbb_finviz.models.price_performance import FinvizPricePerformanceFetcher
from openbb_finviz.models.price_target import FinvizPriceTargetFetcher

finviz_provider = Provider(
    name="finviz",
    website="https://finviz.com",
    description="Unofficial Finviz API - https://github.com/lit26/finvizfinance/releases",
    credentials=None,
    fetcher_dict={
        "CompareGroups": FinvizCompareGroupsFetcher,
        "EtfPricePerformance": FinvizPricePerformanceFetcher,
        "EquityInfo": FinvizEquityProfileFetcher,
        "EquityScreener": FinvizEquityScreenerFetcher,
        "KeyMetrics": FinvizKeyMetricsFetcher,
        "PricePerformance": FinvizPricePerformanceFetcher,
        "PriceTarget": FinvizPriceTargetFetcher,
    },
    repr_name="FinViz",
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
- `FinvizCompareGroupsFetcher`
- `FinvizEquityProfileFetcher`
- `FinvizEquityScreenerFetcher`
- `FinvizKeyMetricsFetcher`
- `FinvizPricePerformanceFetcher`
- `FinvizPriceTargetFetcher`
- `Provider`
- `openbb_core.provider.abstract.provider`
- `openbb_finviz.models.compare_groups`
- `openbb_finviz.models.equity_profile`
- `openbb_finviz.models.equity_screener`
- `openbb_finviz.models.key_metrics`
- `openbb_finviz.models.price_performance`
- `openbb_finviz.models.price_target`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.393943Z
**Generator**: World's Best Repo Book Generator v1.0
