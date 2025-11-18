# Documentation: openbb_platform/core/openbb_core/provider/standard_models/bls_search.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/bls_search.py`
- **Size**: 772 characters, 24 lines
- **Words**: 76
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""BLS Search Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class SearchQueryParams(QueryParams):
    """BLS Search Query Params."""

    query: str = Field(
        default="",
        description="The search word(s). Use semi-colon to separate multiple queries as an & operator.",
    )


class SearchData(Data):
    """BLS Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    title: str | None = Field(default=None, description="The title of the series.")
    survey_name: str | None = Field(default=None, description="The name of the survey.")

```

## High-Level Overview

BLS Search Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class SearchQueryParams(QueryParams):
BLS Search Query Params.
BLS Search Data.

symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
title: str | None = Field(default=None, description="The title of the series.")
survey_name: str | None = Field(default=None, description="The name of the survey.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`SearchQueryParams`, `SearchData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `SearchQueryParams`**: BLS Search Query Params.

**Class `SearchData`**: BLS Search Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.535661
- Generator: World's Best Repo Book Generator v1.0.0
