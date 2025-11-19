# File Documentation: available_indices.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/available_indices.py`
- **Size**: 2,111 bytes
- **Lines**: 69
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Yahoo Finance Available Indices Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.available_indices import (
    AvailableIndicesData,
    AvailableIndicesQueryParams,
)
from openbb_yfinance.utils.references import INDICES
from pydantic import Field


class YFinanceAvailableIndicesQueryParams(AvailableIndicesQueryParams):
    """Yahoo Finance Available Indices Query.

    Source: https://finance.yahoo.com/
    """


class YFinanceAvailableIndicesData(AvailableIndicesData):
    """Yahoo Finance Available Indices Data."""

    __alias_dict__ = {
        "symbol": "ticker",
    }

    code: str = Field(
        description="ID code for keying the index in the OpenBB Terminal."
    )
    symbol: str = Field(description="Symbol for the index.")


class YFinanceAvailableIndicesFetcher(
    Fetcher[
        YFinanceAvailableIndicesQueryParams,
        list[YFinanceAvailableIndicesData],
    ]
):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFinanceAvailableIndicesQueryParams:
        """Transform the query params."""
        return YFinanceAvailableIndicesQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFinanceAvailableIndicesQueryParams,  # pylint disable=unused-argument
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract the data."""
        from pandas import DataFrame  # pylint: disable=import-outside-toplevel

        indices = DataFrame(INDICES).transpose().reset_index()
        indices.columns = ["code", "name", "ticker"]

        return indices.to_dict("records")

    @staticmethod
    def transform_data(
        query: YFinanceAvailableIndicesQueryParams, data: list[dict], **kwargs: Any
    ) -> list[YFinanceAvailableIndicesData]:
        """Return the transformed data."""
        return [YFinanceAvailableIndicesData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `available_indices.py`.

**Python Module**

- **Classes** (3): YFinanceAvailableIndicesQueryParams, YFinanceAvailableIndicesData, YFinanceAvailableIndicesFetcher
- **Functions** (3): transform_query, extract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFinanceAvailableIndicesQueryParams`**(AvailableIndicesQueryParams)
- **`YFinanceAvailableIndicesData`**(AvailableIndicesData)
- **`YFinanceAvailableIndicesFetcher`**(
    Fetcher[
        YFinanceAvailableIndicesQueryParams,
        list[YFinanceAvailableIndicesData],
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
- `Fetcher`
- `Field`
- `INDICES`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.available_indices`
- `openbb_yfinance.utils.references`
- `pandas`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.155869Z
**Generator**: World's Best Repo Book Generator v1.0
