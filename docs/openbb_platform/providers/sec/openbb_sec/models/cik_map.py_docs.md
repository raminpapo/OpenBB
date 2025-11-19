# File Documentation: cik_map.py

## Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/models/cik_map.py`
- **Size**: 1,640 bytes
- **Lines**: 62
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""SEC CIK Mapping Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cik_map import CikMapData, CikMapQueryParams
from pydantic import Field


class SecCikMapQueryParams(CikMapQueryParams):
    """SEC CIK Mapping Query.

    Source: https://sec.gov/
    """

    use_cache: bool | None = Field(
        default=True,
        description="Whether or not to use cache for the request, default is True.",
    )


class SecCikMapData(CikMapData):
    """SEC CIK Mapping Data."""


class SecCikMapFetcher(
    Fetcher[
        SecCikMapQueryParams,
        SecCikMapData,
    ]
):
    """SEC CIK Map Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> SecCikMapQueryParams:
        """Transform the query."""
        return SecCikMapQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: SecCikMapQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Return the raw data from the SEC endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_sec.utils.helpers import symbol_map

        results = {"cik": await symbol_map(query.symbol, query.use_cache)}
        if not results:
            return {"Error": "Symbol not found."}
        return results

    @staticmethod
    def transform_data(
        query: SecCikMapQueryParams, data: dict, **kwargs: Any
    ) -> SecCikMapData:
        """Transform the data to the standard format."""
        return SecCikMapData.model_validate(data)

```



---

## High-Level Overview

This is a **python** file named `cik_map.py`.

**Python Module**

- **Classes** (3): SecCikMapQueryParams, SecCikMapData, SecCikMapFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SecCikMapQueryParams`**(CikMapQueryParams)
- **`SecCikMapData`**(CikMapData)
- **`SecCikMapFetcher`**(
    Fetcher[
        SecCikMapQueryParams,
        SecCikMapData,
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `CikMapData`
- `Fetcher`
- `Field`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.cik_map`
- `openbb_sec.utils.helpers`
- `pydantic`
- `symbol_map`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.968932Z
**Generator**: World's Best Repo Book Generator v1.0
