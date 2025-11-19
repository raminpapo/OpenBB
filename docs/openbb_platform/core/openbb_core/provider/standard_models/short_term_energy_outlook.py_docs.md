# File Documentation: short_term_energy_outlook.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/short_term_energy_outlook.py`
- **Size**: 1,364 bytes
- **Lines**: 39
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Short Term Energy Outlook Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class ShortTermEnergyOutlookQueryParams(QueryParams):
    """Short Term Energy Outlook Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class ShortTermEnergyOutlookData(Data):
    """Short Term Energy Outlook Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    table: str | None = Field(default=None, description="Table name for the data.")
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    order: int | None = Field(
        default=None, description="Presented order of the data, relative to the table."
    )
    title: str | None = Field(default=None, description="Title of the data.")
    value: int | float = Field(description="Value of the data.")
    unit: str | None = Field(default=None, description="Unit or scale of the data.")

```



---

## High-Level Overview

This is a **python** file named `short_term_energy_outlook.py`.

**Python Module**

- **Classes** (2): ShortTermEnergyOutlookQueryParams, ShortTermEnergyOutlookData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ShortTermEnergyOutlookQueryParams`**(QueryParams)
- **`ShortTermEnergyOutlookData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.571502Z
**Generator**: World's Best Repo Book Generator v1.0
