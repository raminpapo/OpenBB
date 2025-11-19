# File Documentation: esg_sector.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/esg_sector.py`
- **Size**: 951 bytes
- **Lines**: 44
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `esg_sector.py`.

**Python Module**

- **Classes** (2): ESGSectorQueryParams, ESGSectorData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ESGSectorQueryParams`**(QueryParams)
- **`ESGSectorData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.438193Z
**Generator**: World's Best Repo Book Generator v1.0
