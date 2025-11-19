# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/government_us/openbb_government_us/__init__.py`
- **Size**: 976 bytes
- **Lines**: 25
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Government US provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_government_us.models.treasury_auctions import (
    GovernmentUSTreasuryAuctionsFetcher,
)
from openbb_government_us.models.treasury_prices import (
    GovernmentUSTreasuryPricesFetcher,
)

government_us_provider = Provider(
    name="government_us",
    website="https://data.gov",
    description="""Data.gov is the United States government's open data website.
It provides access to datasets published by agencies across the federal government.
Data.gov is intended to provide access to government open data to the public, achieve
agency missions, drive innovation, fuel economic activity, and uphold the ideals of
an open and transparent government.""",
    fetcher_dict={
        "TreasuryAuctions": GovernmentUSTreasuryAuctionsFetcher,
        "TreasuryPrices": GovernmentUSTreasuryPricesFetcher,
    },
    repr_name="Data.gov | United States Government",
)

```



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Provider`
- `openbb_core.provider.abstract.provider`
- `openbb_government_us.models.treasury_auctions`
- `openbb_government_us.models.treasury_prices`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.206514Z
**Generator**: World's Best Repo Book Generator v1.0
