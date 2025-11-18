# Documentation: openbb_platform/core/openbb_core/provider/standard_models/futures_instruments.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/futures_instruments.py`
- **Size**: 325 characters, 13 lines
- **Words**: 22
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Futures Instruments Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams


class FuturesInstrumentsQueryParams(QueryParams):
    """Futures Instruments Query."""


class FuturesInstrumentsData(Data):
    """Futures Instruments Data."""

```

## High-Level Overview

Futures Instruments Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams


class FuturesInstrumentsQueryParams(QueryParams):
Futures Instruments Query.
Futures Instruments Data.


## Detailed Structure

### Python File Structure

**Classes** (2):
`FuturesInstrumentsQueryParams`, `FuturesInstrumentsData`

**Functions** (0):
None

**Imports** (4):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`


## Key Components

**Class `FuturesInstrumentsQueryParams`**: Futures Instruments Query.

**Class `FuturesInstrumentsData`**: Futures Instruments Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`

## Notes
- Generated: 2025-11-18T07:54:35.651417
- Generator: World's Best Repo Book Generator v1.0.0
