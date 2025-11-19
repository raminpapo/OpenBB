# File Documentation: symbol_map.py

## Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/models/symbol_map.py`
- **Size**: 1,898 bytes
- **Lines**: 63
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""SEC Symbol Mapping Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.symbol_map import SymbolMapQueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class SecSymbolMapQueryParams(SymbolMapQueryParams):
    """SEC Symbol Mapping Query.

    Source: https://sec.gov/
    """


class SecSymbolMapData(Data):
    """SEC symbol map Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))


class SecSymbolMapFetcher(
    Fetcher[
        SecSymbolMapQueryParams,
        SecSymbolMapData,
    ]
):
    """Transform the query, extract and transform the data from the SEC endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> SecSymbolMapQueryParams:
        """Transform the query."""
        return SecSymbolMapQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: SecSymbolMapQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Return the raw data from the SEC endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_sec.utils.helpers import cik_map

        if not query.query.isdigit():
            raise OpenBBError("Query is required and must be a valid CIK.")
        symbol = await cik_map(int(query.query), query.use_cache)
        response = {"symbol": symbol}
        return response

    @staticmethod
    def transform_data(
        query: SecSymbolMapQueryParams, data: dict, **kwargs: Any
    ) -> SecSymbolMapData:
        """Transform the data to the standard format."""
        return SecSymbolMapData.model_validate(data)

```



---

## High-Level Overview

This is a **python** file named `symbol_map.py`.

**Python Module**

- **Classes** (3): SecSymbolMapQueryParams, SecSymbolMapData, SecSymbolMapFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SecSymbolMapQueryParams`**(SymbolMapQueryParams)
- **`SecSymbolMapData`**(Data)
- **`SecSymbolMapFetcher`**(
    Fetcher[
        SecSymbolMapQueryParams,
        SecSymbolMapData,
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `DATA_DESCRIPTIONS`
- `Data`
- `Fetcher`
- `Field`
- `OpenBBError`
- `SymbolMapQueryParams`
- `cik_map`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.symbol_map`
- `openbb_core.provider.utils.descriptions`
- `openbb_sec.utils.helpers`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:52.013881Z
**Generator**: World's Best Repo Book Generator v1.0
