# Documentation: openbb_platform/providers/yfinance/openbb_yfinance/models/futures_curve.py

## File Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/futures_curve.py`
- **Size**: 1,963 characters, 70 lines
- **Words**: 154
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Yahoo Finance Futures Curve Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.futures_curve import (
FuturesCurveData,
FuturesCurveQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError


class YFinanceFuturesCurveQueryParams(FuturesCurveQueryParams):
Yahoo Finance Futures Curve Query.


__json_schema_extra__ = {
"date": {"multiple_items_allowed": True},

## Detailed Structure

### Python File Structure

**Classes** (3):
`YFinanceFuturesCurveQueryParams`, `YFinanceFuturesCurveData`, `YFinanceFuturesCurveFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (10):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.futures_curve`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `Yahoo.`, `openbb_yfinance.utils.helpers`, `get_futures_curve`


## Key Components

**Class `YFinanceFuturesCurveQueryParams`**: Yahoo Finance Futures Curve Query.

    Source: https://finance.yahoo.com/

**Class `YFinanceFuturesCurveData`**: Yahoo Finance Futures Curve Data.

**Class `YFinanceFuturesCurveFetcher`**: YFiannce Futures Curve Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.futures_curve`
- `openbb_core.provider.utils.errors`
- `openbb_yfinance.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:43.574262
- Generator: World's Best Repo Book Generator v1.0.0
