# File Documentation: options_chains.py

## Metadata
- **Path**: `openbb_platform/providers/tmx/openbb_tmx/models/options_chains.py`
- **Size**: 3,625 bytes
- **Lines**: 116
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""TMX Options Chains Model."""

# pylint: disable=unused-argument
from datetime import (
    date as dateType,
    datetime,
)
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.options_chains import (
    OptionsChainsData,
    OptionsChainsQueryParams,
)
from openbb_core.provider.utils.descriptions import (
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class TmxOptionsChainsQueryParams(OptionsChainsQueryParams):
    """TMX Options Chains Query.

    Source: https://www.Tmx.com/
    """

    date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("date", ""),
        default=None,
    )
    use_cache: bool = Field(
        default=True,
        description="Caching is used to validate the supplied ticker symbol, or if a historical EOD chain is requested."
        + " To bypass, set to False.",
    )


class TmxOptionsChainsData(OptionsChainsData):
    """TMX Options Chains Data."""

    __doc__ = OptionsChainsData.__doc__

    transactions: list[int | None] = Field(
        default_factory=list, description="Number of transactions for the contract."
    )
    total_value: list[float | None] = Field(
        default_factory=list,
        description="Total value of the transactions.",
    )
    settlement_price: list[float | None] = Field(
        default_factory=list,
        description="Settlement price on that date.",
    )

    @field_validator("expiration", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):
        """Return the datetime object from the date string"""
        return [datetime.strptime(d, "%Y-%m-%d") for d in v]


class TmxOptionsChainsFetcher(
    Fetcher[
        TmxOptionsChainsQueryParams,
        TmxOptionsChainsData,
    ]
):
    """TMX Options Chains Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> TmxOptionsChainsQueryParams:
        """Transform the query."""
        return TmxOptionsChainsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: TmxOptionsChainsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Return the data."""
        # pylint: disable=import-outside-toplevel
        from openbb_tmx.models.equity_quote import TmxEquityQuoteFetcher
        from openbb_tmx.utils.helpers import download_eod_chains, get_current_options
        from pandas import DataFrame

        results: dict = {}
        chains = DataFrame()
        if query.date is not None:
            chains = await download_eod_chains(
                symbol=query.symbol, date=query.date, use_cache=query.use_cache
            )
        else:
            chains = await get_current_options(query.symbol, use_cache=query.use_cache)
            underlying_quote = await TmxEquityQuoteFetcher.fetch_data(
                {"symbol": query.symbol}, credentials
            )
            underlying_price = underlying_quote[0].last_price  # type: ignore
            if underlying_price and not chains.empty:
                chains["underlying_price"] = underlying_price
                chains["underlying_symbol"] = query.symbol + ":CA"

        if not chains.empty:
            results = chains.to_dict(orient="list")

        return results

    @staticmethod
    def transform_data(
        query: TmxOptionsChainsQueryParams,
        data: dict,
        **kwargs: Any,
    ) -> TmxOptionsChainsData:
        """Transform the data and validate the model."""
        return TmxOptionsChainsData.model_validate(data)

```



---

## High-Level Overview

This is a **python** file named `options_chains.py`.

**Python Module**

- **Classes** (3): TmxOptionsChainsQueryParams, TmxOptionsChainsData, TmxOptionsChainsFetcher
- **Functions** (4): date_validate, transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TmxOptionsChainsQueryParams`**(OptionsChainsQueryParams)
- **`TmxOptionsChainsData`**(OptionsChainsData)
- **`TmxOptionsChainsFetcher`**(
    Fetcher[
        TmxOptionsChainsQueryParams,
        TmxOptionsChainsData,
    ]
)

#### Functions

- **`date_validate(cls, v)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `DataFrame`
- `Fetcher`
- `Field`
- `TmxEquityQuoteFetcher`
- `datetime`
- `download_eod_chains`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.options_chains`
- `openbb_core.provider.utils.descriptions`
- `openbb_tmx.models.equity_quote`
- `openbb_tmx.utils.helpers`
- `pandas`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:53.106395Z
**Generator**: World's Best Repo Book Generator v1.0
