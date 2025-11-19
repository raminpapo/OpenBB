# File Documentation: export_destinations.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/export_destinations.py`
- **Size**: 826 bytes
- **Lines**: 28
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Export Destinations Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class ExportDestinationsQueryParams(QueryParams):
    """Export Destinations Query."""

    country: str = Field(description=QUERY_DESCRIPTIONS.get("country", ""))


class ExportDestinationsData(Data):
    """Export Destinations Data."""

    origin_country: str = Field(
        description="The country of origin.",
    )
    destination_country: str = Field(
        description="The destination country.",
    )
    value: float | int = Field(
        description="The value of the export.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )

```



---

## High-Level Overview

This is a **python** file named `export_destinations.py`.

**Python Module**

- **Classes** (2): ExportDestinationsQueryParams, ExportDestinationsData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ExportDestinationsQueryParams`**(QueryParams)
- **`ExportDestinationsData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QUERY_DESCRIPTIONS`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.454683Z
**Generator**: World's Best Repo Book Generator v1.0
