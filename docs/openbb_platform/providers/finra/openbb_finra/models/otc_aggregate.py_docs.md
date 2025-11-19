# File Documentation: otc_aggregate.py

## Metadata
- **Path**: `openbb_platform/providers/finra/openbb_finra/models/otc_aggregate.py`
- **Size**: 2,113 bytes
- **Lines**: 65
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FINRA OTC Aggregate Model."""

from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.otc_aggregate import (
    OTCAggregateData,
    OTCAggregateQueryParams,
)
from pydantic import Field


class FinraOTCAggregateQueryParams(OTCAggregateQueryParams):
    """FINRA OTC Aggregate Query."""

    tier: Literal["T1", "T2", "OTCE"] = Field(
        default="T1",
        description=""""T1 - Securities included in the S&P 500, Russell 1000 and selected exchange-traded products;
        T2 - All other NMS stocks; OTC - Over-the-Counter equity securities""",
    )
    is_ats: bool = Field(
        default=True, description="ATS data if true, NON-ATS otherwise"
    )


class FinraOTCAggregateData(OTCAggregateData):
    """FINRA OTC Aggregate Data."""

    __alias_dict__ = {
        "share_quantity": "totalWeeklyShareQuantity",
        "trade_quantity": "totalWeeklyTradeCount",
        "update_date": "lastUpdateDate",
    }


class FinraOTCAggregateFetcher(
    Fetcher[FinraOTCAggregateQueryParams, list[FinraOTCAggregateData]]
):
    """Transform the query, extract and transform the data from the FINRA endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FinraOTCAggregateQueryParams:
        """Transform query params."""
        return FinraOTCAggregateQueryParams(**params)

    # pylint: disable=unused-argument
    @staticmethod
    def extract_data(
        query: FinraOTCAggregateQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract the data from the FINRA endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_finra.utils.helpers import get_full_data

        return get_full_data(query.symbol, query.tier, query.is_ats)

    @staticmethod
    def transform_data(
        query: FinraOTCAggregateQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FinraOTCAggregateData]:
        """Transform the data."""
        return [FinraOTCAggregateData.model_validate(d) for d in data if d]

```



---

## High-Level Overview

This is a **python** file named `otc_aggregate.py`.

**Python Module**

- **Classes** (3): FinraOTCAggregateQueryParams, FinraOTCAggregateData, FinraOTCAggregateFetcher
- **Functions** (3): transform_query, extract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FinraOTCAggregateQueryParams`**(OTCAggregateQueryParams)
- **`FinraOTCAggregateData`**(OTCAggregateData)
- **`FinraOTCAggregateFetcher`**(
    Fetcher[FinraOTCAggregateQueryParams, list[FinraOTCAggregateData]]
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
- `get_full_data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.otc_aggregate`
- `openbb_finra.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:49.789429Z
**Generator**: World's Best Repo Book Generator v1.0
