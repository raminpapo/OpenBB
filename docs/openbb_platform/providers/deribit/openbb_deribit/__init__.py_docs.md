# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/deribit/openbb_deribit/__init__.py`
- **Size**: 1,134 bytes
- **Lines**: 25
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OpenBB Deribit Provider Module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_deribit.models.futures_curve import DeribitFuturesCurveFetcher
from openbb_deribit.models.futures_historical import DeribitFuturesHistoricalFetcher
from openbb_deribit.models.futures_info import DeribitFuturesInfoFetcher
from openbb_deribit.models.futures_instruments import DeribitFuturesInstrumentsFetcher
from openbb_deribit.models.options_chains import DeribitOptionsChainsFetcher

deribit_provider = Provider(
    name="deribit",
    website="https://deribit.com/",
    description="""Unofficial Python client for public data published by Deribit.""",
    credentials=None,
    fetcher_dict={
        "FuturesCurve": DeribitFuturesCurveFetcher,
        "FuturesHistorical": DeribitFuturesHistoricalFetcher,
        "FuturesInfo": DeribitFuturesInfoFetcher,
        "FuturesInstruments": DeribitFuturesInstrumentsFetcher,
        "OptionsChains": DeribitOptionsChainsFetcher,
    },
    repr_name="Deribit Public Data",
    instructions="This provider does not require any credentials and is not meant for trading.",
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
- `DeribitFuturesCurveFetcher`
- `DeribitFuturesHistoricalFetcher`
- `DeribitFuturesInfoFetcher`
- `DeribitFuturesInstrumentsFetcher`
- `DeribitOptionsChainsFetcher`
- `Provider`
- `openbb_core.provider.abstract.provider`
- `openbb_deribit.models.futures_curve`
- `openbb_deribit.models.futures_historical`
- `openbb_deribit.models.futures_info`
- `openbb_deribit.models.futures_instruments`
- `openbb_deribit.models.options_chains`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.741679Z
**Generator**: World's Best Repo Book Generator v1.0
