# File Documentation: short_volume.py

## Metadata
- **Path**: `openbb_platform/providers/stockgrid/openbb_stockgrid/models/short_volume.py`
- **Size**: 2,391 bytes
- **Lines**: 74
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Stockgrid Short Volume Model."""

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.short_volume import (
    ShortVolumeData,
    ShortVolumeQueryParams,
)
from pydantic import Field, field_validator


class StockgridShortVolumeQueryParams(ShortVolumeQueryParams):
    """Stockgrid Short Volume Query.

    Source: https://www.stockgrid.io/
    """


class StockgridShortVolumeData(ShortVolumeData):
    """Stockgrid Short Volume Data."""

    __alias_dict__ = {"short_volume_percent": "short_volume%", "symbol": "ticker"}

    close: float | None = Field(
        default=None, description="Closing price of the stock on the date."
    )

    short_volume_percent: float | None = Field(
        default=None,
        description="Percentage of the total volume that was short volume.",
    )

    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the datetime object from the date string."""
        return datetime.strptime(v, "%Y-%m-%d").date()


class StockgridShortVolumeFetcher(
    Fetcher[StockgridShortVolumeQueryParams, list[StockgridShortVolumeData]]
):
    """Transform the query, extract and transform the data from the Stockgrid endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> StockgridShortVolumeQueryParams:
        """Transform query params."""
        return StockgridShortVolumeQueryParams(**params)

    # pylint: disable=unused-argument
    @staticmethod
    def extract_data(
        query: StockgridShortVolumeQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Get data from Stockgrid."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import make_request

        url = f"https://www.stockgrid.io/get_dark_pool_individual_data?ticker={query.symbol}"
        data = make_request(url).json()
        return data["individual_short_volume_table"]["data"]

    @staticmethod
    def transform_data(
        query: ShortVolumeQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[StockgridShortVolumeData]:
        """Transform data."""
        return [StockgridShortVolumeData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `short_volume.py`.

**Python Module**

- **Classes** (3): StockgridShortVolumeQueryParams, StockgridShortVolumeData, StockgridShortVolumeFetcher
- **Functions** (4): date_validate, transform_query, extract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`StockgridShortVolumeQueryParams`**(ShortVolumeQueryParams)
- **`StockgridShortVolumeData`**(ShortVolumeData)
- **`StockgridShortVolumeFetcher`**(
    Fetcher[StockgridShortVolumeQueryParams, list[StockgridShortVolumeData]]
)

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
- `openbb_core.provider.standard_models.short_volume`
- `openbb_core.provider.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:52.972276Z
**Generator**: World's Best Repo Book Generator v1.0
