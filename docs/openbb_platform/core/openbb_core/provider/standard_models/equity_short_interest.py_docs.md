# File Documentation: equity_short_interest.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_short_interest.py`
- **Size**: 3,527 bytes
- **Lines**: 80
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Equity Short Interest Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class ShortInterestQueryParams(QueryParams):
    """Equity Short Interest Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))


class ShortInterestData(Data):
    """Equity Short Interest Data."""

    settlement_date: dateType = Field(
        description=(
            "The mid-month short interest report is based on short positions held by "
            "members on the settlement date of the 15th of each month. If the 15th falls "
            "on a weekend or another non-settlement date, the designated settlement date "
            "will be the previous business day on which transactions settled. The "
            "end-of-month short interest report is based on short positions held on the "
            "last business day of the month on which transactions settle. Once the short "
            "position reports are received, the short interest data is compiled for each "
            "equity security and provided for publication on the 7th business day after "
            "the reporting settlement date."
        )
    )
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    issue_name: str = Field(description="Unique identifier of the issue.")
    market_class: str = Field(description="Primary listing market.")
    current_short_position: float = Field(
        description=(
            "The total number of shares in the issue that are reflected on the books "
            "and records of the reporting firms as short as defined by Rule 200 of "
            "Regulation SHO as of the current cycle’s designated settlement date."
        )
    )
    previous_short_position: float = Field(
        description=(
            "The total number of shares in the issue that are reflected on the books "
            "and records of the reporting firms as short as defined by Rule 200 of "
            "Regulation SHO as of the previous cycle’s designated settlement date."
        )
    )
    avg_daily_volume: float = Field(
        description=(
            "Total Volume or Adjusted Volume in case of splits / Total trade days "
            "between (previous settlement date + 1) to (current settlement date). The "
            "NULL values are translated as zero."
        )
    )

    days_to_cover: float = Field(
        description=(
            "The number of days of average share volume it would require to buy all of "
            "the shares that were sold short during the reporting cycle. Formula: Short "
            "Interest / Average Daily Share Volume, Rounded to Hundredths. 1.00 will be "
            "displayed for any values equal or less than 1 (i.e., Average Daily Share is "
            "equal to or greater than Short Interest). N/A will be displayed If the days "
            "to cover is Zero (i.e., Average Daily Share Volume is Zero)."
        )
    )
    change: float = Field(
        description=(
            "Change in Shares Short from Previous Cycle: Difference in short interest "
            "between the current cycle and the previous cycle."
        )
    )
    change_pct: float = Field(
        description="Change in Shares Short from Previous Cycle as a percent."
    )

```



---

## High-Level Overview

This is a **python** file named `equity_short_interest.py`.

**Python Module**

- **Classes** (2): ShortInterestQueryParams, ShortInterestData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ShortInterestQueryParams`**(QueryParams)
- **`ShortInterestData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
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

**Generated**: 2025-11-19T02:16:46.433462Z
**Generator**: World's Best Repo Book Generator v1.0
