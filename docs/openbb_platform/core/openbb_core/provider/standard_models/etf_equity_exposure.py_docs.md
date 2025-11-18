# Documentation: openbb_platform/core/openbb_core/provider/standard_models/etf_equity_exposure.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_equity_exposure.py`
- **Size**: 1,439 characters, 43 lines
- **Words**: 147
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ETF Equity Exposure Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class EtfEquityExposureQueryParams(QueryParams):
    """ETF Equity Exposure Query Params."""

    symbol: str = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", "") + " (underlying equity)"
    )

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfEquityExposureData(Data):
    """ETF Equity Exposure Data."""

    equity_symbol: str = Field(description="The symbol of the equity requested.")
    etf_symbol: str = Field(
        description="The symbol of the ETF with exposure to the requested equity."
    )
    weight: float | None = Field(
        default=None,
        description="The weight of the equity in the ETF, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    market_value: int | float | None = Field(
        default=None,
        description="The market value of the equity position in the ETF.",
    )
    shares: int | float | None = Field(
        default=None,
        description="Number of reported shares controlled by the ETF.",
    )

```

## High-Level Overview

ETF Equity Exposure Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class EtfEquityExposureQueryParams(QueryParams):
ETF Equity Exposure Query Params.
Convert field to uppercase.
return v.upper()


class EtfEquityExposureData(Data):
ETF Equity Exposure Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`EtfEquityExposureQueryParams`, `EtfEquityExposureData`

**Functions** (1):
`to_upper`

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `EtfEquityExposureQueryParams`**: ETF Equity Exposure Query Params.

**Class `EtfEquityExposureData`**: ETF Equity Exposure Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.614287
- Generator: World's Best Repo Book Generator v1.0.0
