# Documentation: openbb_platform/core/openbb_core/provider/standard_models/symbol_map.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/symbol_map.py`
- **Size**: 462 characters, 15 lines
- **Words**: 50
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Commitment of Traders Reports Search Standard Model."""

from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class SymbolMapQueryParams(QueryParams):
    """Commitment of Traders Reports Search Query."""

    query: str = Field(description="Search query.")
    use_cache: bool | None = Field(
        default=True,
        description="Whether or not to use cache. If True, cache will store for seven days.",
    )

```

## High-Level Overview

Commitment of Traders Reports Search Standard Model.

from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class SymbolMapQueryParams(QueryParams):
Commitment of Traders Reports Search Query.

## Detailed Structure

### Python File Structure

**Classes** (1):
`SymbolMapQueryParams`

**Functions** (0):
None

**Imports** (4):
`openbb_core.provider.abstract.query_params`, `QueryParams`, `pydantic`, `Field`


## Key Components

**Class `SymbolMapQueryParams`**: Commitment of Traders Reports Search Query.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.query_params`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.746531
- Generator: World's Best Repo Book Generator v1.0.0
