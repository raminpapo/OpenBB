# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/key_executives.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/key_executives.py`
- **Size**: 1,867 characters, 63 lines
- **Words**: 138
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Key Executives Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.key_executives import (
    KeyExecutivesData,
    KeyExecutivesQueryParams,
)
from pydantic import ConfigDict


class FMPKeyExecutivesQueryParams(KeyExecutivesQueryParams):
    """FMP Key Executives Query.

    Source: https://site.financialmodelingprep.com/developer/docs#company-executives
    """


class FMPKeyExecutivesData(KeyExecutivesData):
    """FMP Key Executives Data."""

    model_config = ConfigDict(extra="ignore")


class FMPKeyExecutivesFetcher(
    Fetcher[
        FMPKeyExecutivesQueryParams,
        list[FMPKeyExecutivesData],
    ]
):
    """FMP Key Executives Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPKeyExecutivesQueryParams:
        """Transform the query params."""
        return FMPKeyExecutivesQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPKeyExecutivesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        base_url = "https://financialmodelingprep.com/stable"
        url = f"{base_url}/key-executives?symbol={query.symbol}&apikey={api_key}"

        return await get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPKeyExecutivesQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPKeyExecutivesData]:
        """Return the transformed data."""
        return [FMPKeyExecutivesData.model_validate(d) for d in data]

```

## High-Level Overview

FMP Key Executives Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.key_executives import (
KeyExecutivesData,
KeyExecutivesQueryParams,
)
from pydantic import ConfigDict


class FMPKeyExecutivesQueryParams(KeyExecutivesQueryParams):
FMP Key Executives Query.



class FMPKeyExecutivesData(KeyExecutivesData):

## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPKeyExecutivesQueryParams`, `FMPKeyExecutivesData`, `FMPKeyExecutivesFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (10):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.key_executives`, `pydantic`, `ConfigDict`, `the`, `openbb_fmp.utils.helpers`, `get_data_many`


## Key Components

**Class `FMPKeyExecutivesQueryParams`**: FMP Key Executives Query.

    Source: https://site.financialmodelingprep.com/developer/docs#company-executives

**Class `FMPKeyExecutivesData`**: FMP Key Executives Data.

**Class `FMPKeyExecutivesFetcher`**: FMP Key Executives Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.key_executives`
- `pydantic`
- `openbb_fmp.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:39.402625
- Generator: World's Best Repo Book Generator v1.0.0
