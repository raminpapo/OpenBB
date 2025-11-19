# File Documentation: definitions.py

## Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/utils/definitions.py`
- **Size**: 1,122 bytes
- **Lines**: 46
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `definitions.py`.

**Python Module**

- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Literal`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.416135Z
**Generator**: World's Best Repo Book Generator v1.0
