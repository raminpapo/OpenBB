# Documentation: openbb_platform/providers/tmx/openbb_tmx/models/index_constituents.py

## File Metadata
- **Path**: `openbb_platform/providers/tmx/openbb_tmx/models/index_constituents.py`
- **Size**: 3,194 characters, 99 lines
- **Words**: 271
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""TMX Index Constituents Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_constituents import (
    IndexConstituentsData,
    IndexConstituentsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class TmxIndexConstituentsQueryParams(IndexConstituentsQueryParams):
    """TMX Index Constituents Query Params."""

    use_cache: bool = Field(
        default=True,
        description="Whether to use a cached request."
        + " Index data is from a single JSON file, updated each day after close."
        + " It is cached for one day. To bypass, set to False.",
    )


class TmxIndexConstituentsData(IndexConstituentsData):
    """TMX Index Constituents Data."""

    __alias_dict__ = {
        "market_value": "quotedmarketvalue",
    }

    market_value: float | None = Field(
        default=None,
        description="The quoted market value of the asset.",
    )

    @field_validator("weight", mode="before", check_fields=False)
    @classmethod
    def normalize_percent(cls, v):
        """Return percents as normalized percentage points."""
        return float(v) / 100 if v else None


class TmxIndexConstituentsFetcher(
    Fetcher[
        TmxIndexConstituentsQueryParams,
        list[TmxIndexConstituentsData],
    ]
):
    """TMX Index Constituents Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> TmxIndexConstituentsQueryParams:
        """Transform the query."""
        return TmxIndexConstituentsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: TmxIndexConstituentsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Return the raw data from the TMX endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_tmx.utils.helpers import get_data_from_url, get_indices_backend

        url = "https://tmxinfoservices.com/files/indices/sptsx-indices.json"

        data = await get_data_from_url(
            url,
            use_cache=query.use_cache,
            backend=get_indices_backend(),
        )

        return data

    @staticmethod
    def transform_data(
        query: TmxIndexConstituentsQueryParams, data: dict, **kwargs
    ) -> list[TmxIndexConstituentsData]:
        """Return the transformed data."""
        results = []
        data = data.copy()
        if data == {}:
            raise EmptyDataError
        if query.symbol not in data.get("indices"):  # type: ignore
            raise OpenBBError(f"Index {query.symbol} was not found. Check the symbol.")
        index_data = data["indices"][query.symbol]
        if (
            index_data.get("nb_constituents") == 0
            or index_data.get("constituents") is None
        ):
            raise OpenBBError(f"No constituents found for index, {query.symbol}")
        results = index_data["constituents"]
        return [TmxIndexConstituentsData.model_validate(d) for d in results]

```

## High-Level Overview

TMX Index Constituents Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_constituents import (
IndexConstituentsData,
IndexConstituentsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class TmxIndexConstituentsQueryParams(IndexConstituentsQueryParams):
TMX Index Constituents Query Params.
TMX Index Constituents Data.


## Detailed Structure

### Python File Structure

**Classes** (3):
`TmxIndexConstituentsQueryParams`, `TmxIndexConstituentsData`, `TmxIndexConstituentsFetcher`

**Functions** (4):
`normalize_percent`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (15):
`typing`, `Any`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.index_constituents`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `a`, `the`, `openbb_tmx.utils.helpers`, `get_data_from_url`


## Key Components

**Class `TmxIndexConstituentsQueryParams`**: TMX Index Constituents Query Params.

**Class `TmxIndexConstituentsData`**: TMX Index Constituents Data.

**Class `TmxIndexConstituentsFetcher`**: TMX Index Constituents Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.index_constituents`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `openbb_tmx.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:41.796066
- Generator: World's Best Repo Book Generator v1.0.0
