# File Documentation: equity_peers.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/equity_peers.py`
- **Size**: 2,199 bytes
- **Lines**: 77
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP Equity Peers Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_peers import (
    EquityPeersData,
    EquityPeersQueryParams,
)
from pydantic import Field


class FMPEquityPeersQueryParams(EquityPeersQueryParams):
    """FMP Equity Peers Query.

    Source: https://site.financialmodelingprep.com/developer/docs#peers
    """


class FMPEquityPeersData(EquityPeersData):
    """FMP Equity Peers Data."""

    __alias_dict__ = {"name": "companyName", "market_cap": "mktCap"}

    name: str = Field(
        description="The name of the company.",
    )
    price: float | None = Field(
        default=None,
        description="The current stock price of the company.",
    )
    market_cap: int | None = Field(
        default=None,
        description="The market capitalization of the company.",
    )


class FMPEquityPeersFetcher(
    Fetcher[
        FMPEquityPeersQueryParams,
        list[FMPEquityPeersData],
    ]
):
    """FMP Equity Peers Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPEquityPeersQueryParams:
        """Transform the query params."""
        return FMPEquityPeersQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPEquityPeersQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        url = f"https://financialmodelingprep.com/stable/stock-peers?symbol={query.symbol}&apikey={api_key}"

        return await get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPEquityPeersQueryParams, data: list, **kwargs: Any
    ) -> list[FMPEquityPeersData]:
        """Return the transformed data."""
        return [
            FMPEquityPeersData.model_validate(d)
            for d in sorted(data, key=lambda x: x["mktCap"], reverse=True)
        ]

```



---

## High-Level Overview

This is a **python** file named `equity_peers.py`.

**Python Module**

- **Classes** (3): FMPEquityPeersQueryParams, FMPEquityPeersData, FMPEquityPeersFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPEquityPeersQueryParams`**(EquityPeersQueryParams)
- **`FMPEquityPeersData`**(EquityPeersData)
- **`FMPEquityPeersFetcher`**(
    Fetcher[
        FMPEquityPeersQueryParams,
        list[FMPEquityPeersData],
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
- `get_data_many`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_peers`
- `openbb_fmp.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.618676Z
**Generator**: World's Best Repo Book Generator v1.0
