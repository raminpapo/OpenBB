# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/cboe/openbb_cboe/__init__.py`
- **Size**: 1,772 bytes
- **Lines**: 41
- **Category**: python
- **Extension**: .py

---

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
- `CboeAvailableIndicesFetcher`
- `CboeEquityHistoricalFetcher`
- `CboeEquityQuoteFetcher`
- `CboeEquitySearchFetcher`
- `CboeFuturesCurveFetcher`
- `CboeIndexSearchFetcher`
- `CboeIndexSnapshotsFetcher`
- `CboeOptionsChainsFetcher`
- `Provider`
- `openbb_cboe.models.available_indices`
- `openbb_cboe.models.equity_historical`
- `openbb_cboe.models.equity_quote`
- `openbb_cboe.models.equity_search`
- `openbb_cboe.models.futures_curve`
- `openbb_cboe.models.index_constituents`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.504372Z
**Generator**: World's Best Repo Book Generator v1.0
