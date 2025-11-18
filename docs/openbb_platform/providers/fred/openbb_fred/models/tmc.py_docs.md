# Documentation: openbb_platform/providers/fred/openbb_fred/models/tmc.py

## File Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/tmc.py`
- **Size**: 2,341 characters, 82 lines
- **Words**: 168
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FRED Treasury Constant Maturity Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.tmc import (
    TreasuryConstantMaturityData,
    TreasuryConstantMaturityQueryParams,
)
from pydantic import field_validator

TMC_PARAMETER_TO_FRED_ID = {
    "3m": "T10Y3M",
    "2y": "T10Y2Y",
}


class FREDTreasuryConstantMaturityQueryParams(TreasuryConstantMaturityQueryParams):
    """FRED Treasury Constant Maturity Query."""


class FREDTreasuryConstantMaturityData(TreasuryConstantMaturityData):
    """FRED Treasury Constant Maturity Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDTreasuryConstantMaturityFetcher(
    Fetcher[
        FREDTreasuryConstantMaturityQueryParams,
        list[FREDTreasuryConstantMaturityData],
    ]
):
    """Transform the query, extract and transform the data from the FRED endpoints."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> FREDTreasuryConstantMaturityQueryParams:
        """Transform query."""
        return FREDTreasuryConstantMaturityQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FREDTreasuryConstantMaturityQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any
    ) -> list:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_fred.utils.fred_base import Fred

        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)

        data = fred.get_series(
            series_id=TMC_PARAMETER_TO_FRED_ID[query.maturity],  # type: ignore
            start_date=query.start_date,
            end_date=query.end_date,
            **kwargs,
        )

        return data

    @staticmethod
    def transform_data(
        query: FREDTreasuryConstantMaturityQueryParams, data: list, **kwargs: Any
    ) -> list[FREDTreasuryConstantMaturityData]:
        """Transform data."""
        return [FREDTreasuryConstantMaturityData.model_validate(d) for d in data]

```

## High-Level Overview

FRED Treasury Constant Maturity Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.tmc import (
TreasuryConstantMaturityData,
TreasuryConstantMaturityQueryParams,
)
from pydantic import field_validator

TMC_PARAMETER_TO_FRED_ID = {
"3m": "T10Y3M",
"2y": "T10Y2Y",
}


class FREDTreasuryConstantMaturityQueryParams(TreasuryConstantMaturityQueryParams):

## Detailed Structure

### Python File Structure

**Classes** (3):
`FREDTreasuryConstantMaturityQueryParams`, `FREDTreasuryConstantMaturityData`, `FREDTreasuryConstantMaturityFetcher`

**Functions** (4):
`value_validate`, `transform_query`, `extract_data`, `transform_data`

**Imports** (10):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.tmc`, `pydantic`, `field_validator`, `the`, `openbb_fred.utils.fred_base`, `Fred`


## Key Components

**Class `FREDTreasuryConstantMaturityQueryParams`**: FRED Treasury Constant Maturity Query.

**Class `FREDTreasuryConstantMaturityData`**: FRED Treasury Constant Maturity Data.

**Class `FREDTreasuryConstantMaturityFetcher`**: Transform the query, extract and transform the data from the FRED endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.tmc`
- `pydantic`
- `openbb_fred.utils.fred_base`

## Notes
- Generated: 2025-11-18T07:54:39.722119
- Generator: World's Best Repo Book Generator v1.0.0
