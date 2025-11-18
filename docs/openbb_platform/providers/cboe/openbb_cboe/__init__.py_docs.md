# Documentation: openbb_platform/providers/cboe/openbb_cboe/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/cboe/openbb_cboe/__init__.py`
- **Size**: 1,772 characters, 41 lines
- **Words**: 108
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Cboe provider module."""

from openbb_cboe.models.available_indices import CboeAvailableIndicesFetcher
from openbb_cboe.models.equity_historical import CboeEquityHistoricalFetcher
from openbb_cboe.models.equity_quote import CboeEquityQuoteFetcher
from openbb_cboe.models.equity_search import CboeEquitySearchFetcher
from openbb_cboe.models.futures_curve import CboeFuturesCurveFetcher
from openbb_cboe.models.index_constituents import (
    CboeIndexConstituentsFetcher,
)
from openbb_cboe.models.index_historical import (
    CboeIndexHistoricalFetcher,
)
from openbb_cboe.models.index_search import CboeIndexSearchFetcher
from openbb_cboe.models.index_snapshots import CboeIndexSnapshotsFetcher
from openbb_cboe.models.options_chains import CboeOptionsChainsFetcher
from openbb_core.provider.abstract.provider import Provider

cboe_provider = Provider(
    name="cboe",
    website="https://www.cboe.com",
    description="""Cboe is the world's go-to derivatives and exchange network,
delivering cutting-edge trading, clearing and investment solutions to people
around the world.""",
    credentials=None,
    fetcher_dict={
        "AvailableIndices": CboeAvailableIndicesFetcher,
        "EquityHistorical": CboeEquityHistoricalFetcher,
        "EquityQuote": CboeEquityQuoteFetcher,
        "EquitySearch": CboeEquitySearchFetcher,
        "EtfHistorical": CboeEquityHistoricalFetcher,
        "IndexConstituents": CboeIndexConstituentsFetcher,
        "FuturesCurve": CboeFuturesCurveFetcher,
        "IndexHistorical": CboeIndexHistoricalFetcher,
        "IndexSearch": CboeIndexSearchFetcher,
        "IndexSnapshots": CboeIndexSnapshotsFetcher,
        "OptionsChains": CboeOptionsChainsFetcher,
    },
    repr_name="Chicago Board Options Exchange (CBOE)",
)

```

## High-Level Overview

Cboe provider module.

from openbb_cboe.models.available_indices import CboeAvailableIndicesFetcher
from openbb_cboe.models.equity_historical import CboeEquityHistoricalFetcher
from openbb_cboe.models.equity_quote import CboeEquityQuoteFetcher
from openbb_cboe.models.equity_search import CboeEquitySearchFetcher
from openbb_cboe.models.futures_curve import CboeFuturesCurveFetcher
from openbb_cboe.models.index_constituents import (
CboeIndexConstituentsFetcher,
)
from openbb_cboe.models.index_historical import (
CboeIndexHistoricalFetcher,
)
from openbb_cboe.models.index_search import CboeIndexSearchFetcher
from openbb_cboe.models.index_snapshots import CboeIndexSnapshotsFetcher
from openbb_cboe.models.options_chains import CboeOptionsChainsFetcher
from openbb_core.provider.abstract.provider import Provider

cboe_provider = Provider(
name="cboe",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (20):
`openbb_cboe.models.available_indices`, `CboeAvailableIndicesFetcher`, `openbb_cboe.models.equity_historical`, `CboeEquityHistoricalFetcher`, `openbb_cboe.models.equity_quote`, `CboeEquityQuoteFetcher`, `openbb_cboe.models.equity_search`, `CboeEquitySearchFetcher`, `openbb_cboe.models.futures_curve`, `CboeFuturesCurveFetcher`, `openbb_cboe.models.index_constituents`, `openbb_cboe.models.index_historical`, `openbb_cboe.models.index_search`, `CboeIndexSearchFetcher`, `openbb_cboe.models.index_snapshots`, `CboeIndexSnapshotsFetcher`, `openbb_cboe.models.options_chains`, `CboeOptionsChainsFetcher`, `openbb_core.provider.abstract.provider`, `Provider`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_cboe.models.available_indices`
- `openbb_cboe.models.equity_historical`
- `openbb_cboe.models.equity_quote`
- `openbb_cboe.models.equity_search`
- `openbb_cboe.models.futures_curve`
- `openbb_cboe.models.index_constituents`
- `openbb_cboe.models.index_historical`
- `openbb_cboe.models.index_search`
- `openbb_cboe.models.index_snapshots`
- `openbb_cboe.models.options_chains`

## Notes
- Generated: 2025-11-18T07:54:37.451105
- Generator: World's Best Repo Book Generator v1.0.0
