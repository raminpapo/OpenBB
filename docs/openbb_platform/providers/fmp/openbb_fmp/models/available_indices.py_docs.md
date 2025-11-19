# File Documentation: available_indices.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/available_indices.py`
- **Size**: 1,784 bytes
- **Lines**: 59
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP Available Indices Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.available_indices import (
    AvailableIndicesData,
    AvailableIndicesQueryParams,
)


class FMPAvailableIndicesQueryParams(AvailableIndicesQueryParams):
    """FMP Available Indices Query.

    Source: https://site.financialmodelingprep.com/developer/docs#indexes-list
    """


class FMPAvailableIndicesData(AvailableIndicesData):
    """FMP Available Indices Data."""


class FMPAvailableIndicesFetcher(
    Fetcher[
        FMPAvailableIndicesQueryParams,
        list[FMPAvailableIndicesData],
    ]
):
    """FMP Available Indices Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPAvailableIndicesQueryParams:
        """Transform the query params."""
        return FMPAvailableIndicesQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPAvailableIndicesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        url = f"https://financialmodelingprep.com/stable/index-list?apikey={api_key}"

        return await get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPAvailableIndicesQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPAvailableIndicesData]:
        """Return the transformed data."""
        return [FMPAvailableIndicesData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `available_indices.py`.

**Python Module**

- **Classes** (3): FMPAvailableIndicesQueryParams, FMPAvailableIndicesData, FMPAvailableIndicesFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPAvailableIndicesQueryParams`**(AvailableIndicesQueryParams)
- **`FMPAvailableIndicesData`**(AvailableIndicesData)
- **`FMPAvailableIndicesFetcher`**(
    Fetcher[
        FMPAvailableIndicesQueryParams,
        list[FMPAvailableIndicesData],
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `get_data_many`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.available_indices`
- `openbb_fmp.utils.helpers`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.567572Z
**Generator**: World's Best Repo Book Generator v1.0
