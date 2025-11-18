# Documentation: openbb_platform/core/openbb_core/provider/standard_models/esg_sector.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/esg_sector.py`
- **Size**: 951 characters, 44 lines
- **Words**: 110
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ESG Sector Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams


class ESGSectorQueryParams(QueryParams):
    """ESG Sector Query.

    Parameter
    ---------
    year : int
        The year to get ESG information for
    """

    year: int


class ESGSectorData(Data):
    """ESG Sector Data.

    Returns
    -------
    year : int
        The year of the ESG Sector.
    sector : str
        The sector of the ESG Sector.
    environmental_score : float
        The environmental score of the ESG Sector.
    social_score : float
        The social score of the ESG Sector.
    governance_score : float
        The governance score of the ESG Sector.
    esg_score : float
        The ESG score of the ESG Sector.
    """

    year: int
    sector: str
    environmental_score: float
    social_score: float
    governance_score: float
    esg_score: float

```

## High-Level Overview

ESG Sector Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams


class ESGSectorQueryParams(QueryParams):
ESG Sector Query.


year: int


class ESGSectorData(Data):
ESG Sector Data.


year: int
sector: str
environmental_score: float

## Detailed Structure

### Python File Structure

**Classes** (2):
`ESGSectorQueryParams`, `ESGSectorData`

**Functions** (0):
None

**Imports** (4):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`


## Key Components

**Class `ESGSectorQueryParams`**: ESG Sector Query.

    Parameter
    ---------
    year : int
        The year to get ESG information for

**Class `ESGSectorData`**: ESG Sector Data.

    Returns
    -------
    year : int
        The year of the ESG Sector.
    sector : str
        The sector of the ESG Sector.
    environmental_score : float
        The environm

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`

## Notes
- Generated: 2025-11-18T07:54:35.611975
- Generator: World's Best Repo Book Generator v1.0.0
