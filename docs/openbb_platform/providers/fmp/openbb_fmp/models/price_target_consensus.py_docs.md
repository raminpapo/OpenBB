# File Documentation: price_target_consensus.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/price_target_consensus.py`
- **Size**: 3,152 bytes
- **Lines**: 97
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP Price Target Consensus Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.price_target_consensus import (
    PriceTargetConsensusData,
    PriceTargetConsensusQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import field_validator


class FMPPriceTargetConsensusQueryParams(PriceTargetConsensusQueryParams):
    """FMP Price Target Consensus Query.

    Source: https://site.financialmodelingprep.com/developer/docs#price-target-consensus
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def check_symbol(cls, value):
        """Check the symbol."""
        if not value:
            raise OpenBBError("Symbol is a required field for FMP.")
        return value


class FMPPriceTargetConsensusData(PriceTargetConsensusData):
    """FMP Price Target Consensus Data."""


class FMPPriceTargetConsensusFetcher(
    Fetcher[
        FMPPriceTargetConsensusQueryParams,
        list[FMPPriceTargetConsensusData],
    ]
):
    """FMP Price Target Consensus Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPPriceTargetConsensusQueryParams:
        """Transform the query params."""
        return FMPPriceTargetConsensusQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPPriceTargetConsensusQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        import warnings
        from openbb_fmp.utils.helpers import get_data_urls

        api_key = credentials.get("fmp_api_key") if credentials else ""

        symbols = query.symbol.split(",")  # type: ignore
        results: list[dict] = []

        async def get_one(symbol):
            """Get data for one symbol."""
            url = f"https://financialmodelingprep.com/stable/price-target-consensus?symbol={symbol}&apikey={api_key}"
            result = await get_data_urls([url], **kwargs)

            if not result or len(result) == 0:
                warnings.warn(f"Symbol Error: No data found for {symbol}")

            if result:
                results.extend(result)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data returned for the given symbols.")

        return sorted(
            results,
            key=(lambda item: (symbols.index(item.get("symbol", len(symbols))))),
        )

    @staticmethod
    def transform_data(
        query: FMPPriceTargetConsensusQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[FMPPriceTargetConsensusData]:
        """Return the transformed data."""
        return [FMPPriceTargetConsensusData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `price_target_consensus.py`.

**Python Module**

- **Classes** (3): FMPPriceTargetConsensusQueryParams, FMPPriceTargetConsensusData, FMPPriceTargetConsensusFetcher
- **Functions** (5): check_symbol, transform_query, aextract_data, get_one, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPPriceTargetConsensusQueryParams`**(PriceTargetConsensusQueryParams)
- **`FMPPriceTargetConsensusData`**(PriceTargetConsensusData)
- **`FMPPriceTargetConsensusFetcher`**(
    Fetcher[
        FMPPriceTargetConsensusQueryParams,
        list[FMPPriceTargetConsensusData],
    ]
)

#### Functions

- **`check_symbol(cls, value)`**
- **`get_one(symbol)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `EmptyDataError`
- `Fetcher`
- `OpenBBError`
- `asyncio`
- `field_validator`
- `get_data_urls`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.price_target_consensus`
- `openbb_core.provider.utils.errors`
- `openbb_fmp.utils.helpers`
- `pydantic`
- `typing`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.686206Z
**Generator**: World's Best Repo Book Generator v1.0
