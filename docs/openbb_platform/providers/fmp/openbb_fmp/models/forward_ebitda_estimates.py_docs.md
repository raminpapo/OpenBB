# File Documentation: forward_ebitda_estimates.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/forward_ebitda_estimates.py`
- **Size**: 4,961 bytes
- **Lines**: 148
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP Forward EBITDA Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.forward_ebitda_estimates import (
    ForwardEbitdaEstimatesData,
    ForwardEbitdaEstimatesQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class FMPForwardEbitdaEstimatesQueryParams(ForwardEbitdaEstimatesQueryParams):
    """FMP Forward EBITDA Query.

    Source: https://site.financialmodelingprep.com/developer/docs#financial-estimates
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

    __alias_dict__ = {"fiscal_period": "period"}

    fiscal_period: Literal["annual", "quarter"] = Field(
        default="annual",
        description="The future fiscal period to retrieve estimates for.",
    )
    limit: int | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("limit", "")
        + " Number of historical periods.",
    )
    include_historical: bool = Field(
        default=False,
        description="If True, the data will include all past data and the limit will be ignored.",
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def check_symbol(cls, value):
        """Check the symbol."""
        if not value:
            raise OpenBBError("Symbol is a required field for FMP.")
        return value


class FMPForwardEbitdaEstimatesData(ForwardEbitdaEstimatesData):
    """FMP Forward EBITDA Data."""

    __alias_dict__ = {
        "period_ending": "date",
        "high_estimate": "ebitdaHigh",
        "low_estimate": "ebitdaLow",
        "mean": "ebitdaAvg",
    }


class FMPForwardEbitdaEstimatesFetcher(
    Fetcher[
        FMPForwardEbitdaEstimatesQueryParams,
        list[FMPForwardEbitdaEstimatesData],
    ]
):
    """FMP Forward EBITDA Estimates Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPForwardEbitdaEstimatesQueryParams:
        """Transform the query params."""
        return FMPForwardEbitdaEstimatesQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPForwardEbitdaEstimatesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        import warnings
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        symbols = query.symbol.split(",")  # type: ignore
        results: list[dict] = []
        base_url = "https://financialmodelingprep.com/stable/analyst-estimates?"
        limit = query.limit if query.limit else 1000

        async def get_one(symbol):
            """Get data for one symbol."""
            url = f"{base_url}symbol={symbol}&period={query.fiscal_period}&limit={limit}&apikey={api_key}"
            result = await get_data_many(url, **kwargs)
            if not result or len(result) == 0:
                warnings.warn(f"Symbol Error: No data found for {symbol}")
            if result:
                results.extend(result)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data returned for the given symbols.")

        return results

    @staticmethod
    def transform_data(
        query: FMPForwardEbitdaEstimatesQueryParams, data: list, **kwargs: Any
    ) -> list[FMPForwardEbitdaEstimatesData]:
        """Return the transformed data."""
        symbols = query.symbol.split(",") if query.symbol else []
        cols = [
            "symbol",
            "date",
            "ebitdaAvg",
            "ebitdaHigh",
            "ebitdaLow",
        ]
        year = datetime.now().year
        results: list[FMPForwardEbitdaEstimatesData] = []
        for item in sorted(
            data,
            key=lambda item: (  # type: ignore
                (
                    symbols.index(item.get("symbol")) if item.get("symbol") in symbols else len(symbols),  # type: ignore
                    item.get("date"),
                )
                if symbols
                else item.get("date")
            ),
        ):
            temp: dict[str, Any] = {}
            for col in cols:
                temp[col] = item.get(col)

            if (
                query.include_historical is False
                and datetime.strptime(temp["date"], "%Y-%m-%d").year < year
            ):
                continue
            results.append(FMPForwardEbitdaEstimatesData.model_validate(temp))

        return results

```



---

## High-Level Overview

This is a **python** file named `forward_ebitda_estimates.py`.

**Python Module**

- **Classes** (3): FMPForwardEbitdaEstimatesQueryParams, FMPForwardEbitdaEstimatesData, FMPForwardEbitdaEstimatesFetcher
- **Functions** (5): check_symbol, transform_query, aextract_data, get_one, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPForwardEbitdaEstimatesQueryParams`**(ForwardEbitdaEstimatesQueryParams)
- **`FMPForwardEbitdaEstimatesData`**(ForwardEbitdaEstimatesData)
- **`FMPForwardEbitdaEstimatesFetcher`**(
    Fetcher[
        FMPForwardEbitdaEstimatesQueryParams,
        list[FMPForwardEbitdaEstimatesData],
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
- `Field`
- `OpenBBError`
- `QUERY_DESCRIPTIONS`
- `asyncio`
- `datetime`
- `get_data_many`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.forward_ebitda_estimates`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.errors`
- `openbb_fmp.utils.helpers`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.644874Z
**Generator**: World's Best Repo Book Generator v1.0
