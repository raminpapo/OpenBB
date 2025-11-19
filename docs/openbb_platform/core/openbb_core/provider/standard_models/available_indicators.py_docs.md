# File Documentation: available_indicators.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/available_indicators.py`
- **Size**: 1,329 bytes
- **Lines**: 41
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Available Indicators Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class AvailableIndicesQueryParams(QueryParams):
    """Available Indicators Query."""


class AvailableIndicatorsData(Data):
    """Available Indicators Data.

    Returns the list of available economic indicators from a provider.
    """

    symbol_root: str | None = Field(
        default=None, description="The root symbol representing the indicator."
    )
    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", "")
        + " The root symbol with additional codes.",
    )
    country: str | None = Field(
        default=None,
        description="The name of the country, region, or entity represented by the symbol.",
    )
    iso: str | None = Field(
        default=None,
        description="The ISO code of the country, region, or entity represented by the symbol.",
    )
    description: str | None = Field(
        default=None, description="The description of the indicator."
    )
    frequency: str | None = Field(
        default=None, description="The frequency of the indicator data."
    )

```



---

## High-Level Overview

This is a **python** file named `available_indicators.py`.

**Python Module**

- **Classes** (2): AvailableIndicesQueryParams, AvailableIndicatorsData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AvailableIndicesQueryParams`**(QueryParams)
- **`AvailableIndicatorsData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `DATA_DESCRIPTIONS`
- `Data`
- `Field`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.343364Z
**Generator**: World's Best Repo Book Generator v1.0
