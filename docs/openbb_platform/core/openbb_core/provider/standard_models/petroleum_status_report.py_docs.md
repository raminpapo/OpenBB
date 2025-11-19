# File Documentation: petroleum_status_report.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/petroleum_status_report.py`
- **Size**: 1,342 bytes
- **Lines**: 39
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Petroleum Status Report Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class PetroleumStatusReportQueryParams(QueryParams):
    """Petroleum Status Report Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class PetroleumStatusReportData(Data):
    """Petroleum Status Report Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    table: str | None = Field(description="Table name for the data.")
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

This is a **python** file named `petroleum_status_report.py`.

**Python Module**

- **Classes** (2): PetroleumStatusReportQueryParams, PetroleumStatusReportData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`PetroleumStatusReportQueryParams`**(QueryParams)
- **`PetroleumStatusReportData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.544872Z
**Generator**: World's Best Repo Book Generator v1.0
