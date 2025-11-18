# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/equity_losers.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/equity_losers.py`
- **Size**: 2,269 characters, 80 lines
- **Words**: 178
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Top Losers Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_performance import (
    EquityPerformanceData,
    EquityPerformanceQueryParams,
)
from pydantic import Field, field_validator


class FMPLosersQueryParams(EquityPerformanceQueryParams):
    """FMP Losers Query.

    Source: https://site.financialmodelingprep.com/developer/docs#biggest-losers
    """


class FMPLosersData(EquityPerformanceData):
    """FMP Losers Data."""

    __alias_dict__ = {
        "percent_change": "changesPercentage",
    }

    exchange: str = Field(
        description="Stock exchange where the security is listed.",
    )

    @field_validator("percent_change", mode="before", check_fields=False)
    @classmethod
    def _normalize_percent(cls, v):
        """Normalize percent change by removing % sign and converting to float."""
        return v / 100 if v else None


class FMPLosersFetcher(Fetcher[FMPLosersQueryParams, list[FMPLosersData]]):
    """FMP Losers Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPLosersQueryParams:
        """Transform query params."""
        return FMPLosersQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPLosersQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Get the raw data from the FMP API."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        url = (
            f"https://financialmodelingprep.com/stable/biggest-losers?apikey={api_key}"
        )

        return await get_data_many(url)

    @staticmethod
    def transform_data(
        query: EquityPerformanceQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[FMPLosersData]:
        """Transform data."""
        return [
            FMPLosersData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: x["changesPercentage"],
                reverse=query.sort == "desc",
            )
        ]

```

## High-Level Overview

FMP Top Losers Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_performance import (
EquityPerformanceData,
EquityPerformanceQueryParams,
)
from pydantic import Field, field_validator


class FMPLosersQueryParams(EquityPerformanceQueryParams):
FMP Losers Query.



class FMPLosersData(EquityPerformanceData):

## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPLosersQueryParams`, `FMPLosersData`, `FMPLosersFetcher`

**Functions** (4):
`_normalize_percent`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (10):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.equity_performance`, `pydantic`, `Field`, `the`, `openbb_fmp.utils.helpers`, `get_data_many`


## Key Components

**Class `FMPLosersQueryParams`**: FMP Losers Query.

    Source: https://site.financialmodelingprep.com/developer/docs#biggest-losers

**Class `FMPLosersData`**: FMP Losers Data.

**Class `FMPLosersFetcher`**: FMP Losers Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.equity_performance`
- `pydantic`
- `openbb_fmp.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:39.349978
- Generator: World's Best Repo Book Generator v1.0.0
