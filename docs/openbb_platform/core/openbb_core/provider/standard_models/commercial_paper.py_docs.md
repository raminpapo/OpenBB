# File Documentation: commercial_paper.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/commercial_paper.py`
- **Size**: 1,256 bytes
- **Lines**: 45
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Commercial Paper Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CommercialPaperParams(QueryParams):
    """Commercial Paper Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class CommercialPaperData(Data):
    """Commercial Paper Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    maturity: str = Field(description="Maturity length of the item.")
    rate: float = Field(
        description="Interest rate.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    title: str | None = Field(
        default=None,
        description="Title of the series.",
    )

```



---

## High-Level Overview

This is a **python** file named `commercial_paper.py`.

**Python Module**

- **Classes** (2): CommercialPaperParams, CommercialPaperData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CommercialPaperParams`**(QueryParams)
- **`CommercialPaperData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.376117Z
**Generator**: World's Best Repo Book Generator v1.0
