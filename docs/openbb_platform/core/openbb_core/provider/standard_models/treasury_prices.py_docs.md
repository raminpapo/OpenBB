# File Documentation: treasury_prices.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/treasury_prices.py`
- **Size**: 3,576 bytes
- **Lines**: 101
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Treasury Prices Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class TreasuryPricesQueryParams(QueryParams):
    """Treasury Prices Query."""

    date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("date", "")
        + " Defaults to the last business day.",
        default=None,
    )


class TreasuryPricesData(Data):
    """Treasury Prices Data."""

    issuer_name: str | None = Field(
        default=None,
        description="Name of the issuing entity.",
    )
    cusip: str | None = Field(
        default=None,
        description="CUSIP of the security.",
    )
    isin: str | None = Field(
        default=None,
        description="ISIN of the security.",
    )
    security_type: str | None = Field(
        default=None,
        description="The type of Treasury security - i.e., Bill, Note, Bond, TIPS, FRN.",
    )
    issue_date: dateType | None = Field(
        default=None,
        description="The original issue date of the security.",
    )
    maturity_date: dateType | None = Field(
        default=None,
        description="The maturity date of the security.",
    )
    call_date: dateType | None = Field(
        description="The call date of the security.", default=None
    )
    bid: float | None = Field(
        default=None,
        description="The bid price of the security.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    offer: float | None = Field(
        default=None,
        description="The offer price of the security.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    eod_price: float | None = Field(
        default=None,
        description="The end-of-day price of the security.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    last_traded_date: dateType | None = Field(
        description="The last trade date of the security.", default=None
    )
    total_trades: int | None = Field(
        default=None,
        description="Total number of trades on the last traded date.",
    )
    last_price: float | None = Field(
        default=None,
        description="The last price of the security.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    highest_price: float | None = Field(
        default=None,
        description="The highest price for the bond on the last traded date.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    lowest_price: float | None = Field(
        default=None,
        description="The lowest price for the bond on the last traded date.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    rate: float | None = Field(
        description="The annualized interest rate or coupon of the security.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    ytm: float | None = Field(
        default=None,
        description="Yield to maturity (YTM) is the rate of return anticipated on a bond"
        + " if it is held until the maturity date. It takes into account"
        + " the current market price, par value, coupon rate and time to maturity. It is assumed that all"
        + " coupons are reinvested at the same rate.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```



---

## High-Level Overview

This is a **python** file named `treasury_prices.py`.

**Python Module**

- **Classes** (2): TreasuryPricesQueryParams, TreasuryPricesData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TreasuryPricesQueryParams`**(QueryParams)
- **`TreasuryPricesData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QUERY_DESCRIPTIONS`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.592533Z
**Generator**: World's Best Repo Book Generator v1.0
