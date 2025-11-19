# File Documentation: currency_pairs.py

## Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/currency_pairs.py`
- **Size**: 3,067 bytes
- **Lines**: 91
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Intrinio Currency Available Pairs Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.currency_pairs import (
    CurrencyPairsData,
    CurrencyPairsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class IntrinioCurrencyPairsQueryParams(CurrencyPairsQueryParams):
    """Intrinio Currency Available Pairs Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_forex_pairs_v2
    """


class IntrinioCurrencyPairsData(CurrencyPairsData):
    """Intrinio Currency Available Pairs Data."""

    __alias_dict__ = {"symbol": "code"}

    base_currency: str = Field(
        description="ISO 4217 currency code of the base currency."
    )
    quote_currency: str = Field(
        description="ISO 4217 currency code of the quote currency."
    )


class IntrinioCurrencyPairsFetcher(
    Fetcher[
        IntrinioCurrencyPairsQueryParams,
        list[IntrinioCurrencyPairsData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> IntrinioCurrencyPairsQueryParams:
        """Transform the query params."""
        return IntrinioCurrencyPairsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: IntrinioCurrencyPairsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Intrinio endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_intrinio.utils.helpers import get_data_many

        api_key = credentials.get("intrinio_api_key") if credentials else ""

        base_url = "https://api-v2.intrinio.com"
        url = f"{base_url}/forex/pairs?api_key={api_key}"
        return await get_data_many(url, "pairs", **kwargs)

    @staticmethod
    def transform_data(
        query: IntrinioCurrencyPairsQueryParams, data: list[dict], **kwargs: Any
    ) -> list[IntrinioCurrencyPairsData]:
        """Return the transformed data."""
        # pylint: disable=import-outside-toplevel
        from pandas import DataFrame

        if not data:
            raise EmptyDataError("The request was returned empty.")
        df = DataFrame(data)
        if query.query:
            df = df[
                df["code"].str.contains(query.query, case=False)
                | df["base_currency"].str.contains(query.query, case=False)
                | df["quote_currency"].str.contains(query.query, case=False)
            ]
        if len(df) == 0:
            raise EmptyDataError(
                f"No results were found with the query supplied. -> {query.query}"
                + " Hint: Names and descriptions are not searchable from Intrinio, try 3-letter symbols."
            )
        return [
            IntrinioCurrencyPairsData.model_validate(d)
            for d in df.to_dict(orient="records")
        ]

```



---

## High-Level Overview

This is a **python** file named `currency_pairs.py`.

**Python Module**

- **Classes** (3): IntrinioCurrencyPairsQueryParams, IntrinioCurrencyPairsData, IntrinioCurrencyPairsFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IntrinioCurrencyPairsQueryParams`**(CurrencyPairsQueryParams)
- **`IntrinioCurrencyPairsData`**(CurrencyPairsData)
- **`IntrinioCurrencyPairsFetcher`**(
    Fetcher[
        IntrinioCurrencyPairsQueryParams,
        list[IntrinioCurrencyPairsData],
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `DataFrame`
- `EmptyDataError`
- `Fetcher`
- `Field`
- `get_data_many`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.currency_pairs`
- `openbb_core.provider.utils.errors`
- `openbb_intrinio.utils.helpers`
- `pandas`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.400594Z
**Generator**: World's Best Repo Book Generator v1.0
