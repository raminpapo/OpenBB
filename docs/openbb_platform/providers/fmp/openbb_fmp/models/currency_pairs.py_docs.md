# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/currency_pairs.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/currency_pairs.py`
- **Size**: 3,048 characters, 88 lines
- **Words**: 245
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Currency Available Pairs Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.currency_pairs import (
    CurrencyPairsData,
    CurrencyPairsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FMPCurrencyPairsQueryParams(CurrencyPairsQueryParams):
    """FMP Currency Available Pairs Query.

    Source: https://site.financialmodelingprep.com/developer/docs#forex
    """


class FMPCurrencyPairsData(CurrencyPairsData):
    """FMP Currency Available Pairs Data."""

    symbol: str = Field(description="Symbol of the currency pair.")
    from_currency: str = Field(description="Base currency of the currency pair.")
    to_currency: str = Field(description="Quote currency of the currency pair.")
    from_name: str = Field(description="Name of the base currency.")
    to_name: str = Field(description="Name of the quote currency.")


class FMPCurrencyPairsFetcher(
    Fetcher[
        FMPCurrencyPairsQueryParams,
        list[FMPCurrencyPairsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPCurrencyPairsQueryParams:
        """Transform the query params."""
        return FMPCurrencyPairsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPCurrencyPairsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        url = f"https://financialmodelingprep.com/stable/forex-list?apikey={api_key}"

        return await get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPCurrencyPairsQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPCurrencyPairsData]:
        """Return the transformed data."""
        # pylint: disable=import-outside-toplevel
        from pandas import DataFrame

        if not data:
            raise EmptyDataError("The request was returned empty.")

        df = DataFrame(data)

        if query.query:
            df = df[
                df["symbol"].str.contains(query.query, case=False)
                | df["fromCurrency"].str.contains(query.query, case=False)
                | df["toCurrency"].str.contains(query.query, case=False)
                | df["fromName"].str.contains(query.query, case=False)
                | df["toName"].str.contains(query.query, case=False)
            ]

        if len(df) == 0:
            raise EmptyDataError(
                f"No results were found with the query supplied. -> {query.query}"
            )
        return [FMPCurrencyPairsData.model_validate(d) for d in df.to_dict("records")]

```

## High-Level Overview

FMP Currency Available Pairs Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.currency_pairs import (
CurrencyPairsData,
CurrencyPairsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FMPCurrencyPairsQueryParams(CurrencyPairsQueryParams):
FMP Currency Available Pairs Query.




## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPCurrencyPairsQueryParams`, `FMPCurrencyPairsData`, `FMPCurrencyPairsFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (15):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.currency_pairs`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `the`, `the`, `openbb_fmp.utils.helpers`, `get_data_many`, `pandas`, `DataFrame`


## Key Components

**Class `FMPCurrencyPairsQueryParams`**: FMP Currency Available Pairs Query.

    Source: https://site.financialmodelingprep.com/developer/docs#forex

**Class `FMPCurrencyPairsData`**: FMP Currency Available Pairs Data.

**Class `FMPCurrencyPairsFetcher`**: Transform the query, extract and transform the data from the FMP endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.currency_pairs`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `openbb_fmp.utils.helpers`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:39.338149
- Generator: World's Best Repo Book Generator v1.0.0
