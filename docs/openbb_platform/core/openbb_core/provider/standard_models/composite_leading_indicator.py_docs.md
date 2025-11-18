# Documentation: openbb_platform/core/openbb_core/provider/standard_models/composite_leading_indicator.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/composite_leading_indicator.py`
- **Size**: 1,049 characters, 35 lines
- **Words**: 82
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Composite Leading Indicator Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CompositeLeadingIndicatorQueryParams(QueryParams):
    """Composite Leading Indicator Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class CompositeLeadingIndicatorData(Data):
    """Composite Leading Indicator Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
    value: float = Field(
        default=None,
        description="CLI value",
        json_schema_extra={"x-unit_measurement": "index"},
    )
    country: str = Field(description="Country for the CLI value.")

```

## High-Level Overview

Composite Leading Indicator Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CompositeLeadingIndicatorQueryParams(QueryParams):
Composite Leading Indicator Query.
Composite Leading Indicator Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
value: float = Field(
default=None,

## Detailed Structure

### Python File Structure

**Classes** (2):
`CompositeLeadingIndicatorQueryParams`, `CompositeLeadingIndicatorData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CompositeLeadingIndicatorQueryParams`**: Composite Leading Indicator Query.

**Class `CompositeLeadingIndicatorData`**: Composite Leading Indicator Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.564213
- Generator: World's Best Repo Book Generator v1.0.0
