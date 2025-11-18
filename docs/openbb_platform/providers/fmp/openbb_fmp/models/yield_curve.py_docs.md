# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/yield_curve.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/yield_curve.py`
- **Size**: 4,464 characters, 133 lines
- **Words**: 351
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Yield Curve Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.yield_curve import (
    YieldCurveData,
    YieldCurveQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError

maturity_dict = {
    "month1": "month_1",
    "month2": "month_2",
    "month3": "month_3",
    "month6": "month_6",
    "year1": "year_1",
    "year2": "year_2",
    "year3": "year_3",
    "year5": "year_5",
    "year7": "year_7",
    "year10": "year_10",
    "year20": "year_20",
    "year30": "year_30",
}


class FMPYieldCurveQueryParams(YieldCurveQueryParams):
    """FMP Yield Curve Query.

    Source: https://site.financialmodelingprep.com/developer/docs/treasury-rates-api/
    """

    __json_schema_extra__ = {"date": {"multiple_items_allowed": True}}


class FMPYieldCurveData(YieldCurveData):
    """FMP Yield Curve Data."""


class FMPYieldCurveFetcher(
    Fetcher[
        FMPYieldCurveQueryParams,
        list[FMPYieldCurveData],
    ]
):
    """FMP Yield Curve Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPYieldCurveQueryParams:
        """Transform the query params."""
        transformed_params = params
        if not transformed_params.get("date"):
            transformed_params["date"] = datetime.now().strftime("%Y-%m-%d")
        return FMPYieldCurveQueryParams(**transformed_params)

    @staticmethod
    async def aextract_data(
        query: FMPYieldCurveQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from datetime import timedelta  # noqa
        from openbb_fmp.utils.helpers import get_data_urls

        api_key = credentials.get("fmp_api_key") if credentials else ""

        def generate_url(date):
            """Generate URL for a small window between each date."""
            date = datetime.strptime(date, "%Y-%m-%d")
            from_date = (date - timedelta(days=3)).strftime("%Y-%m-%d")
            to_date = (date + timedelta(days=3)).strftime("%Y-%m-%d")
            url = (
                "https://financialmodelingprep.com/stable/treasury-rates?"
                + f"from={from_date}&to={to_date}&apikey={api_key}"
            )
            return url

        dates = query.date.split(",")  # type: ignore
        urls = [generate_url(date) for date in dates]

        return await get_data_urls(urls, **kwargs)  # type: ignore

    @staticmethod
    def transform_data(
        query: FMPYieldCurveQueryParams, data: list, **kwargs: Any
    ) -> list[FMPYieldCurveData]:
        """Return the transformed data."""
        # pylint: disable=import-outside-toplevel
        from numpy import nan
        from pandas import Categorical, DataFrame, DatetimeIndex

        if not data:
            raise EmptyDataError("The request was returned empty.")
        df = DataFrame(data).set_index("date").sort_index()
        dates = query.date.split(",") if query.date else [df.index.max()]  # type: ignore
        df.index = DatetimeIndex(df.index)
        dates_list = DatetimeIndex(dates)
        df = df.rename(columns=maturity_dict)
        df.columns.name = "maturity"

        # Find the nearest date in the DataFrame to each date in dates_list
        nearest_dates = [df.index.asof(date) for date in dates_list]

        # Filter for only the nearest dates
        df = df[df.index.isin(nearest_dates)]

        df = df.replace({nan: None})

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

        return [FMPYieldCurveData.model_validate(d) for d in records]

```

## High-Level Overview

FMP Yield Curve Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.yield_curve import (
YieldCurveData,
YieldCurveQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError

maturity_dict = {
"month1": "month_1",
"month2": "month_2",
"month3": "month_3",
"month6": "month_6",
"year1": "year_1",

## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPYieldCurveQueryParams`, `FMPYieldCurveData`, `FMPYieldCurveFetcher`

**Functions** (4):
`transform_query`, `aextract_data`, `generate_url`, `transform_data`

**Imports** (18):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.yield_curve`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `the`, `datetime`, `timedelta`, `openbb_fmp.utils.helpers`, `get_data_urls`, `numpy`, `nan`, `pandas`, `Categorical`


## Key Components

**Class `FMPYieldCurveQueryParams`**: FMP Yield Curve Query.

    Source: https://site.financialmodelingprep.com/developer/docs/treasury-rates-api/

**Class `FMPYieldCurveData`**: FMP Yield Curve Data.

**Class `FMPYieldCurveFetcher`**: FMP Yield Curve Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.yield_curve`
- `openbb_core.provider.utils.errors`
- `datetime`
- `openbb_fmp.utils.helpers`
- `numpy`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:39.426893
- Generator: World's Best Repo Book Generator v1.0.0
