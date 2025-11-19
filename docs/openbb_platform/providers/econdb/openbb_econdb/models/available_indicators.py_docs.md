# File Documentation: available_indicators.py

## Metadata
- **Path**: `openbb_platform/providers/econdb/openbb_econdb/models/available_indicators.py`
- **Size**: 3,220 bytes
- **Lines**: 104
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""EconDB Available Indicators."""

# pylint: disable=unused-argument

from datetime import (
    date as dateType,
    datetime,
)
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.available_indicators import (
    AvailableIndicatorsData,
    AvailableIndicesQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class EconDbAvailableIndicatorsQueryParams(AvailableIndicesQueryParams):
    """EconDB Available Indicators Query Parameters."""

    use_cache: bool = Field(
        default=True,
        description="Whether to use cache or not, by default is True"
        + " The cache of indicator symbols will persist for one week.",
    )


class EconDbAvailableIndicatorsData(AvailableIndicatorsData):
    """EconDB Available Indicators Data."""

    __alias_dict__ = {
        "symbol": "short_ticker",
        "country": "entity",
    }
    currency: str | None = Field(
        default=None,
        description="The currency, or unit, the data is based in.",
    )
    scale: str | None = Field(
        default=None,
        description="The scale of the data.",
    )
    multiplier: int | None = Field(
        description="The multiplier of the data to arrive at whole units.",
    )
    transformation: str = Field(
        description="Transformation type.",
    )
    source: str | None = Field(
        default=None,
        description="The original source of the data.",
    )
    first_date: dateType | None = Field(
        default=None,
        description="The first date of the data.",
    )
    last_date: dateType | None = Field(
        default=None,
        description="The last date of the data.",
    )
    last_insert_timestamp: datetime | None = Field(
        default=None,
        description="The time of the last update. Data is typically reported with a lag.",
    )


class EconDbAvailableIndicatorsFetcher(
    Fetcher[EconDbAvailableIndicatorsQueryParams, list[EconDbAvailableIndicatorsData]]
):
    """EconDB Available Indicators Fetcher."""

    require_credentials = False

    @staticmethod
    def transform_query(params: dict[str, Any]) -> EconDbAvailableIndicatorsQueryParams:
        """Transform query."""
        return EconDbAvailableIndicatorsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: EconDbAvailableIndicatorsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_econdb.utils.helpers import download_indicators

        df = await download_indicators(query.use_cache)
        if df.empty:
            raise EmptyDataError("There was an error fetching the data.")
        return df.sort_values(by="last_date", ascending=False).to_dict(orient="records")

    @staticmethod
    def transform_data(
        query: EconDbAvailableIndicatorsQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[EconDbAvailableIndicatorsData]:
        """Transform data."""
        return [EconDbAvailableIndicatorsData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `available_indicators.py`.

**Python Module**

- **Classes** (3): EconDbAvailableIndicatorsQueryParams, EconDbAvailableIndicatorsData, EconDbAvailableIndicatorsFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EconDbAvailableIndicatorsQueryParams`**(AvailableIndicesQueryParams)
- **`EconDbAvailableIndicatorsData`**(AvailableIndicatorsData)
- **`EconDbAvailableIndicatorsFetcher`**(
    Fetcher[EconDbAvailableIndicatorsQueryParams, list[EconDbAvailableIndicatorsData]]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `EmptyDataError`
- `Fetcher`
- `Field`
- `datetime`
- `download_indicators`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.available_indicators`
- `openbb_core.provider.utils.errors`
- `openbb_econdb.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:49.198595Z
**Generator**: World's Best Repo Book Generator v1.0
