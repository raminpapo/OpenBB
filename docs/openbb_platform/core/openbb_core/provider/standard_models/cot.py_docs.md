# Documentation: openbb_platform/core/openbb_core/provider/standard_models/cot.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/cot.py`
- **Size**: 2,930 characters, 76 lines
- **Words**: 311
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Commitment of Traders Reports Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class COTQueryParams(QueryParams):
    """Commitment of Traders Reports Query."""

    id: str = Field(
        description="A string with the CFTC market code or other identifying string,"
        + " such as the contract market name, commodity name, or commodity group - i.e, 'gold' or 'japanese yen'."
        + "Default report is Fed Funds Futures. Use the 'cftc_market_code' for an exact match.",
        default="045601",
    )
    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", "")
        + " Default is the most recent report.",
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class COTData(Data):
    """Commitment of Traders Reports Data.
    Data returned will vary based on the query, this model will not define all possible fields.
    """

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    report_week: str | None = Field(
        default=None, description="Report week for the year."
    )
    market_and_exchange_names: str | None = Field(
        default=None, description="Market and exchange names."
    )
    cftc_contract_market_code: str | None = Field(
        default=None, description="CFTC contract market code."
    )
    cftc_market_code: str | None = Field(default=None, description="CFTC market code.")
    cftc_region_code: str | None = Field(default=None, description="CFTC region code.")
    cftc_commodity_code: str | None = Field(
        default=None, description="CFTC commodity code."
    )
    cftc_contract_market_code_quotes: str | None = Field(
        default=None, description="CFTC contract market code quotes."
    )
    cftc_market_code_quotes: str | None = Field(
        default=None, description="CFTC market code quotes."
    )
    cftc_commodity_code_quotes: str | None = Field(
        default=None, description="CFTC commodity code quotes."
    )
    cftc_subgroup_code: str | None = Field(
        default=None, description="CFTC subgroup code."
    )
    commodity: str | None = Field(default=None, description="Commodity.")
    commodity_group: str | None = Field(
        default=None, description="Commodity group name."
    )
    commodity_subgroup: str | None = Field(
        default=None, description="Commodity subgroup name."
    )
    futonly_or_combined: str | None = Field(
        default=None, description="If the report is futures-only or combined."
    )
    contract_units: str | None = Field(default=None, description="Contract units.")

```

## High-Level Overview

Commitment of Traders Reports Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class COTQueryParams(QueryParams):
Commitment of Traders Reports Query.
Commitment of Traders Reports Data.
Data returned will vary based on the query, this model will not define all possible fields.


## Detailed Structure

### Python File Structure

**Classes** (2):
`COTQueryParams`, `COTData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `COTQueryParams`**: Commitment of Traders Reports Query.

**Class `COTData`**: Commitment of Traders Reports Data.
    Data returned will vary based on the query, this model will not define all possible fields.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.567160
- Generator: World's Best Repo Book Generator v1.0.0
