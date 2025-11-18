# Documentation: openbb_platform/core/openbb_core/provider/standard_models/analyst_search.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/analyst_search.py`
- **Size**: 1,223 characters, 49 lines
- **Words**: 128
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Analyst Search Standard Model."""

from datetime import (
    datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class AnalystSearchQueryParams(QueryParams):
    """Analyst Search Query."""

    analyst_name: str | None = Field(
        default=None,
        description="Analyst names to return."
        + " Omitting will return all available analysts.",
    )
    firm_name: str | None = Field(
        default=None,
        description="Firm names to return."
        + " Omitting will return all available firms.",
    )


class AnalystSearchData(Data):
    """Analyst Search data."""

    last_updated: datetime | None = Field(
        default=None,
        description="Date of the last update.",
    )
    firm_name: str | None = Field(
        default=None,
        description="Firm name of the analyst.",
    )
    name_first: str | None = Field(
        default=None,
        description="Analyst first name.",
    )
    name_last: str | None = Field(
        default=None,
        description="Analyst last name.",
    )
    name_full: str = Field(
        description="Analyst full name.",
    )

```

## High-Level Overview

Analyst Search Standard Model.

from datetime import (
datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class AnalystSearchQueryParams(QueryParams):
Analyst Search Query.
Analyst Search data.

last_updated: datetime | None = Field(
default=None,
description="Date of the last update.",
)
firm_name: str | None = Field(

## Detailed Structure

### Python File Structure

**Classes** (2):
`AnalystSearchQueryParams`, `AnalystSearchData`

**Functions** (0):
None

**Imports** (7):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `pydantic`, `Field`


## Key Components

**Class `AnalystSearchQueryParams`**: Analyst Search Query.

**Class `AnalystSearchData`**: Analyst Search data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.526195
- Generator: World's Best Repo Book Generator v1.0.0
