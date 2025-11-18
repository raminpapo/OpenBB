# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/etf_sectors.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/etf_sectors.py`
- **Size**: 2,874 characters, 97 lines
- **Words**: 224
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

FMP ETF Sectors Model.

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
FMP ETF Sectors Query.
FMP ETF Sectors Data.

__alias_dict__ = {"weight": "weightPercentage"}

## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPEtfSectorsQueryParams`, `FMPEtfSectorsData`, `FMPEtfSectorsFetcher`

**Functions** (4):
`_normalize_percent`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (13):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.etf_sectors`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `field_validator`, `the`, `openbb_fmp.utils.helpers`, `get_data_urls`, `warnings`


## Key Components

**Class `FMPEtfSectorsQueryParams`**: FMP ETF Sectors Query.

**Class `FMPEtfSectorsData`**: FMP ETF Sectors Data.

**Class `FMPEtfSectorsFetcher`**: FMP ETF Sectors Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.etf_sectors`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `openbb_fmp.utils.helpers`
- `warnings`

## Notes
- Generated: 2025-11-18T07:54:39.370885
- Generator: World's Best Repo Book Generator v1.0.0
