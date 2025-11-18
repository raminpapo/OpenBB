# Documentation: openbb_platform/providers/intrinio/openbb_intrinio/models/search_attributes.py

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/search_attributes.py`
- **Size**: 2,409 characters, 76 lines
- **Words**: 185
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Intrinio Search Attributes Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.search_attributes import (
    SearchAttributesData,
    SearchAttributesQueryParams,
)
from openbb_core.provider.utils.helpers import get_querystring
from openbb_intrinio.utils.helpers import get_data_one


class IntrinioSearchAttributesQueryParams(SearchAttributesQueryParams):
    """Intrinio Search Attributes Query.

    Source: https://docs.intrinio.com/documentation/web_api/search_data_tags_v2
    """

    __alias_dict__ = {"limit": "page_size"}


class IntrinioSearchAttributesData(SearchAttributesData):
    """Intrinio Search Attributes Data."""

    __alias_dict__ = {
        "parent_name": "parent",
        "transaction": "balance",
    }


class IntrinioSearchAttributesFetcher(
    Fetcher[
        IntrinioSearchAttributesQueryParams,
        list[IntrinioSearchAttributesData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> IntrinioSearchAttributesQueryParams:
        """Transform the query params."""
        return IntrinioSearchAttributesQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: IntrinioSearchAttributesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""

        base_url = "https://api-v2.intrinio.com"
        query_str = get_querystring(query.model_dump(by_alias=True), [])

        url = f"{base_url}/data_tags/search?{query_str}&api_key={api_key}"
        data = await get_data_one(url, **kwargs)

        # Intrinio doesn't return the correct number of results when using the limit parameter
        # Temporary fix until they fix it
        data = data.get("tags", [])[: query.limit]

        return data

    @staticmethod
    def transform_data(
        query: IntrinioSearchAttributesQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[IntrinioSearchAttributesData]:
        """Return the transformed data."""
        return [IntrinioSearchAttributesData.model_validate(item) for item in data]

```

## High-Level Overview

Intrinio Search Attributes Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.search_attributes import (
SearchAttributesData,
SearchAttributesQueryParams,
)
from openbb_core.provider.utils.helpers import get_querystring
from openbb_intrinio.utils.helpers import get_data_one


class IntrinioSearchAttributesQueryParams(SearchAttributesQueryParams):
Intrinio Search Attributes Query.


__alias_dict__ = {"limit": "page_size"}

## Detailed Structure

### Python File Structure

**Classes** (3):
`IntrinioSearchAttributesQueryParams`, `IntrinioSearchAttributesData`, `IntrinioSearchAttributesFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (11):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.search_attributes`, `openbb_core.provider.utils.helpers`, `get_querystring`, `openbb_intrinio.utils.helpers`, `get_data_one`, `the`, `the`


## Key Components

**Class `IntrinioSearchAttributesQueryParams`**: Intrinio Search Attributes Query.

    Source: https://docs.intrinio.com/documentation/web_api/search_data_tags_v2

**Class `IntrinioSearchAttributesData`**: Intrinio Search Attributes Data.

**Class `IntrinioSearchAttributesFetcher`**: Transform the query, extract and transform the data from the Intrinio endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.search_attributes`
- `openbb_core.provider.utils.helpers`
- `openbb_intrinio.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:40.148961
- Generator: World's Best Repo Book Generator v1.0.0
