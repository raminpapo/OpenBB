# Documentation: openbb_platform/core/openbb_core/provider/standard_models/bond_reference.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/bond_reference.py`
- **Size**: 2,926 characters, 90 lines
- **Words**: 318
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Bond Reference Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field, field_validator


class BondReferenceQueryParams(QueryParams):
    """Bond Reference Query."""

    country: str | None = Field(
        default=None,
        description="The country to get data. Matches partial name.",
    )
    issuer_name: str | None = Field(
        default=None,
        description="Name of the issuer.  Returns partial matches and is case insensitive.",
    )
    isin: list | str | None = Field(
        default=None,
        description="International Securities Identification Number(s) of the bond(s).",
    )
    lei: str | None = Field(
        default=None,
        description="Legal Entity Identifier of the issuing entity.",
    )
    currency: list | str | None = Field(
        default=None,
        description="Currency of the bond. Formatted as the 3-letter ISO 4217 code (e.g. GBP, EUR, USD).",
    )
    coupon_min: float | None = Field(
        default=None,
        description="Minimum coupon rate of the bond.",
    )
    coupon_max: float | None = Field(
        default=None,
        description="Maximum coupon rate of the bond.",
    )
    issued_amount_min: int | None = Field(
        default=None,
        description="Minimum issued amount of the bond.",
    )
    issued_amount_max: str | None = Field(
        default=None,
        description="Maximum issued amount of the bond.",
    )
    maturity_date_min: dateType | None = Field(
        default=None,
        description="Minimum maturity date of the bond.",
    )
    maturity_date_max: dateType | None = Field(
        default=None,
        description="Maximum maturity date of the bond.",
    )

    @field_validator("isin", "currency", "lei", mode="before", check_fields=False)
    @classmethod
    def validate_upper_case(cls, v):
        """Convert the field to uppercase and convert a list to a query string."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)]) if v else None


class BondReferenceData(Data):
    """Bond Reference Search Data."""

    isin: str | None = Field(
        default=None,
        description="International Securities Identification Number of the bond.",
    )
    lei: str | None = Field(
        default=None,
        description="Legal Entity Identifier of the issuing entity.",
    )
    figi: str | None = Field(default=None, description="FIGI of the bond.")
    cusip: str | None = Field(
        default=None,
        description="CUSIP of the bond.",
    )
    coupon_rate: float | None = Field(
        default=None,
        description="Coupon rate of the bond.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```

## High-Level Overview

Bond Reference Standard Model.

from datetime import (
date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field, field_validator


class BondReferenceQueryParams(QueryParams):
Bond Reference Query.

## Detailed Structure

### Python File Structure

**Classes** (2):
`BondReferenceQueryParams`, `BondReferenceData`

**Functions** (1):
`validate_upper_case`

**Imports** (7):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `pydantic`, `Field`


## Key Components

**Class `BondReferenceQueryParams`**: Bond Reference Query.

**Class `BondReferenceData`**: Bond Reference Search Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.541453
- Generator: World's Best Repo Book Generator v1.0.0
