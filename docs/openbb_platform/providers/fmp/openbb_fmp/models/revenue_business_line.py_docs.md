# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/revenue_business_line.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/revenue_business_line.py`
- **Size**: 3,618 characters, 100 lines
- **Words**: 255
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Revenue By Business Line Model."""

# pylint: disable=unused-argument

from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.revenue_business_line import (
    RevenueBusinessLineData,
    RevenueBusinessLineQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FMPRevenueBusinessLineQueryParams(RevenueBusinessLineQueryParams):
    """FMP Revenue By Business Line Query.

    Source: https://site.financialmodelingprep.com/developer/docs#revenue-product-segmentation
    """

    period: Literal["quarter", "annual"] = Field(
        default="annual", description=QUERY_DESCRIPTIONS.get("period", "")
    )


class FMPRevenueBusinessLineData(RevenueBusinessLineData):
    """FMP Revenue By Business Line Data."""


class FMPRevenueBusinessLineFetcher(
    Fetcher[
        FMPRevenueBusinessLineQueryParams,
        list[FMPRevenueBusinessLineData],
    ]
):
    """FMP Revenue By Business Line Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPRevenueBusinessLineQueryParams:
        """Transform the query params."""
        return FMPRevenueBusinessLineQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPRevenueBusinessLineQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        base_url = (
            "https://financialmodelingprep.com/stable/revenue-product-segmentation?"
        )
        url = f"{base_url}symbol={query.symbol}&period={query.period}&structure=flat&apikey={api_key}"
        return await get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPRevenueBusinessLineQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[FMPRevenueBusinessLineData]:
        """Return the transformed data."""
        if not data:
            raise EmptyDataError("The request was returned empty.")

        results: list = []
        # We need to flatten the data.
        for item in data:
            period_ending = item.get("date")
            fiscal_year = item.get("fiscalYear")
            fiscal_period = item.get("period")
            segment = item.get("data", {})

            for business_line, revenue_value in segment.items():
                if revenue_value is not None:
                    revenue = int(revenue_value) if revenue_value is not None else None
                    if revenue is not None:
                        results.append(
                            FMPRevenueBusinessLineData.model_validate(
                                {
                                    "period_ending": period_ending,
                                    "fiscal_year": fiscal_year,
                                    "fiscal_period": fiscal_period,
                                    "business_line": business_line.strip(),
                                    "revenue": revenue,
                                }
                            )
                        )

        if not results:
            raise EmptyDataError("Unknown error while transforming the data.")

        return sorted(results, key=lambda x: (x.period_ending or "", x.revenue or 0))

```

## High-Level Overview

FMP Revenue By Business Line Model.

# pylint: disable=unused-argument

from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.revenue_business_line import (
RevenueBusinessLineData,
RevenueBusinessLineQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FMPRevenueBusinessLineQueryParams(RevenueBusinessLineQueryParams):
FMP Revenue By Business Line Query.



## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPRevenueBusinessLineQueryParams`, `FMPRevenueBusinessLineData`, `FMPRevenueBusinessLineFetcher`

**Functions** (3):
`transform_query`, `aextract_data`, `transform_data`

**Imports** (14):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.revenue_business_line`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `the`, `openbb_fmp.utils.helpers`, `get_data_many`


## Key Components

**Class `FMPRevenueBusinessLineQueryParams`**: FMP Revenue By Business Line Query.

    Source: https://site.financialmodelingprep.com/developer/docs#revenue-product-segmentation

**Class `FMPRevenueBusinessLineData`**: FMP Revenue By Business Line Data.

**Class `FMPRevenueBusinessLineFetcher`**: FMP Revenue By Business Line Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.revenue_business_line`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `openbb_fmp.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:39.415633
- Generator: World's Best Repo Book Generator v1.0.0
