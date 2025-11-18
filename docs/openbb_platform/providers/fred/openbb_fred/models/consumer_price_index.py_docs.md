# Documentation: openbb_platform/providers/fred/openbb_fred/models/consumer_price_index.py

## File Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/consumer_price_index.py`
- **Size**: 4,809 characters, 136 lines
- **Words**: 399
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FRED Consumer Price Index Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.annotated_result import AnnotatedResult
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.consumer_price_index import (
    ConsumerPriceIndexData,
    ConsumerPriceIndexQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import check_item
from openbb_fred.models.series import FredSeriesFetcher
from openbb_fred.utils.fred_helpers import CPI_COUNTRIES, CpiCountries, all_cpi_options
from pydantic import Field, field_validator


class FREDConsumerPriceIndexQueryParams(ConsumerPriceIndexQueryParams):
    """FRED Consumer Price Index Query."""

    __json_schema_extra__ = {
        "country": {
            "multiple_items_allowed": True,
            "choices": CPI_COUNTRIES,
        },
    }

    country: CpiCountries | str = Field(
        description=QUERY_DESCRIPTIONS.get("country"),
        default="united_states",
    )

    @field_validator("country", mode="before", check_fields=False)
    @classmethod
    def validate_country(cls, c: str):
        """Validate country."""
        result: list = []
        values = c.replace(" ", "_").split(",")
        for v in values:
            check_item(v.lower(), CPI_COUNTRIES)
            result.append(v.lower())
        return ",".join(result)


class FREDConsumerPriceIndexData(ConsumerPriceIndexData):
    """FRED Consumer Price Index Data."""


class FREDConsumerPriceIndexFetcher(
    Fetcher[FREDConsumerPriceIndexQueryParams, list[FREDConsumerPriceIndexData]]
):
    """Transform the query, extract and transform the data from the FRED endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FREDConsumerPriceIndexQueryParams:
        """Transform query."""
        return FREDConsumerPriceIndexQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FREDConsumerPriceIndexQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Extract data."""
        frequency = "quarterly" if query.frequency == "quarter" else query.frequency

        # Convert the params to series IDs.
        all_options = all_cpi_options(query.harmonized)
        units_dict = {
            "period": "growth_previous",
            "yoy": "growth_same",
            "index": "index_2015",
        }
        units = (
            "growth_same"
            if query.transform == "period" and frequency == "annual"
            else units_dict.get(query.transform)
        )
        step_1 = [x for x in all_options if x["country"] in query.country]
        step_2 = [x for x in step_1 if x["units"] == units]
        step_3 = [x for x in step_2 if x["frequency"] == frequency]
        ids = [item["series_id"] for item in step_3]
        country_map = {item["series_id"]: item["country"] for item in step_3}
        item_query = dict(
            symbol=",".join(ids),
            start_date=query.start_date,
            end_date=query.end_date,
        )
        results: dict = {}
        temp = await FredSeriesFetcher.fetch_data(item_query, credentials)
        result = [d.model_dump() for d in temp.result]
        results["metadata"] = {country_map.get(k): v for k, v in temp.metadata.items()}
        results["data"] = [
            {country_map.get(k, k): v for k, v in d.items()} for d in result
        ]

        return results

    @staticmethod
    def transform_data(
        query: FREDConsumerPriceIndexQueryParams,
        data: dict,
        **kwargs: Any,
    ) -> AnnotatedResult[list[FREDConsumerPriceIndexData]]:
        """Transform data and validate the model."""
        # pylint: disable=import-outside-toplevel
        from pandas import DataFrame

        df = DataFrame.from_records(data["data"])
        if df.empty:
            raise EmptyDataError(
                "No data found for the given query. Try adjusting the parameters."
            )
        # Flatten the data as a pivot table.
        df = (
            df.melt(id_vars="date", var_name="country", value_name="value")
            .query("value.notnull()")
            .set_index(["date", "country"])
            .sort_index()
            .reset_index()
        )
        # Normalize the percent values.
        if query.transform in ("period", "yoy"):
            df["value"] = df["value"] / 100

        records = df.to_dict(orient="records")
        metadata = data.get("metadata", {})
        return AnnotatedResult(
            result=[FREDConsumerPriceIndexData.model_validate(r) for r in records],
            metadata=metadata,
        )

```

## High-Level Overview

FRED Consumer Price Index Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.annotated_result import AnnotatedResult
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.consumer_price_index import (
ConsumerPriceIndexData,
ConsumerPriceIndexQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import check_item
from openbb_fred.models.series import FredSeriesFetcher
from openbb_fred.utils.fred_helpers import CPI_COUNTRIES, CpiCountries, all_cpi_options
from pydantic import Field, field_validator



## Detailed Structure

### Python File Structure

**Classes** (3):
`FREDConsumerPriceIndexQueryParams`, `FREDConsumerPriceIndexData`, `FREDConsumerPriceIndexFetcher`

**Functions** (4):
`validate_country`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (22):
`typing`, `Any`, `openbb_core.provider.abstract.annotated_result`, `AnnotatedResult`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.consumer_price_index`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `openbb_core.provider.utils.helpers`, `check_item`, `openbb_fred.models.series`, `FredSeriesFetcher`, `openbb_fred.utils.fred_helpers`, `CPI_COUNTRIES`, `pydantic`, `Field`, `the`


## Key Components

**Class `FREDConsumerPriceIndexQueryParams`**: FRED Consumer Price Index Query.

**Class `FREDConsumerPriceIndexData`**: FRED Consumer Price Index Data.

**Class `FREDConsumerPriceIndexFetcher`**: Transform the query, extract and transform the data from the FRED endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.annotated_result`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.consumer_price_index`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`
- `openbb_fred.models.series`
- `openbb_fred.utils.fred_helpers`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:39.665606
- Generator: World's Best Repo Book Generator v1.0.0
