# File Documentation: equity_info.py

## Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/equity_info.py`
- **Size**: 2,354 bytes
- **Lines**: 79
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Intrinio Equity Info Model."""

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_info import (
    EquityInfoData,
    EquityInfoQueryParams,
)
from openbb_core.provider.utils.helpers import (
    amake_requests,
)
from openbb_intrinio.utils.helpers import response_callback
from pydantic import Field


class IntrinioEquityInfoQueryParams(EquityInfoQueryParams):
    """Intrinio Equity Info Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_company_v2
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class IntrinioEquityInfoData(EquityInfoData):
    """Intrinio Equity Info Data."""

    __alias_dict__ = {
        "symbol": "ticker",
    }

    id: str = Field(default=None, description="Intrinio ID for the company.")
    thea_enabled: bool | None = Field(
        default=None, description="Whether the company has been enabled for Thea."
    )


class IntrinioEquityInfoFetcher(
    Fetcher[
        IntrinioEquityInfoQueryParams,
        list[IntrinioEquityInfoData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> IntrinioEquityInfoQueryParams:
        """Transform the query."""
        return IntrinioEquityInfoQueryParams(**params)

    # pylint: disable=W0613:unused-argument
    @staticmethod
    async def aextract_data(
        query: IntrinioEquityInfoQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""
        base_url = "https://api-v2.intrinio.com"

        urls = [
            f"{base_url}/companies/{s.strip()}?api_key={api_key}"
            for s in query.symbol.split(",")
        ]

        return await amake_requests(urls, response_callback, **kwargs)

    # pylint: disable=W0613:unused-argument
    @staticmethod
    def transform_data(
        query: IntrinioEquityInfoQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[IntrinioEquityInfoData]:
        """Transform the data."""
        return [IntrinioEquityInfoData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `equity_info.py`.

**Python Module**

- **Classes** (3): IntrinioEquityInfoQueryParams, IntrinioEquityInfoData, IntrinioEquityInfoFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IntrinioEquityInfoQueryParams`**(EquityInfoQueryParams)
- **`IntrinioEquityInfoData`**(EquityInfoData)
- **`IntrinioEquityInfoFetcher`**(
    Fetcher[
        IntrinioEquityInfoQueryParams,
        list[IntrinioEquityInfoData],
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Field`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_info`
- `openbb_core.provider.utils.helpers`
- `openbb_intrinio.utils.helpers`
- `pydantic`
- `response_callback`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.405117Z
**Generator**: World's Best Repo Book Generator v1.0
