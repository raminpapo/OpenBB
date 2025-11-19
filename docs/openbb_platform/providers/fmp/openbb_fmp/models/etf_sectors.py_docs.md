# File Documentation: etf_sectors.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/etf_sectors.py`
- **Size**: 2,874 bytes
- **Lines**: 97
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP ETF Sectors Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.etf_sectors import (
    EtfSectorsData,
    EtfSectorsQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import field_validator


class FMPEtfSectorsQueryParams(EtfSectorsQueryParams):
    """FMP ETF Sectors Query."""

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class FMPEtfSectorsData(EtfSectorsData):
    """FMP ETF Sectors Data."""

    __alias_dict__ = {"weight": "weightPercentage"}

    @field_validator("weight", mode="before", check_fields=False)
    @classmethod
    def _normalize_percent(cls, v):
        """Normalize percent values."""
        return float(v) / 100 if v else None


class FMPEtfSectorsFetcher(
    Fetcher[
        FMPEtfSectorsQueryParams,
        list[FMPEtfSectorsData],
    ]
):
    """FMP ETF Sectors Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPEtfSectorsQueryParams:
        """Transform the query."""
        return FMPEtfSectorsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPEtfSectorsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_urls

        api_key = credentials.get("fmp_api_key") if credentials else ""
        symbols = query.symbol.split(",")

        urls = [
            f"https://financialmodelingprep.com/stable/etf/sector-weightings?symbol={symbol.upper()}&apikey={api_key}"
            for symbol in symbols
        ]

        return await get_data_urls(urls, **kwargs)  # type: ignore

    @staticmethod
    def transform_data(
        query: FMPEtfSectorsQueryParams, data: list, **kwargs: Any
    ) -> list[FMPEtfSectorsData]:
        """Return the transformed data."""
        # pylint: disable=import-outside-toplevel
        import warnings

        if not data:
            raise EmptyDataError("No data found")

        symbols = set(query.symbol.split(","))
        returned_symbols = {
            d.get("symbol", "").upper() for d in data if d.get("symbol")
        }
        missing_symbols = symbols - returned_symbols

        if missing_symbols:
            warnings.warn(f"Missing symbols in response: {missing_symbols}")

        return [
            FMPEtfSectorsData.model_validate(d)
            for d in sorted(
                data,
                key=lambda x: (
                    query.symbol.split(",").index(x.get("symbol", len(symbols))),
                    -(x.get("weightPercentage", 0) or 0),
                ),
            )
        ]

```



---

## High-Level Overview

This is a **python** file named `etf_sectors.py`.

**Python Module**

- **Classes** (3): FMPEtfSectorsQueryParams, FMPEtfSectorsData, FMPEtfSectorsFetcher
- **Functions** (4): _normalize_percent, transform_query, aextract_data, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPEtfSectorsQueryParams`**(EtfSectorsQueryParams)
- **`FMPEtfSectorsData`**(EtfSectorsData)
- **`FMPEtfSectorsFetcher`**(
    Fetcher[
        FMPEtfSectorsQueryParams,
        list[FMPEtfSectorsData],
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
- `EmptyDataError`
- `Fetcher`
- `field_validator`
- `get_data_urls`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.etf_sectors`
- `openbb_core.provider.utils.errors`
- `openbb_fmp.utils.helpers`
- `pydantic`
- `typing`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.637724Z
**Generator**: World's Best Repo Book Generator v1.0
