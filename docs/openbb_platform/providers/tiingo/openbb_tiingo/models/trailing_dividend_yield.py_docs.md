# File Documentation: trailing_dividend_yield.py

## Metadata
- **Path**: `openbb_platform/providers/tiingo/openbb_tiingo/models/trailing_dividend_yield.py`
- **Size**: 2,104 bytes
- **Lines**: 65
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Tiingo Trailing Dividend Yield Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.trailing_dividend_yield import (
    TrailingDivYieldData,
    TrailingDivYieldQueryParams,
)


class TiingoTrailingDivYieldQueryParams(TrailingDivYieldQueryParams):
    """Tiingo Trailing Dividend Yield Query.

    Source: https://www.tiingo.com/documentation/end-of-day
    """


class TiingoTrailingDivYieldData(TrailingDivYieldData):
    """Tiingo Trailing Dividend Yield Data."""

    __alias_dict__ = {"trailing_dividend_yield": "trailingDiv1Y"}


class TiingoTrailingDivYieldFetcher(
    Fetcher[
        TiingoTrailingDivYieldQueryParams,
        list[TiingoTrailingDivYieldData],
    ]
):
    """Transform the query, extract and transform the data from the Tiingo endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> TiingoTrailingDivYieldQueryParams:
        """Transform the query params."""
        transformed_params = params
        return TiingoTrailingDivYieldQueryParams(**transformed_params)

    @staticmethod
    async def aextract_data(
        query: TiingoTrailingDivYieldQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Tiingo endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_tiingo.utils.helpers import get_data

        api_key = credentials.get("tiingo_token") if credentials else ""
        url = f"https://api.tiingo.com/tiingo/corporate-actions/{query.symbol}/distribution-yield?token={api_key}"

        return await get_data(url)  # type: ignore

    @staticmethod
    def transform_data(
        query: TiingoTrailingDivYieldQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[TiingoTrailingDivYieldData]:
        """Return the transformed data."""
        data = data[-query.limit :] if query.limit else data
        return [TiingoTrailingDivYieldData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `trailing_dividend_yield.py`.

**Python Module**

- **Classes** (3): TiingoTrailingDivYieldQueryParams, TiingoTrailingDivYieldData, TiingoTrailingDivYieldFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TiingoTrailingDivYieldQueryParams`**(TrailingDivYieldQueryParams)
- **`TiingoTrailingDivYieldData`**(TrailingDivYieldData)
- **`TiingoTrailingDivYieldFetcher`**(
    Fetcher[
        TiingoTrailingDivYieldQueryParams,
        list[TiingoTrailingDivYieldData],
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
- `get_data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.trailing_dividend_yield`
- `openbb_tiingo.utils.helpers`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:53.015293Z
**Generator**: World's Best Repo Book Generator v1.0
