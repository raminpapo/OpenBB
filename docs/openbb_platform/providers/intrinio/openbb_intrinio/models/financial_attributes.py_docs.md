# Documentation: openbb_platform/providers/intrinio/openbb_intrinio/models/financial_attributes.py

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/financial_attributes.py`
- **Size**: 2,781 characters, 81 lines
- **Words**: 203
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Intrinio Financial Attributes Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.financial_attributes import (
    FinancialAttributesData,
    FinancialAttributesQueryParams,
)
from openbb_core.provider.utils.helpers import get_querystring
from openbb_intrinio.utils.helpers import get_data_many


class IntrinioFinancialAttributesQueryParams(FinancialAttributesQueryParams):
    """Intrinio Financial Attributes Query."""

    __alias_dict__ = {"sort": "sort_order", "limit": "page_size"}


class IntrinioFinancialAttributesData(FinancialAttributesData):
    """Intrinio Financial Attributes Data."""


class IntrinioFinancialAttributesFetcher(
    Fetcher[
        IntrinioFinancialAttributesQueryParams,
        list[IntrinioFinancialAttributesData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> IntrinioFinancialAttributesQueryParams:
        """Transform the query params."""
        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=5)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return IntrinioFinancialAttributesQueryParams(**transformed_params)

    @staticmethod
    async def aextract_data(
        query: IntrinioFinancialAttributesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""
        frequency = "yearly" if query.period == "annual" else "quarterly"
        data: list[dict] = []

        base_url = "https://api-v2.intrinio.com"
        query_str = get_querystring(query.model_dump(by_alias=True), ["frequency"])
        query_str = f"{query_str}&frequency={frequency}"

        url = f"{base_url}/historical_data/{query.symbol}/{query.tag}?{query_str}&api_key={api_key}"
        # data = get_data_one(url).get("historical_data", [])
        data = await get_data_many(url, "historical_data")

        return data

    @staticmethod
    def transform_data(
        query: IntrinioFinancialAttributesQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[IntrinioFinancialAttributesData]:
        """Return the transformed data."""
        return [IntrinioFinancialAttributesData.model_validate(item) for item in data]

```

## High-Level Overview

Intrinio Financial Attributes Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.financial_attributes import (
FinancialAttributesData,
FinancialAttributesQueryParams,
)
from openbb_core.provider.utils.helpers import get_querystring
from openbb_intrinio.utils.helpers import get_data_many


class IntrinioFinancialAttributesQueryParams(FinancialAttributesQueryParams):
Intrinio Financial Attributes Query.
Intrinio Financial Attributes Data.

## Detailed Structure

### Python File Structure

**Classes** (3):
`IntrinioFinancialAttributesQueryParams`, `IntrinioFinancialAttributesData`, `IntrinioFinancialAttributesFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (15):
`datetime`, `datetime`, `typing`, `Any`, `dateutil.relativedelta`, `relativedelta`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.financial_attributes`, `openbb_core.provider.utils.helpers`, `get_querystring`, `openbb_intrinio.utils.helpers`, `get_data_many`, `the`, `the`


## Key Components

**Class `IntrinioFinancialAttributesQueryParams`**: Intrinio Financial Attributes Query.

**Class `IntrinioFinancialAttributesData`**: Intrinio Financial Attributes Data.

**Class `IntrinioFinancialAttributesFetcher`**: Transform the query, extract and transform the data from the Intrinio endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `dateutil.relativedelta`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.financial_attributes`
- `openbb_core.provider.utils.helpers`
- `openbb_intrinio.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:40.102598
- Generator: World's Best Repo Book Generator v1.0.0
