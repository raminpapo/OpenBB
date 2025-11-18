# Documentation: openbb_platform/providers/multpl/openbb_multpl/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/multpl/openbb_multpl/__init__.py`
- **Size**: 419 characters, 14 lines
- **Words**: 27
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Multpl Provider Module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_multpl.models.sp500_multiples import MultplSP500MultiplesFetcher

multpl_provider = Provider(
    name="multpl",
    website="https://www.multpl.com/",
    description="""Public broad-market data published to https://multpl.com.""",
    fetcher_dict={
        "SP500Multiples": MultplSP500MultiplesFetcher,
    },
)

```

## High-Level Overview

Multpl Provider Module.

from openbb_core.provider.abstract.provider import Provider
from openbb_multpl.models.sp500_multiples import MultplSP500MultiplesFetcher

multpl_provider = Provider(
name="multpl",
website="https://www.multpl.com/",
description="""Public broad-market data published to https://multpl.com.""",
fetcher_dict={
"SP500Multiples": MultplSP500MultiplesFetcher,
},
)


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (4):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_multpl.models.sp500_multiples`, `MultplSP500MultiplesFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_multpl.models.sp500_multiples`

## Notes
- Generated: 2025-11-18T07:54:40.286785
- Generator: World's Best Repo Book Generator v1.0.0
