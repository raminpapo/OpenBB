# Documentation: openbb_platform/providers/stockgrid/openbb_stockgrid/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/stockgrid/openbb_stockgrid/__init__.py`
- **Size**: 667 characters, 18 lines
- **Words**: 68
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""stockgrid provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_stockgrid.models.short_volume import StockgridShortVolumeFetcher

stockgrid_provider = Provider(
    name="stockgrid",
    website="https://www.stockgrid.io",
    description="""Stockgrid gives you a detailed view of what smart money is doing.
Get in depth data about large option blocks being traded, including
the sentiment score, size, volume and order type. Stop guessing and
build a strategy around the number 1 factor moving the market: money.""",
    fetcher_dict={
        "ShortVolume": StockgridShortVolumeFetcher,
    },
    repr_name="Stockgrid",
)

```

## High-Level Overview

stockgrid provider module.

from openbb_core.provider.abstract.provider import Provider
from openbb_stockgrid.models.short_volume import StockgridShortVolumeFetcher

stockgrid_provider = Provider(
name="stockgrid",
website="https://www.stockgrid.io",
description="""Stockgrid gives you a detailed view of what smart money is doing.
Get in depth data about large option blocks being traded, including
the sentiment score, size, volume and order type. Stop guessing and
build a strategy around the number 1 factor moving the market: money.""",
fetcher_dict={
"ShortVolume": StockgridShortVolumeFetcher,
},
repr_name="Stockgrid",
)


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (4):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_stockgrid.models.short_volume`, `StockgridShortVolumeFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_stockgrid.models.short_volume`

## Notes
- Generated: 2025-11-18T07:54:41.681578
- Generator: World's Best Repo Book Generator v1.0.0
