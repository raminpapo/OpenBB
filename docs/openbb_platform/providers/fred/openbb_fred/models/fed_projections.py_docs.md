# File Documentation: fed_projections.py

## Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/fed_projections.py`
- **Size**: 2,328 bytes
- **Lines**: 76
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FRED PROJECTION Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.fed_projections import (
    PROJECTIONData,
    PROJECTIONQueryParams,
)
from pydantic import Field

NAME_TO_ID_PROJECTION = {
    "range_high": ["FEDTARRH", "FEDTARRHLR"],
    "central_tendency_high": ["FEDTARCTH", "FEDTARCTHLR"],
    "median": ["FEDTARMD", "FEDTARMDLR"],
    "range_midpoint": ["FEDTARRM", "FEDTARRMLR"],
    "central_tendency_midpoint": ["FEDTARCTM", "FEDTARCTMLR"],
    "range_low": ["FEDTARRL", "FEDTARRLLR"],
    "central_tendency_low": ["FEDTARCTL", "FEDTARCTLLR"],
}


class FREDPROJECTIONQueryParams(PROJECTIONQueryParams):
    """FRED PROJECTION Query."""

    long_run: bool = Field(
        default=False, description="Flag to show long run projections"
    )


class FREDPROJECTIONData(PROJECTIONData):
    """FRED PROJECTION Data."""


class FREDPROJECTIONFetcher(
    Fetcher[FREDPROJECTIONQueryParams, list[FREDPROJECTIONData]]
):
    """FRED Federal Funds Rate Projections Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FREDPROJECTIONQueryParams:
        """Transform query."""
        return FREDPROJECTIONQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FREDPROJECTIONQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any
    ) -> list:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_fred.utils.fred_base import Fred
        from openbb_fred.utils.fred_helpers import process_projections

        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)
        data_dict: dict = {}
        for key, value in NAME_TO_ID_PROJECTION.items():
            data = fred.get_series(value[query.long_run], **kwargs)
            data_dict[key] = data

        processed = process_projections(data_dict)

        return processed

    @staticmethod
    def transform_data(
        query: FREDPROJECTIONQueryParams, data: list, **kwargs: Any
    ) -> list[FREDPROJECTIONData]:
        """Transform data"""
        keys = ["date"] + list(NAME_TO_ID_PROJECTION.keys())
        return [FREDPROJECTIONData(**{k: x[k] for k in keys}) for x in data]

```



---

## High-Level Overview

This is a **python** file named `fed_projections.py`.

**Python Module**

- **Classes** (3): FREDPROJECTIONQueryParams, FREDPROJECTIONData, FREDPROJECTIONFetcher
- **Functions** (3): transform_query, extract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FREDPROJECTIONQueryParams`**(PROJECTIONQueryParams)
- **`FREDPROJECTIONData`**(PROJECTIONData)
- **`FREDPROJECTIONFetcher`**(
    Fetcher[FREDPROJECTIONQueryParams, list[FREDPROJECTIONData]]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Field`
- `Fred`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.fed_projections`
- `openbb_fred.utils.fred_base`
- `openbb_fred.utils.fred_helpers`
- `process_projections`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.962341Z
**Generator**: World's Best Repo Book Generator v1.0
