# File Documentation: sofr.py

## Metadata
- **Path**: `openbb_platform/providers/federal_reserve/openbb_federal_reserve/models/sofr.py`
- **Size**: 3,245 bytes
- **Lines**: 109
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Federal Reserve SOFR Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.sofr import (
    SOFRData,
    SOFRQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import field_validator


class FederalReserveSOFRQueryParams(SOFRQueryParams):
    """FederalReserve FED Query."""


class FederalReserveSOFRData(SOFRData):
    """FederalReserve FED Data."""

    __alias_dict__ = {
        "date": "effectiveDate",
        "rate": "percentRate",
        "percentile_1": "percentPercentile1",
        "percentile_25": "percentPercentile25",
        "percentile_75": "percentPercentile75",
        "percentile_99": "percentPercentile99",
        "volume": "volumeInBillions",
    }

    @field_validator(
        "rate",
        "target_range_upper",
        "target_range_lower",
        "percentile_1",
        "percentile_25",
        "percentile_75",
        "percentile_99",
        mode="before",
        check_fields=False,
    )
    @classmethod
    def normalize_percent(cls, v):
        """Normalize percent."""
        if v not in (None, "", "''", "NA"):
            return float(v) / 100 if v != 0 else 0
        return None


class FederalReserveSOFRFetcher(
    Fetcher[
        FederalReserveSOFRQueryParams,
        list[FederalReserveSOFRData],
    ]
):
    """Federal Reserve Federal Funds Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FederalReserveSOFRQueryParams:
        """Transform query."""
        transformed_params = params.copy()
        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = datetime(2018, 4, 2).date()
        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return FederalReserveSOFRQueryParams(**transformed_params)

    @staticmethod
    async def aextract_data(
        query: FederalReserveSOFRQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract the raw data."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import amake_request

        url = (
            "https://markets.newyorkfed.org/api/rates/secured/sofr/search.json?"
            + f"startDate={query.start_date}&endDate={query.end_date}"
        )
        results: list[dict] = []
        response = await amake_request(url, **kwargs)
        results = response.get("refRates")  # type: ignore
        if not results:
            raise EmptyDataError()
        return results

    @staticmethod
    def transform_data(
        query: FederalReserveSOFRQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[FederalReserveSOFRData]:
        """Transform data."""
        results: list[FederalReserveSOFRData] = []
        for d in data.copy():
            _ = d.pop("type", None)
            _ = d.pop("footnoteId", None)
            _ = d.pop("revisionIndicator", None)
            results.append(FederalReserveSOFRData.model_validate(d))

        return results

```



---

## High-Level Overview

This is a **python** file named `sofr.py`.

**Python Module**

- **Classes** (3): FederalReserveSOFRQueryParams, FederalReserveSOFRData, FederalReserveSOFRFetcher
- **Functions** (4): normalize_percent, transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FederalReserveSOFRQueryParams`**(SOFRQueryParams)
- **`FederalReserveSOFRData`**(SOFRData)
- **`FederalReserveSOFRFetcher`**(
    Fetcher[
        FederalReserveSOFRQueryParams,
        list[FederalReserveSOFRData],
    ]
)

#### Functions

- **`normalize_percent(cls, v)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `EmptyDataError`
- `Fetcher`
- `amake_request`
- `datetime`
- `field_validator`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.sofr`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:49.650113Z
**Generator**: World's Best Repo Book Generator v1.0
