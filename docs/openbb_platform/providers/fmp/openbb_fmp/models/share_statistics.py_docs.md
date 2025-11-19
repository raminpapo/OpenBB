# File Documentation: share_statistics.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/share_statistics.py`
- **Size**: 2,970 bytes
- **Lines**: 99
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP Share Statistics Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.share_statistics import (
    ShareStatisticsData,
    ShareStatisticsQueryParams,
)
from pydantic import Field, field_validator


class FMPShareStatisticsQueryParams(ShareStatisticsQueryParams):
    """FMP Share Statistics Query.

    Source: https://site.financialmodelingprep.com/developer/docs#shares-float
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class FMPShareStatisticsData(ShareStatisticsData):
    """FMP Share Statistics Data."""

    __alias_dict__ = {"url": "source"}

    url: str | None = Field(
        default=None,
        description="URL to the source document, if available.",
    )

    @field_validator("free_float", mode="before")
    @classmethod
    def _normalize_percent(cls, v):
        """Return the date as a datetime object."""
        return v / 100 if v else None


class FMPShareStatisticsFetcher(
    Fetcher[
        FMPShareStatisticsQueryParams,
        list[FMPShareStatisticsData],
    ]
):
    """FMP Share Statistics Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPShareStatisticsQueryParams:
        """Transform the query params."""
        return FMPShareStatisticsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPShareStatisticsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_urls

        api_key = credentials.get("fmp_api_key") if credentials else ""
        symbols = query.symbol.split(",")

        urls = [
            f"https://financialmodelingprep.com/stable/shares-float?symbol={symbol}&apikey={api_key}"
            for symbol in symbols
        ]

        return await get_data_urls(urls, **kwargs)  # type: ignore

    @staticmethod
    def transform_data(
        query: FMPShareStatisticsQueryParams, data: list, **kwargs: Any
    ) -> list[FMPShareStatisticsData]:
        """Return the transformed data."""
        # pylint: disable=import-outside-toplevel
        import warnings

        symbols = query.symbol.split(",")

        if len(symbols) != len(data):
            data_symbols = {d["symbol"] for d in data if "symbol" in d}
            missing_symbols = set(symbols) - data_symbols
            if missing_symbols:
                warnings.warn(
                    f"No data found for symbols: {', '.join(missing_symbols)}"
                )

        return [
            FMPShareStatisticsData.model_validate(d)
            for d in sorted(
                data,
                key=(lambda item: (symbols.index(item.get("symbol", len(symbols))))),
            )
        ]

```



---

## High-Level Overview

This is a **python** file named `share_statistics.py`.

**Python Module**

- **Classes** (3): FMPShareStatisticsQueryParams, FMPShareStatisticsData, FMPShareStatisticsFetcher
- **Functions** (4): _normalize_percent, transform_query, aextract_data, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPShareStatisticsQueryParams`**(ShareStatisticsQueryParams)
- **`FMPShareStatisticsData`**(ShareStatisticsData)
- **`FMPShareStatisticsFetcher`**(
    Fetcher[
        FMPShareStatisticsQueryParams,
        list[FMPShareStatisticsData],
    ]
)

#### Functions

- **`_normalize_percent(cls, v)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Field`
- `get_data_urls`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.share_statistics`
- `openbb_fmp.utils.helpers`
- `pydantic`
- `typing`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.693579Z
**Generator**: World's Best Repo Book Generator v1.0
