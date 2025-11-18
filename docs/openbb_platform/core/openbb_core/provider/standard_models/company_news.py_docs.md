# Documentation: openbb_platform/core/openbb_core/provider/standard_models/company_news.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/company_news.py`
- **Size**: 1,926 characters, 62 lines
- **Words**: 190
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Company News Standard Model."""

from datetime import (
    date as dateType,
    datetime,
)
from typing import Any

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, NonNegativeInt, field_validator


class CompanyNewsQueryParams(QueryParams):
    """Company news Query."""

    symbol: str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("symbol", ""),
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    limit: NonNegativeInt | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("limit", "")
    )

    @field_validator("symbol", mode="before")
    @classmethod
    def symbols_validate(cls, v):
        """Validate the symbols."""
        return v.upper() if v else None


class CompanyNewsData(Data):
    """Company News Data."""

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
    url: str = Field(description="URL to the article.")
    symbols: str | None = Field(
        default=None, description="Symbols associated with the article."
    )

```

## High-Level Overview

Company News Standard Model.

from datetime import (
date as dateType,
datetime,
)
from typing import Any

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, NonNegativeInt, field_validator


class CompanyNewsQueryParams(QueryParams):
Company news Query.
Validate the symbols.

## Detailed Structure

### Python File Structure

**Classes** (2):
`CompanyNewsQueryParams`, `CompanyNewsData`

**Functions** (1):
`symbols_validate`

**Imports** (10):
`datetime`, `typing`, `Any`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CompanyNewsQueryParams`**: Company news Query.

**Class `CompanyNewsData`**: Company News Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.560313
- Generator: World's Best Repo Book Generator v1.0.0
