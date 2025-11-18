# Documentation: openbb_platform/providers/sec/openbb_sec/models/institutions_search.py

## File Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/models/institutions_search.py`
- **Size**: 2,207 characters, 76 lines
- **Words**: 181
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""SEC Institutions Search Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cot_search import CotSearchQueryParams
from pydantic import Field


class SecInstitutionsSearchQueryParams(CotSearchQueryParams):
    """SEC Institutions Search Query.

    Source: https://sec.gov/
    """

    use_cache: bool | None = Field(
        default=True,
        description="Whether or not to use cache.",
    )


class SecInstitutionsSearchData(Data):
    """SEC Institutions Search Data."""

    __alias_dict__ = {
        "name": "Institution",
        "cik": "CIK Number",
    }

    name: str | None = Field(
        default=None,
        description="The name of the institution.",
    )
    cik: str | int | None = Field(
        default=None,
        description="Central Index Key (CIK)",
    )


class SecInstitutionsSearchFetcher(
    Fetcher[
        SecInstitutionsSearchQueryParams,
        list[SecInstitutionsSearchData],
    ]
):
    """SEC Institutions Search Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> SecInstitutionsSearchQueryParams:
        """Transform the query."""
        return SecInstitutionsSearchQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: SecInstitutionsSearchQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the SEC endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_sec.utils.helpers import get_all_ciks

        institutions = await get_all_ciks(use_cache=query.use_cache)
        hp = institutions["Institution"].str.contains(query.query, case=False)
        return institutions[hp].astype(str).to_dict("records")

    @staticmethod
    def transform_data(
        query: SecInstitutionsSearchQueryParams, data: list[dict], **kwargs: Any
    ) -> list[SecInstitutionsSearchData]:
        """Transform the data to the standard format."""
        return [SecInstitutionsSearchData.model_validate(d) for d in data]

```

## High-Level Overview

SEC Institutions Search Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cot_search import CotSearchQueryParams
from pydantic import Field


class SecInstitutionsSearchQueryParams(CotSearchQueryParams):
SEC Institutions Search Query.


use_cache: bool | None = Field(
default=True,
description="Whether or not to use cache.",
)

## Detailed Structure

### Python File Structure

**Classes** (3):
`SecInstitutionsSearchQueryParams`, `SecInstitutionsSearchData`, `SecInstitutionsSearchFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (13):
`typing`, `Any`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.cot_search`, `CotSearchQueryParams`, `pydantic`, `Field`, `the`, `openbb_sec.utils.helpers`, `get_all_ciks`


## Key Components

**Class `SecInstitutionsSearchQueryParams`**: SEC Institutions Search Query.

    Source: https://sec.gov/

**Class `SecInstitutionsSearchData`**: SEC Institutions Search Data.

**Class `SecInstitutionsSearchFetcher`**: SEC Institutions Search Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.cot_search`
- `pydantic`
- `openbb_sec.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:40.595969
- Generator: World's Best Repo Book Generator v1.0.0
