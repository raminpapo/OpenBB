# Documentation: openbb_platform/providers/finviz/openbb_finviz/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/__init__.py`
- **Size**: 1,161 characters, 27 lines
- **Words**: 60
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Finviz provider module.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (14):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_finviz.models.compare_groups`, `FinvizCompareGroupsFetcher`, `openbb_finviz.models.equity_profile`, `FinvizEquityProfileFetcher`, `openbb_finviz.models.equity_screener`, `FinvizEquityScreenerFetcher`, `openbb_finviz.models.key_metrics`, `FinvizKeyMetricsFetcher`, `openbb_finviz.models.price_performance`, `FinvizPricePerformanceFetcher`, `openbb_finviz.models.price_target`, `FinvizPriceTargetFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_finviz.models.compare_groups`
- `openbb_finviz.models.equity_profile`
- `openbb_finviz.models.equity_screener`
- `openbb_finviz.models.key_metrics`
- `openbb_finviz.models.price_performance`
- `openbb_finviz.models.price_target`

## Notes
- Generated: 2025-11-18T07:54:39.156903
- Generator: World's Best Repo Book Generator v1.0.0
