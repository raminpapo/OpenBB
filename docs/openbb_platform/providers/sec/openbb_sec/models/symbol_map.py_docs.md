# Documentation: openbb_platform/providers/sec/openbb_sec/models/symbol_map.py

## File Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/models/symbol_map.py`
- **Size**: 1,898 characters, 63 lines
- **Words**: 162
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

SEC Symbol Mapping Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.symbol_map import SymbolMapQueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class SecSymbolMapQueryParams(SymbolMapQueryParams):
SEC Symbol Mapping Query.



class SecSymbolMapData(Data):

## Detailed Structure

### Python File Structure

**Classes** (3):
`SecSymbolMapQueryParams`, `SecSymbolMapData`, `SecSymbolMapFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (18):
`typing`, `Any`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.symbol_map`, `SymbolMapQueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`, `the`, `the`, `openbb_sec.utils.helpers`, `cik_map`


## Key Components

**Class `SecSymbolMapQueryParams`**: SEC Symbol Mapping Query.

    Source: https://sec.gov/

**Class `SecSymbolMapData`**: SEC symbol map Data.

**Class `SecSymbolMapFetcher`**: Transform the query, extract and transform the data from the SEC endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.symbol_map`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `openbb_sec.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:40.618853
- Generator: World's Best Repo Book Generator v1.0.0
