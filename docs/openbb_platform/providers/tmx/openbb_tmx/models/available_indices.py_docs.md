# Documentation: openbb_platform/providers/tmx/openbb_tmx/models/available_indices.py

## File Metadata
- **Path**: `openbb_platform/providers/tmx/openbb_tmx/models/available_indices.py`
- **Size**: 4,789 characters, 135 lines
- **Words**: 361
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Available Indices fetcher for TMX"""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.available_indices import (
    AvailableIndicesData,
    AvailableIndicesQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class TmxAvailableIndicesQueryParams(AvailableIndicesQueryParams):
    """TMX Available Indices Query Params."""

    use_cache: bool = Field(
        default=True,
        description="Whether to use a cached request."
        + " Index data is from a single JSON file, updated each day after close."
        + " It is cached for one day. To bypass, set to False.",
    )


class TmxAvailableIndicesData(AvailableIndicesData):
    """TMX Available Indices Data."""

    symbol: str = Field(description="The ticker symbol of the index.")


class TmxAvailableIndicesFetcher(
    Fetcher[
        TmxAvailableIndicesQueryParams,
        list[TmxAvailableIndicesData],
    ]
):
    """Transform the query, extract and transform the data from the TMX endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> TmxAvailableIndicesQueryParams:
        """Transform the query params."""
        return TmxAvailableIndicesQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: TmxAvailableIndicesQueryParams,
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
        query: TmxAvailableIndicesQueryParams,
        data: dict,
        **kwargs: Any,
    ) -> list[TmxAvailableIndicesData]:
        """Transform the data to the standard format."""
        # pylint: disable=import-outside-toplevel
        import re

        data = data.copy()
        if data == {}:
            raise EmptyDataError

        # Extract the category for each index.
        symbols = {}
        for category, symbol_list in data["groups"].items():
            for symbol in symbol_list:
                if symbol not in symbols:
                    symbols[symbol] = category
                else:
                    symbols[symbol].append(category)
            category = {"category": symbols}  # noqa: PLW2901
        # Extract the data for each index and combine with the category.
        new_data = []
        for symbol in data["indices"]:
            overview = data["indices"][symbol].get("overview_en", None)
            if overview:
                # Remove HTML tags from the overview
                overview = re.sub("<.*?>", "", overview)
                # Remove additional artifacts from the overview
                overview = re.sub("\r|\n|amp;", "", overview)
            new_data.append(
                {
                    "symbol": symbol,
                    "name": data["indices"][symbol].get("name_en", None),
                    "currency": (
                        "USD"
                        if "(USD)" in data["indices"][symbol]["name_en"]
                        else "CAD"
                    ),
                    "category": symbols[symbol],
                    "market_value": (
                        data["indices"][symbol]["quotedmarketvalue"].get("total", None)
                        if data["indices"][symbol].get("quotedmarketvalue")
                        else None
                    ),
                    "num_constituents": data["indices"][symbol].get(
                        "nb_constituents", None
                    ),
                    "overview": (
                        overview
                        if data["indices"][symbol].get("overview") != ""
                        else None
                    ),
                    "methodology": (
                        data["indices"][symbol].get("methodology", None)
                        if data["indices"][symbol].get("methodology") != ""
                        else None
                    ),
                    "factsheet": (
                        data["indices"][symbol].get("factsheet", None)
                        if data["indices"][symbol].get("factsheet") != ""
                        else None
                    ),
                }
            )

        return [TmxAvailableIndicesData.model_validate(d) for d in new_data]

```

## High-Level Overview

Available Indices fetcher for TMX

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.available_indices import (
AvailableIndicesData,
AvailableIndicesQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class TmxAvailableIndicesQueryParams(AvailableIndicesQueryParams):
TMX Available Indices Query Params.
TMX Available Indices Data.

symbol: str = Field(description="The ticker symbol of the index.")

## Detailed Structure

### Python File Structure

**Classes** (3):
`TmxAvailableIndicesQueryParams`, `TmxAvailableIndicesData`, `TmxAvailableIndicesFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (17):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.available_indices`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `a`, `the`, `the`, `openbb_tmx.utils.helpers`, `get_data_from_url`, `re`, `the`, `the`


## Key Components

**Class `TmxAvailableIndicesQueryParams`**: TMX Available Indices Query Params.

**Class `TmxAvailableIndicesData`**: TMX Available Indices Data.

**Class `TmxAvailableIndicesFetcher`**: Transform the query, extract and transform the data from the TMX endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.available_indices`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `openbb_tmx.utils.helpers`
- `re`

## Notes
- Generated: 2025-11-18T07:54:41.763553
- Generator: World's Best Repo Book Generator v1.0.0
