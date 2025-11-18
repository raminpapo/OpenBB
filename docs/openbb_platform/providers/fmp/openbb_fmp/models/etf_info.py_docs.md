# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/etf_info.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/etf_info.py`
- **Size**: 4,145 characters, 126 lines
- **Words**: 370
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP ETF Info Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.etf_info import (
    EtfInfoData,
    EtfInfoQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import ConfigDict, Field, field_validator


class FMPEtfInfoQueryParams(EtfInfoQueryParams):
    """FMP ETF Info Query."""

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class FMPEtfInfoData(EtfInfoData):
    """FMP ETF Info Data."""

    model_config = ConfigDict(extra="ignore")

    __alias_dict__ = {
        "issuer": "etfCompany",
        "cusip": "securityCusip",
        "aum": "assetsUnderManagement",
        "nav": "netAssetValue",
        "currency": "navCurrency",
        "volume_avg": "avgVolume",
        "updated": "updatedAt",
    }

    cusip: str | None = Field(default=None, description="CUSIP of the ETF.")
    isin: str | None = Field(default=None, description="ISIN of the ETF.")
    asset_class: str | None = Field(default=None, description="Asset class of the ETF.")
    currency: str | None = Field(
        default=None, description="Currency of the ETF's net asset value."
    )
    holdings_count: int | None = Field(default=None, description="Number of holdings.")
    aum: float | None = Field(
        default=None,
        description="Assets under management.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    expense_ratio: float | None = Field(
        default=None,
        description="The expense ratio, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    nav: float | None = Field(
        default=None,
        description="Net asset value of the ETF.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    volume_avg: int | float | None = Field(
        default=None, description="Average daily trading volume."
    )
    updated: datetime | None = Field(
        default=None, description="As of date for the latest data point."
    )

    @field_validator("expense_ratio", mode="before", check_fields=False)
    @classmethod
    def _normalize_percent(cls, v):
        """Normalize percent values."""
        return v / 100 if v else None


class FMPEtfInfoFetcher(
    Fetcher[
        FMPEtfInfoQueryParams,
        list[FMPEtfInfoData],
    ]
):
    """FMP ETF Info Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPEtfInfoQueryParams:
        """Transform the query."""
        return FMPEtfInfoQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPEtfInfoQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        import warnings
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        symbols = query.symbol.split(",")
        results: list = []

        async def get_one(symbol):
            """Get one symbol."""
            url = f"https://financialmodelingprep.com/stable/etf/info?symbol={symbol}&apikey={api_key}"
            response = await get_data_many(url, **kwargs)
            if not response:
                warnings.warn(f"No results found for {symbol}.")
            results.extend(response)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        return sorted(
            results,
            key=(lambda item: (symbols.index(item.get("symbol", len(symbols))))),
        )

    @staticmethod
    def transform_data(
        query: FMPEtfInfoQueryParams, data: list, **kwargs: Any
    ) -> list[FMPEtfInfoData]:
        """Return the transformed data."""
        if not data:
            raise EmptyDataError("No data was found for the given symbols.")
        return [FMPEtfInfoData.model_validate(d) for d in data]

```

## High-Level Overview

FMP ETF Info Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.etf_info import (
EtfInfoData,
EtfInfoQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import ConfigDict, Field, field_validator


class FMPEtfInfoQueryParams(EtfInfoQueryParams):
FMP ETF Info Query.
FMP ETF Info Data.


## Detailed Structure

### Python File Structure

**Classes** (4):
`FMPEtfInfoQueryParams`, `FMPEtfInfoData`, `of`, `FMPEtfInfoFetcher`

**Functions** (5):
`_normalize_percent`, `transform_query`, `aextract_data`, `get_one`, `transform_data`

**Imports** (16):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.etf_info`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `ConfigDict`, `the`, `asyncio`, `warnings`, `openbb_fmp.utils.helpers`, `get_data_many`


## Key Components

**Class `FMPEtfInfoQueryParams`**: FMP ETF Info Query.

**Class `FMPEtfInfoData`**: FMP ETF Info Data.

**Class `of`**: No documentation

**Class `FMPEtfInfoFetcher`**: FMP ETF Info Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.etf_info`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `asyncio`
- `warnings`
- `openbb_fmp.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:39.367796
- Generator: World's Best Repo Book Generator v1.0.0
