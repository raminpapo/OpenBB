# Documentation: openbb_platform/providers/tiingo/openbb_tiingo/models/trailing_dividend_yield.py

## File Metadata
- **Path**: `openbb_platform/providers/tiingo/openbb_tiingo/models/trailing_dividend_yield.py`
- **Size**: 2,104 characters, 65 lines
- **Words**: 156
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Tiingo Trailing Dividend Yield Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.trailing_dividend_yield import (
TrailingDivYieldData,
TrailingDivYieldQueryParams,
)


class TiingoTrailingDivYieldQueryParams(TrailingDivYieldQueryParams):
Tiingo Trailing Dividend Yield Query.



class TiingoTrailingDivYieldData(TrailingDivYieldData):
Tiingo Trailing Dividend Yield Data.

## Detailed Structure

### Python File Structure

**Classes** (3):
`TiingoTrailingDivYieldQueryParams`, `TiingoTrailingDivYieldData`, `TiingoTrailingDivYieldFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (9):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.trailing_dividend_yield`, `the`, `the`, `openbb_tiingo.utils.helpers`, `get_data`


## Key Components

**Class `TiingoTrailingDivYieldQueryParams`**: Tiingo Trailing Dividend Yield Query.

    Source: https://www.tiingo.com/documentation/end-of-day

**Class `TiingoTrailingDivYieldData`**: Tiingo Trailing Dividend Yield Data.

**Class `TiingoTrailingDivYieldFetcher`**: Transform the query, extract and transform the data from the Tiingo endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.trailing_dividend_yield`
- `openbb_tiingo.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:41.719535
- Generator: World's Best Repo Book Generator v1.0.0
