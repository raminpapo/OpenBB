# Documentation: openbb_platform/providers/nasdaq/openbb_nasdaq/utils/query_params.py

## File Metadata
- **Path**: `openbb_platform/providers/nasdaq/openbb_nasdaq/utils/query_params.py`
- **Size**: 1,037 characters, 31 lines
- **Words**: 96
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Nasdaq Data Link Standard Query Params."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class DataLinkQueryParams(QueryParams):
    """Standard Nasdaq Data Link Query Params"""

    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
        default=None,
    )
    transform: Literal["diff", "rdiff", "cumul", "normalize", None] = Field(
        description="Transform the data as difference, percent change, cumulative, or normalize.",
        default=None,
    )
    collapse: Literal["daily", "weekly", "monthly", "quarterly", "annual", None] = (
        Field(
            description="Collapse the frequency of the time series.",
            default=None,
        )
    )

```

## High-Level Overview

Nasdaq Data Link Standard Query Params.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class DataLinkQueryParams(QueryParams):
Standard Nasdaq Data Link Query Params

## Detailed Structure

### Python File Structure

**Classes** (1):
`DataLinkQueryParams`

**Functions** (0):
None

**Imports** (10):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `DataLinkQueryParams`**: Standard Nasdaq Data Link Query Params

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:40.333772
- Generator: World's Best Repo Book Generator v1.0.0
