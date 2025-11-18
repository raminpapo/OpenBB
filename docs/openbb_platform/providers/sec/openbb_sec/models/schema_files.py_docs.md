# Documentation: openbb_platform/providers/sec/openbb_sec/models/schema_files.py

## File Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/models/schema_files.py`
- **Size**: 2,063 characters, 65 lines
- **Words**: 190
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""SEC Schema Files List Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cot_search import CotSearchQueryParams
from pydantic import Field


class SecSchemaFilesQueryParams(CotSearchQueryParams):
    """SEC Schema Files List Query.

    Source: https://sec.gov/
    """

    url: str | None = Field(
        description="Enter an optional URL path to fetch the next level.", default=None
    )
    use_cache: bool | None = Field(
        default=True,
        description="Whether or not to use cache.",
    )


class SecSchemaFilesData(Data):
    """SEC Schema Files List Data."""

    files: list[str] = Field(description="Dictionary of URLs to SEC Schema Files")


class SecSchemaFilesFetcher(Fetcher[SecSchemaFilesQueryParams, SecSchemaFilesData]):
    """SEC Schema Files Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> SecSchemaFilesQueryParams:
        """Transform the query."""
        return SecSchemaFilesQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SecSchemaFilesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Return the raw data from the SEC endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_sec.utils.helpers import get_schema_filelist

        if query.url and ".xsd" in query.url or query.url and ".xml" in query.url:
            raise OpenBBError("Invalid URL. This endpoint does not parse the files.")
        results = get_schema_filelist(query.query, query.url)

        return {"files": results}

    @staticmethod
    def transform_data(
        query: SecSchemaFilesQueryParams, data: dict, **kwargs: Any
    ) -> SecSchemaFilesData:
        """Transform the data to the standard format."""
        return SecSchemaFilesData.model_validate(data)

```

## High-Level Overview

SEC Schema Files List Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cot_search import CotSearchQueryParams
from pydantic import Field


class SecSchemaFilesQueryParams(CotSearchQueryParams):
SEC Schema Files List Query.


url: str | None = Field(
description="Enter an optional URL path to fetch the next level.", default=None
)

## Detailed Structure

### Python File Structure

**Classes** (3):
`SecSchemaFilesQueryParams`, `SecSchemaFilesData`, `SecSchemaFilesFetcher`

**Functions** (3):
`transform_query`, `extract_data`, `transform_data`

**Imports** (15):
`typing`, `Any`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.cot_search`, `CotSearchQueryParams`, `pydantic`, `Field`, `the`, `openbb_sec.utils.helpers`, `get_schema_filelist`


## Key Components

**Class `SecSchemaFilesQueryParams`**: SEC Schema Files List Query.

    Source: https://sec.gov/

**Class `SecSchemaFilesData`**: SEC Schema Files List Data.

**Class `SecSchemaFilesFetcher`**: SEC Schema Files Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.cot_search`
- `pydantic`
- `openbb_sec.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:40.611685
- Generator: World's Best Repo Book Generator v1.0.0
