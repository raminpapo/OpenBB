# Documentation: openbb_platform/providers/intrinio/openbb_intrinio/models/institutional_ownership.py

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/institutional_ownership.py`
- **Size**: 4,419 characters, 131 lines
- **Words**: 338
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Intrinio Institutional Ownership Model."""

# pylint: disable=unused-argument

import asyncio
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.institutional_ownership import (
    InstitutionalOwnershipData,
    InstitutionalOwnershipQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.helpers import get_querystring
from openbb_intrinio.utils.helpers import get_data_many, get_data_one
from pydantic import Field


class IntrinioInstitutionalOwnershipQueryParams(InstitutionalOwnershipQueryParams):
    """Intrinio Institutional Ownership Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_security_insider_ownership_v2
            https://docs.intrinio.com/documentation/web_api/get_owner_by_id_v2
    """

    __alias_dict__ = {
        "limit": "page_size",
    }

    limit: int | None = Field(
        default=100,
        description=QUERY_DESCRIPTIONS.get("limit", ""),
    )


class IntrinioInstitutionalOwnershipData(InstitutionalOwnershipData):
    """Intrinio Institutional Ownership Data."""

    __alias_dict__ = {
        "cik": "owner_cik",
        "date": "period_ended",
        "name": "owner_name",
    }

    name: str = Field(
        description="Name of the institutional owner.",
    )
    value: float = Field(description="Value of the institutional owner.")
    amount: float = Field(description="Amount of the institutional owner.")
    sole_voting_authority: float = Field(
        description="Sole voting authority of the institutional owner."
    )
    shared_voting_authority: float = Field(
        description="Shared voting authority of the institutional owner."
    )
    no_voting_authority: float = Field(
        description="No voting authority of the institutional owner."
    )
    previous_amount: float = Field(
        description="Previous amount of the institutional owner."
    )
    amount_change: float = Field(
        description="Amount change of the institutional owner."
    )
    amount_percent_change: float = Field(
        description="Amount percent change of the institutional owner."
    )


class IntrinioInstitutionalOwnershipFetcher(
    Fetcher[
        IntrinioInstitutionalOwnershipQueryParams,
        list[IntrinioInstitutionalOwnershipData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> IntrinioInstitutionalOwnershipQueryParams:
        """Transform the query params."""
        return IntrinioInstitutionalOwnershipQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: IntrinioInstitutionalOwnershipQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""
        data: list[dict] = []

        base_url = "https://api-v2.intrinio.com"
        query_str = get_querystring(query.model_dump(by_alias=True), ["symbol"])
        url = f"{base_url}/securities/{query.symbol}/institutional_ownership?{query_str}&api_key={api_key}"

        async def get_owner_name(item: dict) -> dict:
            cik = item["owner_cik"]
            cik_url = f"{base_url}/owners/{cik}?api_key={api_key}"
            cik_data = await get_data_one(cik_url, **kwargs)
            owner_name = cik_data["owner_name"]
            item["symbol"] = query.symbol
            item["owner_name"] = owner_name
            return item

        results = await asyncio.gather(
            *[
                get_owner_name(item)
                for item in await get_data_many(url, "ownership", **kwargs)
            ],
            return_exceptions=True,
        )

        for item in results:
            if isinstance(item, Exception):
                continue
            data.append(item)  # type: ignore

        return data

    @staticmethod
    def transform_data(
        query: IntrinioInstitutionalOwnershipQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[IntrinioInstitutionalOwnershipData]:
        """Return the transformed data."""
        return [IntrinioInstitutionalOwnershipData.model_validate(d) for d in data]

```

## High-Level Overview

Intrinio Institutional Ownership Model.

# pylint: disable=unused-argument

import asyncio
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.institutional_ownership import (
InstitutionalOwnershipData,
InstitutionalOwnershipQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.helpers import get_querystring
from openbb_intrinio.utils.helpers import get_data_many, get_data_one
from pydantic import Field


class IntrinioInstitutionalOwnershipQueryParams(InstitutionalOwnershipQueryParams):
Intrinio Institutional Ownership Query.

## Detailed Structure

### Python File Structure

**Classes** (3):
`IntrinioInstitutionalOwnershipQueryParams`, `IntrinioInstitutionalOwnershipData`, `IntrinioInstitutionalOwnershipFetcher`

**Functions** (4):
`transform_query`, `aextract_data`, `get_owner_name`, `transform_data`

**Imports** (16):
`asyncio`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.institutional_ownership`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `openbb_core.provider.utils.helpers`, `get_querystring`, `openbb_intrinio.utils.helpers`, `get_data_many`, `pydantic`, `Field`, `the`, `the`


## Key Components

**Class `IntrinioInstitutionalOwnershipQueryParams`**: Intrinio Institutional Ownership Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_security_insider_ownership_v2
            https://docs.intrinio.com/documentation/web_api/get_o

**Class `IntrinioInstitutionalOwnershipData`**: Intrinio Institutional Ownership Data.

**Class `IntrinioInstitutionalOwnershipFetcher`**: Transform the query, extract and transform the data from the Intrinio endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `asyncio`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.institutional_ownership`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.helpers`
- `openbb_intrinio.utils.helpers`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:40.129111
- Generator: World's Best Repo Book Generator v1.0.0
