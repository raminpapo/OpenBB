# File Documentation: esg_score.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/esg_score.py`
- **Size**: 1,822 bytes
- **Lines**: 55
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ESG Score Standard Model."""

from datetime import (
    date as dateType,
    datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EsgScoreQueryParams(QueryParams):
    """ESG Score Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EsgScoreData(Data):
    """ESG Score Data."""

    period_ending: dateType = Field(description="Period ending date of the report.")
    disclosure_date: dateType | datetime | None = Field(
        description="Date when the report was submitted."
    )
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    cik: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("cik", ""),
        coerce_numbers_to_str=True,
    )
    company_name: str | None = Field(
        default=None, description="Company name of the company."
    )
    form_type: str | None = Field(
        default=None, description="Form type where the disclosure was made."
    )
    environmental_score: float = Field(
        description="Environmental score of the company."
    )
    social_score: float = Field(description="Social score of the company.")
    governance_score: float = Field(description="Governance score of the company.")
    esg_score: float = Field(description="ESG score of the company.")
    url: str | None = Field(default=None, description="URL to the report or filing.")

```



---

## High-Level Overview

This is a **python** file named `esg_score.py`.

**Python Module**

- **Classes** (2): EsgScoreQueryParams, EsgScoreData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EsgScoreQueryParams`**(QueryParams)
- **`EsgScoreData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.436698Z
**Generator**: World's Best Repo Book Generator v1.0
