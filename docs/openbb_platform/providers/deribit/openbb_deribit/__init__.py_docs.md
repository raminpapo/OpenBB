# Documentation: openbb_platform/providers/deribit/openbb_deribit/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/deribit/openbb_deribit/__init__.py`
- **Size**: 1,134 characters, 25 lines
- **Words**: 72
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

OpenBB Deribit Provider Module.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (12):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_deribit.models.futures_curve`, `DeribitFuturesCurveFetcher`, `openbb_deribit.models.futures_historical`, `DeribitFuturesHistoricalFetcher`, `openbb_deribit.models.futures_info`, `DeribitFuturesInfoFetcher`, `openbb_deribit.models.futures_instruments`, `DeribitFuturesInstrumentsFetcher`, `openbb_deribit.models.options_chains`, `DeribitOptionsChainsFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_deribit.models.futures_curve`
- `openbb_deribit.models.futures_historical`
- `openbb_deribit.models.futures_info`
- `openbb_deribit.models.futures_instruments`
- `openbb_deribit.models.options_chains`

## Notes
- Generated: 2025-11-18T07:54:37.642388
- Generator: World's Best Repo Book Generator v1.0.0
