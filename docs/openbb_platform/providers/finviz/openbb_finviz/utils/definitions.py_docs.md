# Documentation: openbb_platform/providers/finviz/openbb_finviz/utils/definitions.py

## File Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/utils/definitions.py`
- **Size**: 1,122 characters, 46 lines
- **Words**: 86
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Finviz Definitions."""

from typing import Literal

GROUPS = Literal[
    "sector",
    "industry",
    "country",
    "capitalization",
    "energy",
    "materials",
    "industrials",
    "consumer_cyclical",
    "consumer_defensive",
    "healthcare",
    "financial",
    "technology",
    "communication_services",
    "utilities",
    "real_estate",
]

GROUPS_DICT = {
    "sector": "Sector",
    "industry": "Industry",
    "country": "Country (U.S. listed stocks only)",
    "capitalization": "Capitalization",
    "energy": "Industry (Energy)",
    "materials": "Industry (Basic Materials)",
    "industrials": "Industry (Industrials)",
    "consumer_cyclical": "Industry (Consumer Cyclical)",
    "consumer_defensive": "Industry (Consumer Defensive)",
    "healthcare": "Industry (Healthcare)",
    "financial": "Industry (Financial)",
    "technology": "Industry (Technology)",
    "communication_services": "Industry (Communication Services)",
    "utilities": "Industry (Utilities)",
    "real_estate": "Industry (Real Estate)",
}

METRICS = Literal[
    "performance",
    "valuation",
    "overview",
]

```

## High-Level Overview

Finviz Definitions.

from typing import Literal

GROUPS = Literal[
"sector",
"industry",
"country",
"capitalization",
"energy",
"materials",
"industrials",
"consumer_cyclical",
"consumer_defensive",
"healthcare",
"financial",
"technology",
"communication_services",
"utilities",
"real_estate",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (2):
`typing`, `Literal`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`

## Notes
- Generated: 2025-11-18T07:54:39.175745
- Generator: World's Best Repo Book Generator v1.0.0
