# Documentation: openbb_platform/providers/fred/openbb_fred/models/yield_curve.py

## File Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/yield_curve.py`
- **Size**: 4,230 characters, 124 lines
- **Words**: 323
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FRED Yield Curve Model."""

# pylint: disable=unused-argument

from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.yield_curve import (
    YieldCurveData,
    YieldCurveQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_fred.models.series import FredSeriesFetcher
from openbb_fred.utils.fred_helpers import YIELD_CURVES
from pydantic import Field


class FREDYieldCurveQueryParams(YieldCurveQueryParams):
    """FRED Yield Curve Query."""

    __json_schema_extra__ = {"date": {"multiple_items_allowed": True}}

    yield_curve_type: Literal[
        "nominal",
        "real",
        "breakeven",
        "treasury_minus_fed_funds",
        "corporate_spot",
        "corporate_par",
    ] = Field(
        default="nominal",
        description="Yield curve type."
        + " Nominal and Real Rates are available daily, others are monthly."
        + " The closest date to the requested date will be returned.",
        json_schema_extra={
            "choices": [
                "nominal",
                "real",
                "breakeven",
                "treasury_minus_fed_funds",
                "corporate_spot",
                "corporate_par",
            ]
        },
    )


class FREDYieldCurveData(YieldCurveData):
    """FRED Yield Curve Data."""


class FREDYieldCurveFetcher(
    Fetcher[FREDYieldCurveQueryParams, list[FREDYieldCurveData]]
):
    """Transform the query, extract and transform the data from the FRED endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FREDYieldCurveQueryParams:
        """Transform query."""
        return FREDYieldCurveQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FREDYieldCurveQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any
    ) -> list[dict]:
        """Extract data."""
        api_key = credentials.get("fred_api_key") if credentials else ""
        series_ids = ",".join(list(YIELD_CURVES[query.yield_curve_type]))
        fetcher = FredSeriesFetcher()
        data = await fetcher.fetch_data(
            {"symbol": series_ids}, {"fred_api_key": api_key}
        )
        if not data:
            raise EmptyDataError("The request was returned empty.")
        results = [d.model_dump() for d in data.result]

        return results

    @staticmethod
    def transform_data(
        query: FREDYieldCurveQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FREDYieldCurveData]:
        """Transform data."""
        # pylint: disable=import-outside-toplevel
        from pandas import Categorical, DataFrame, DatetimeIndex

        df = DataFrame(data).set_index("date").sort_index()
        df.index = df.index.astype(str)
        dates = query.date.split(",") if query.date else [df.index.max()]
        df.index = DatetimeIndex(df.index)
        dates_list = DatetimeIndex(dates)
        maturity_dict = YIELD_CURVES[query.yield_curve_type]
        df = df.rename(columns=maturity_dict)
        df.columns.name = "maturity"

        # Find the nearest date in the DataFrame to each date in dates_list
        nearest_dates = [df.index.asof(date) for date in dates_list]

        # Filter for only the nearest dates
        df = df[df.index.isin(nearest_dates)]

        df = df.fillna("N/A").replace("N/A", None)

        # Flatten the DataFrame
        flattened_data = df.reset_index().melt(
            id_vars="date", var_name="maturity", value_name="rate"
        )
        flattened_data = flattened_data.sort_values("date")
        flattened_data["maturity"] = Categorical(
            flattened_data["maturity"],
            categories=list(maturity_dict.values()),
            ordered=True,
        )
        flattened_data["rate"] = flattened_data["rate"].astype(float) / 100
        flattened_data = flattened_data.sort_values(
            by=["date", "maturity"]
        ).reset_index(drop=True)
        flattened_data.loc[:, "date"] = flattened_data["date"].dt.strftime("%Y-%m-%d")
        records = flattened_data.to_dict(orient="records")

        return [FREDYieldCurveData.model_validate(d) for d in records]

```

## High-Level Overview

FRED Yield Curve Model.

# pylint: disable=unused-argument

from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.yield_curve import (
YieldCurveData,
YieldCurveQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_fred.models.series import FredSeriesFetcher
from openbb_fred.utils.fred_helpers import YIELD_CURVES
from pydantic import Field


class FREDYieldCurveQueryParams(YieldCurveQueryParams):
FRED Yield Curve Query.
FRED Yield Curve Data.

## Detailed Structure

### Python File Structure

**Classes** (3):
`FREDYieldCurveQueryParams`, `FREDYieldCurveData`, `FREDYieldCurveFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (16):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.yield_curve`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `openbb_fred.models.series`, `FredSeriesFetcher`, `openbb_fred.utils.fred_helpers`, `YIELD_CURVES`, `pydantic`, `Field`, `the`, `pandas`, `Categorical`


## Key Components

**Class `FREDYieldCurveQueryParams`**: FRED Yield Curve Query.

**Class `FREDYieldCurveData`**: FRED Yield Curve Data.

**Class `FREDYieldCurveFetcher`**: Transform the query, extract and transform the data from the FRED endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.yield_curve`
- `openbb_core.provider.utils.errors`
- `openbb_fred.models.series`
- `openbb_fred.utils.fred_helpers`
- `pydantic`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:39.725498
- Generator: World's Best Repo Book Generator v1.0.0
