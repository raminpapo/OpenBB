# File Documentation: manufacturing_outlook_texas.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/manufacturing_outlook_texas.py`
- **Size**: 1,842 bytes
- **Lines**: 50
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Manufacturing Outlook - Texas - Standard Model."""

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


class ManufacturingOutlookTexasQueryParams(QueryParams):
    """Manufacturing Outlook - Texas - Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class ManufacturingOutlookTexasData(Data):
    """Manufacturing Outlook - Texas - Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    topic: str | None = Field(default=None, description="Topic of the survey response.")
    diffusion_index: float | None = Field(default=None, description="Diffusion Index.")
    percent_reporting_increase: float | None = Field(
        default=None,
        description="Percent of respondents reporting an increase over the last month.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    percent_reporting_decrease: float | None = Field(
        default=None,
        description="Percent of respondents reporting a decrease over the last month.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    percent_reporting_no_change: float | None = Field(
        default=None,
        description="Percent of respondents reporting no change over the last month.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```



---

## High-Level Overview

This is a **python** file named `manufacturing_outlook_texas.py`.

**Python Module**

- **Classes** (2): ManufacturingOutlookTexasQueryParams, ManufacturingOutlookTexasData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ManufacturingOutlookTexasQueryParams`**(QueryParams)
- **`ManufacturingOutlookTexasData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.522202Z
**Generator**: World's Best Repo Book Generator v1.0
