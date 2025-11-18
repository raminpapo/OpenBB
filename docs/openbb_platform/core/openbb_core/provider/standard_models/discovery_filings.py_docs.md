# Documentation: openbb_platform/core/openbb_core/provider/standard_models/discovery_filings.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/discovery_filings.py`
- **Size**: 1,558 characters, 50 lines
- **Words**: 137
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Discovery Filings Standard Model."""

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
from pydantic import Field, NonNegativeInt


class DiscoveryFilingsQueryParams(QueryParams):
    """Discovery Filings Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS["start_date"],
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS["end_date"],
    )
    form_type: str | None = Field(
        default=None,
        description=(
            "Filter by form type. Visit https://www.sec.gov/forms for a list of supported form types."
        ),
    )
    limit: NonNegativeInt | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("limit", "")
    )


class DiscoveryFilingsData(Data):
    """Discovery Filings Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    cik: str = Field(description=DATA_DESCRIPTIONS.get("cik", ""))
    filing_date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    accepted_date: datetime = Field(
        description=DATA_DESCRIPTIONS.get("accepted_date", "")
    )
    form_type: str = Field(description="The form type of the filing")
    link: str = Field(description="URL to the filing page on the SEC site.")

```

## High-Level Overview

Discovery Filings Standard Model.

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
from pydantic import Field, NonNegativeInt


class DiscoveryFilingsQueryParams(QueryParams):
Discovery Filings Query.
Discovery Filings Data.


## Detailed Structure

### Python File Structure

**Classes** (2):
`DiscoveryFilingsQueryParams`, `DiscoveryFilingsData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `DiscoveryFilingsQueryParams`**: Discovery Filings Query.

**Class `DiscoveryFilingsData`**: Discovery Filings Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.582433
- Generator: World's Best Repo Book Generator v1.0.0
