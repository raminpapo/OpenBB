# File Documentation: institutions_search.py

## Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/models/institutions_search.py`
- **Size**: 2,207 bytes
- **Lines**: 76
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `institutions_search.py`.

**Python Module**

- **Classes** (3): SecInstitutionsSearchQueryParams, SecInstitutionsSearchData, SecInstitutionsSearchFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SecInstitutionsSearchQueryParams`**(CotSearchQueryParams)
- **`SecInstitutionsSearchData`**(Data)
- **`SecInstitutionsSearchFetcher`**(
    Fetcher[
        SecInstitutionsSearchQueryParams,
        list[SecInstitutionsSearchData],
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `CotSearchQueryParams`
- `Data`
- `Fetcher`
- `Field`
- `get_all_ciks`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.cot_search`
- `openbb_sec.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.983912Z
**Generator**: World's Best Repo Book Generator v1.0
