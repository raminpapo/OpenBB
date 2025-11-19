# File Documentation: tbffr.py

## Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/tbffr.py`
- **Size**: 2,224 bytes
- **Lines**: 80
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FRED Selected Treasury Bill Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.tbffr import (
    SelectedTreasuryBillData,
    SelectedTreasuryBillQueryParams,
)
from pydantic import field_validator

TBFFR_PARAMETER_TO_FRED_ID = {
    "3m": "TB3SMFFM",
    "6m": "TB6SMFFM",
}


class FREDSelectedTreasuryBillQueryParams(SelectedTreasuryBillQueryParams):
    """FRED Selected Treasury Bill Query."""


class FREDSelectedTreasuryBillData(SelectedTreasuryBillData):
    """FRED Selected Treasury Bill Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDSelectedTreasuryBillFetcher(
    Fetcher[
        FREDSelectedTreasuryBillQueryParams,
        list[FREDSelectedTreasuryBillData],
    ]
):
    """FRED Selected Treasury Bill Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FREDSelectedTreasuryBillQueryParams:
        """Transform query."""
        return FREDSelectedTreasuryBillQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FREDSelectedTreasuryBillQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any
    ) -> list:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_fred.utils.fred_base import Fred

        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)

        data = fred.get_series(
            series_id=TBFFR_PARAMETER_TO_FRED_ID[query.maturity],  # type: ignore
            start_date=query.start_date,
            end_date=query.end_date,
            **kwargs,
        )

        return data

    @staticmethod
    def transform_data(
        query: FREDSelectedTreasuryBillQueryParams, data: list, **kwargs: Any
    ) -> list[FREDSelectedTreasuryBillData]:
        """Transform data."""
        return [FREDSelectedTreasuryBillData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `tbffr.py`.

**Python Module**

- **Classes** (3): FREDSelectedTreasuryBillQueryParams, FREDSelectedTreasuryBillData, FREDSelectedTreasuryBillFetcher
- **Functions** (4): value_validate, transform_query, extract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FREDSelectedTreasuryBillQueryParams`**(SelectedTreasuryBillQueryParams)
- **`FREDSelectedTreasuryBillData`**(SelectedTreasuryBillData)
- **`FREDSelectedTreasuryBillFetcher`**(
    Fetcher[
        FREDSelectedTreasuryBillQueryParams,
        list[FREDSelectedTreasuryBillData],
    ]
)

#### Functions

- **`value_validate(cls, v)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Fred`
- `field_validator`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.tbffr`
- `openbb_fred.utils.fred_base`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.014732Z
**Generator**: World's Best Repo Book Generator v1.0
