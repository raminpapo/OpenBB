# Documentation: openbb_platform/core/openbb_core/provider/standard_models/currency_snapshots.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/currency_snapshots.py`
- **Size**: 3,074 characters, 82 lines
- **Words**: 328
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Currency Snapshots Standard Model."""

from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field, field_validator


class CurrencySnapshotsQueryParams(QueryParams):
    """Currency Snapshots Query Params."""

    base: str = Field(description="The base currency symbol.", default="usd")
    quote_type: Literal["direct", "indirect"] = Field(
        description="Whether the quote is direct or indirect."
        + " Selecting 'direct' will return the exchange rate"
        + " as the amount of domestic currency required to buy one unit"
        + " of the foreign currency."
        + " Selecting 'indirect' (default) will return the exchange rate"
        + " as the amount of foreign currency required to buy one unit"
        + " of the domestic currency.",
        default="indirect",
    )
    counter_currencies: str | list[str] | None = Field(
        description="An optional list of counter currency symbols to filter for."
        + " None returns all.",
        default=None,
    )

    @field_validator("base", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v):
        """Convert the base currency to uppercase."""
        return v.upper()

    @field_validator("counter_currencies", mode="before", check_fields=False)
    @classmethod
    def convert_string(cls, v):
        """Convert the counter currencies to an upper case string list."""
        if v is not None:
            return ",".join(v).upper() if isinstance(v, list) else v.upper()
        return None


class CurrencySnapshotsData(Data):
    """Currency Snapshots Data."""

    base_currency: str = Field(description="The base, or domestic, currency.")
    counter_currency: str = Field(description="The counter, or foreign, currency.")
    last_rate: float = Field(
        description="The exchange rate, relative to the base currency."
        + " Rates are expressed as the amount of foreign currency"
        + " received from selling one unit of the base currency,"
        + " or the quantity of foreign currency required to purchase"
        + " one unit of the domestic currency."
        + " To inverse the perspective, set the 'quote_type' parameter as 'direct'.",
    )
    open: float | None = Field(
        description=DATA_DESCRIPTIONS.get("open", ""),
        default=None,
    )
    high: float | None = Field(
        description=DATA_DESCRIPTIONS.get("high", ""),
        default=None,
    )
    low: float | None = Field(
        description=DATA_DESCRIPTIONS.get("low", ""),
        default=None,
    )
    close: float | None = Field(
        description=DATA_DESCRIPTIONS.get("close", ""),
        default=None,
    )
    volume: int | None = Field(
        description=DATA_DESCRIPTIONS.get("volume", ""), default=None
    )
    prev_close: float | None = Field(
        description=DATA_DESCRIPTIONS.get("prev_close", ""),
        default=None,
    )

```

## High-Level Overview

Currency Snapshots Standard Model.

from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field, field_validator


class CurrencySnapshotsQueryParams(QueryParams):
Currency Snapshots Query Params.
Convert the base currency to uppercase.
return v.upper()

@field_validator("counter_currencies", mode="before", check_fields=False)
@classmethod
def convert_string(cls, v):
Convert the counter currencies to an upper case string list.
Currency Snapshots Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`CurrencySnapshotsQueryParams`, `CurrencySnapshotsData`

**Functions** (2):
`to_upper`, `convert_string`

**Imports** (11):
`typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`, `selling`


## Key Components

**Class `CurrencySnapshotsQueryParams`**: Currency Snapshots Query Params.

**Class `CurrencySnapshotsData`**: Currency Snapshots Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.579739
- Generator: World's Best Repo Book Generator v1.0.0
