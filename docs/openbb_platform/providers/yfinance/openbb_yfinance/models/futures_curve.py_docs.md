# File Documentation: futures_curve.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/futures_curve.py`
- **Size**: 1,963 bytes
- **Lines**: 70
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Yahoo Finance Futures Curve Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.futures_curve import (
    FuturesCurveData,
    FuturesCurveQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError


class YFinanceFuturesCurveQueryParams(FuturesCurveQueryParams):
    """Yahoo Finance Futures Curve Query.

    Source: https://finance.yahoo.com/
    """

    __json_schema_extra__ = {
        "date": {"multiple_items_allowed": True},
    }


class YFinanceFuturesCurveData(FuturesCurveData):
    """Yahoo Finance Futures Curve Data."""


class YFinanceFuturesCurveFetcher(
    Fetcher[
        YFinanceFuturesCurveQueryParams,
        list[YFinanceFuturesCurveData],
    ]
):
    """YFiannce Futures Curve Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFinanceFuturesCurveQueryParams:
        """Transform the query."""
        return YFinanceFuturesCurveQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFinanceFuturesCurveQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract the data from Yahoo."""
        # pylint: disable=import-outside-toplevel
        from openbb_yfinance.utils.helpers import get_futures_curve

        # TODO: Find a better way to do this.
        data = await get_futures_curve(query.symbol, query.date)  # type: ignore
        data = data.to_dict(orient="records")

        if not data:
            raise EmptyDataError()

        return data

    @staticmethod
    def transform_data(
        query: YFinanceFuturesCurveQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFinanceFuturesCurveData]:
        """Transform the data to the standard format."""
        return [YFinanceFuturesCurveData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `futures_curve.py`.

**Python Module**

- **Classes** (3): YFinanceFuturesCurveQueryParams, YFinanceFuturesCurveData, YFinanceFuturesCurveFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFinanceFuturesCurveQueryParams`**(FuturesCurveQueryParams)
- **`YFinanceFuturesCurveData`**(FuturesCurveData)
- **`YFinanceFuturesCurveFetcher`**(
    Fetcher[
        YFinanceFuturesCurveQueryParams,
        list[YFinanceFuturesCurveData],
    ]
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
- `get_futures_curve`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.futures_curve`
- `openbb_core.provider.utils.errors`
- `openbb_yfinance.utils.helpers`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.177145Z
**Generator**: World's Best Repo Book Generator v1.0
