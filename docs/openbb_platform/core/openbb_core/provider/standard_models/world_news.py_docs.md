# File Documentation: world_news.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/world_news.py`
- **Size**: 2,274 bytes
- **Lines**: 71
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""World News Standard Model."""

from datetime import (
    date as dateType,
    datetime,
)
from typing import Any

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, NonNegativeInt, field_validator


class WorldNewsQueryParams(QueryParams):
    """World News Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", "")
        + " The default is 2 weeks ago.",
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", "") + " The default is today.",
    )
    limit: NonNegativeInt | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("limit", "")
        + " The number of articles to return.",
    )

    @field_validator("start_date", mode="before")
    @classmethod
    def start_date_validate(cls, v) -> dateType:  # pylint: disable=E0213
        """Populate start date if empty."""
        if not v:
            now = datetime.now().date()
            v = now - relativedelta(weeks=2)
        return v

    @field_validator("end_date", mode="before")
    @classmethod
    def end_date_validate(cls, v) -> dateType:  # pylint: disable=E0213
        """Populate end date if empty."""
        if not v:
            v = datetime.now().date()
        return v


class WorldNewsData(Data):
    """World News Data."""

    date: datetime = Field(
        description=DATA_DESCRIPTIONS.get("date", "") + " The date of publication."
    )
    title: str = Field(description="Title of the article.")
    author: str | None = Field(default=None, description="Author of the article.")
    excerpt: str | None = Field(
        default=None, description="Excerpt of the article text."
    )
    body: str | None = Field(default=None, description="Body of the article text.")
    images: Any | None = Field(
        default=None, description="Images associated with the article."
    )
    url: str | None = Field(default=None, description="URL to the article.")

```



---

## High-Level Overview

This is a **python** file named `world_news.py`.

**Python Module**

- **Classes** (2): WorldNewsQueryParams, WorldNewsData
- **Functions** (2): start_date_validate, end_date_validate
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`WorldNewsQueryParams`**(QueryParams)
- **`WorldNewsData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Data`
- `Field`
- `QueryParams`
- `datetime`
- `dateutil.relativedelta`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `relativedelta`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.598025Z
**Generator**: World's Best Repo Book Generator v1.0
