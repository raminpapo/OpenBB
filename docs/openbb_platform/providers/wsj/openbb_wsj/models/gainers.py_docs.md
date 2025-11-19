# File Documentation: gainers.py

## Metadata
- **Path**: `openbb_platform/providers/wsj/openbb_wsj/models/gainers.py`
- **Size**: 3,315 bytes
- **Lines**: 111
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""WSJ Asset Performance Gainers Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.etf_performance import (
    ETFPerformanceData,
    ETFPerformanceQueryParams,
)
from pydantic import Field, field_validator


class WSJGainersQueryParams(ETFPerformanceQueryParams):
    """WSJ Asset Performance Gainers Query.

    Source: https://www.wsj.com/market-data/mutualfunds-etfs/etfmovers
    """


class WSJGainersData(ETFPerformanceData):
    """WSJ Asset Performance Gainers Data."""

    __alias_dict__ = {
        "symbol": "ticker",
        "last_price": "lastPrice",
        "percent_change": "percentChange",
        "net_change": "priceChange",
        "date": "timestamp",
    }

    bluegrass_channel: str | None = Field(
        description="Bluegrass channel.", default=None
    )
    country: str = Field(
        description="Country of the entity.",
    )
    mantissa: int = Field(
        description="Mantissa.",
    )
    type: str = Field(
        description="Type of the entity.",
    )
    formatted_price: str = Field(
        description="Formatted price.",
    )
    formatted_volume: str = Field(
        description="Formatted volume.",
    )
    formatted_price_change: str = Field(
        description="Formatted price change.",
    )
    formatted_percent_change: str = Field(
        description="Formatted percent change.",
    )
    url: str = Field(
        description="The source url.",
    )

    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the datetime object from the date string."""
        return datetime.strptime(v[:10], "%Y-%m-%d").date()


class WSJGainersFetcher(Fetcher[WSJGainersQueryParams, list[WSJGainersData]]):
    """Transform the query, extract and transform the data from the WSJ endpoints."""

    # pylint: disable=unused-argument
    @staticmethod
    def transform_query(params: dict[str, Any]) -> WSJGainersQueryParams:
        """Transform query params."""
        return WSJGainersQueryParams(**params)

    @staticmethod
    def extract_data(
        query: WSJGainersQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from WSJ."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import make_request

        url = (
            "https://www.wsj.com/market-data/mutualfunds-etfs/etfmovers?id=%7B%22application"
            "%22%3A%22WSJ%22%2C%22etfMover%22%3A%22leaders%22%2C%22count%22%3A25%7D&type="
            "mdc_etfmovers"
        )
        data = make_request(url).json()

        return data["data"]["instruments"]

    @staticmethod
    def transform_data(
        query: ETFPerformanceQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[WSJGainersData]:
        """Transform data."""
        data = data[: query.limit]
        data = sorted(
            data,
            key=lambda x: (
                x["percentChange"] if query.sort == "asc" else -x["percentChange"]
            ),
        )
        return [WSJGainersData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `gainers.py`.

**Python Module**

- **Classes** (3): WSJGainersQueryParams, WSJGainersData, WSJGainersFetcher
- **Functions** (4): date_validate, transform_query, extract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`WSJGainersQueryParams`**(ETFPerformanceQueryParams)
- **`WSJGainersData`**(ETFPerformanceData)
- **`WSJGainersFetcher`**(Fetcher[WSJGainersQueryParams, list[WSJGainersData]])

#### Functions

- **`date_validate(cls, v)`**

#### Decorators Used

field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Field`
- `datetime`
- `make_request`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.etf_performance`
- `openbb_core.provider.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.114106Z
**Generator**: World's Best Repo Book Generator v1.0
