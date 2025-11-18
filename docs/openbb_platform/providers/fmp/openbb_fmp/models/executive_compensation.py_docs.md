# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/executive_compensation.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/executive_compensation.py`
- **Size**: 5,128 characters, 155 lines
- **Words**: 385
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Executive Compensation Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.executive_compensation import (
    ExecutiveCompensationData,
    ExecutiveCompensationQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FMPExecutiveCompensationQueryParams(ExecutiveCompensationQueryParams):
    """FMP Executive Compensation Query.

    Source: https://site.financialmodelingprep.com/developer/docs#executive-compensation
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

    year: int = Field(
        default=-1,
        description="Filters results by year, enter 0 for all data available."
        + " Default is the most recent year in the dataset, -1.",
    )


class FMPExecutiveCompensationData(ExecutiveCompensationData):
    """FMP Executive Compensation Data."""

    __alias_dict__ = {
        "company_name": "companyName",
        "industry": "industryTitle",
        "url": "link",
        "executive": "nameAndPosition",
        "report_date": "filingDate",
    }
    accepted_date: datetime | None = Field(
        default=None, description="Date the filing was accepted."
    )
    url: str | None = Field(default=None, description="URL to the filing data.")


class FMPExecutiveCompensationFetcher(
    Fetcher[
        FMPExecutiveCompensationQueryParams,
        list[FMPExecutiveCompensationData],
    ]
):
    """FMP Executive Compensation Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPExecutiveCompensationQueryParams:
        """Transform the query params."""
        return FMPExecutiveCompensationQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPExecutiveCompensationQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        import warnings
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        base_url = "https://financialmodelingprep.com/stable/governance-executive-compensation?"
        symbols = query.symbol.split(",")
        results: list = []

        async def get_one(symbol):
            """Get data for one symbol."""
            url = f"{base_url}symbol={symbol}&apikey={api_key}"
            result = await get_data_many(url, **kwargs)

            if not result:
                warnings.warn(f"Symbol Error: No data found for {symbol}.")

            if result:
                results.extend(result)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data found for given symbols.")

        return results

    @staticmethod
    def transform_data(
        query: FMPExecutiveCompensationQueryParams,
        data: list,
        **kwargs: Any,
    ) -> list[FMPExecutiveCompensationData]:
        """Return the transformed data."""
        # pylint: disable=import-outside-toplevel
        import warnings

        symbols = query.symbol.split(",")
        filtered_results: list[FMPExecutiveCompensationData] = []

        for symbol in symbols:
            symbol_data = [item for item in data if item.get("symbol") == symbol]

            if symbol_data and query.year != 0:
                max_year_for_symbol = (
                    (
                        max(
                            item.get("year", 0)
                            for item in symbol_data
                            if item.get("year")
                        )
                    )
                    if query.year == -1
                    else query.year
                )
                symbol_max_year_data = [
                    item
                    for item in symbol_data
                    if int(item.get("year", 0)) == max_year_for_symbol
                ]
                if not symbol_max_year_data:
                    warnings.warn(
                        f"ValueError: No data found for {symbol} and year {query.year}."
                    )
                    continue

                filtered_results.extend(
                    [
                        FMPExecutiveCompensationData.model_validate(item)
                        for item in symbol_max_year_data
                    ]
                )
            else:
                filtered_results.extend(
                    [
                        FMPExecutiveCompensationData.model_validate(item)
                        for item in sorted(
                            symbol_data, key=lambda x: x.get("year", 0), reverse=True
                        )
                    ]
                )

        if not filtered_results:
            raise EmptyDataError("No data found for given symbols and year.")

        return filtered_results

```

## High-Level Overview

FMP Executive Compensation Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.executive_compensation import (
ExecutiveCompensationData,
ExecutiveCompensationQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FMPExecutiveCompensationQueryParams(ExecutiveCompensationQueryParams):
FMP Executive Compensation Query.



## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPExecutiveCompensationQueryParams`, `FMPExecutiveCompensationData`, `FMPExecutiveCompensationFetcher`

**Functions** (4):
`transform_query`, `aextract_data`, `get_one`, `transform_data`

**Imports** (17):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.executive_compensation`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `the`, `asyncio`, `warnings`, `openbb_fmp.utils.helpers`, `get_data_many`, `warnings`


## Key Components

**Class `FMPExecutiveCompensationQueryParams`**: FMP Executive Compensation Query.

    Source: https://site.financialmodelingprep.com/developer/docs#executive-compensation

**Class `FMPExecutiveCompensationData`**: FMP Executive Compensation Data.

**Class `FMPExecutiveCompensationFetcher`**: FMP Executive Compensation Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.executive_compensation`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `asyncio`
- `warnings`
- `openbb_fmp.utils.helpers`
- `warnings`

## Notes
- Generated: 2025-11-18T07:54:39.372348
- Generator: World's Best Repo Book Generator v1.0.0
