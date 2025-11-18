# Documentation: openbb_platform/providers/fred/openbb_fred/models/ffrmc.py

## File Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/ffrmc.py`
- **Size**: 2,568 characters, 91 lines
- **Words**: 175
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FRED Selected Treasury Constant Maturity Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.ffrmc import (
    SelectedTreasuryConstantMaturityData,
    SelectedTreasuryConstantMaturityQueryParams,
)
from pydantic import field_validator

FFRMC_PARAMETER_TO_FRED_ID = {
    "10y": "T10YFF",
    "5y": "T5YFF",
    "1y": "T1YFF",
    "6m": "T6MFF",
    "3m": "T3MFF",
}


class FREDSelectedTreasuryConstantMaturityQueryParams(
    SelectedTreasuryConstantMaturityQueryParams
):
    """FRED Selected Treasury Constant Maturity Query."""


class FREDSelectedTreasuryConstantMaturityData(SelectedTreasuryConstantMaturityData):
    """FRED Selected Treasury Constant Maturity Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDSelectedTreasuryConstantMaturityFetcher(
    Fetcher[
        FREDSelectedTreasuryConstantMaturityQueryParams,
        list[FREDSelectedTreasuryConstantMaturityData],
    ]
):
    """FRED Selected Treasury Constant Maturity Fetcher."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> FREDSelectedTreasuryConstantMaturityQueryParams:
        """Transform query."""
        return FREDSelectedTreasuryConstantMaturityQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FREDSelectedTreasuryConstantMaturityQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any
    ) -> list:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_fred.utils.fred_base import Fred

        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)

        data = fred.get_series(
            series_id=FFRMC_PARAMETER_TO_FRED_ID[query.maturity],  # type: ignore
            start_date=query.start_date,
            end_date=query.end_date,
            **kwargs,
        )

        return data

    @staticmethod
    def transform_data(
        query: FREDSelectedTreasuryConstantMaturityQueryParams,
        data: list,
        **kwargs: Any
    ) -> list[FREDSelectedTreasuryConstantMaturityData]:
        """Transform data."""
        return [
            FREDSelectedTreasuryConstantMaturityData.model_validate(d) for d in data
        ]

```

## High-Level Overview

FRED Selected Treasury Constant Maturity Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.ffrmc import (
SelectedTreasuryConstantMaturityData,
SelectedTreasuryConstantMaturityQueryParams,
)
from pydantic import field_validator

FFRMC_PARAMETER_TO_FRED_ID = {
"10y": "T10YFF",
"5y": "T5YFF",
"1y": "T1YFF",
"6m": "T6MFF",
"3m": "T3MFF",
}

## Detailed Structure

### Python File Structure

**Classes** (3):
`FREDSelectedTreasuryConstantMaturityQueryParams`, `FREDSelectedTreasuryConstantMaturityData`, `FREDSelectedTreasuryConstantMaturityFetcher`

**Functions** (4):
`value_validate`, `transform_query`, `extract_data`, `transform_data`

**Imports** (9):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.ffrmc`, `pydantic`, `field_validator`, `openbb_fred.utils.fred_base`, `Fred`


## Key Components

**Class `FREDSelectedTreasuryConstantMaturityQueryParams`**: FRED Selected Treasury Constant Maturity Query.

**Class `FREDSelectedTreasuryConstantMaturityData`**: FRED Selected Treasury Constant Maturity Data.

**Class `FREDSelectedTreasuryConstantMaturityFetcher`**: FRED Selected Treasury Constant Maturity Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.ffrmc`
- `pydantic`
- `openbb_fred.utils.fred_base`

## Notes
- Generated: 2025-11-18T07:54:39.677145
- Generator: World's Best Repo Book Generator v1.0.0
