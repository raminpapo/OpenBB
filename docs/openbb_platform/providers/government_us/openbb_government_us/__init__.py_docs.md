# Documentation: openbb_platform/providers/government_us/openbb_government_us/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/government_us/openbb_government_us/__init__.py`
- **Size**: 976 characters, 25 lines
- **Words**: 89
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Government US provider module.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (4):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_government_us.models.treasury_auctions`, `openbb_government_us.models.treasury_prices`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_government_us.models.treasury_auctions`
- `openbb_government_us.models.treasury_prices`

## Notes
- Generated: 2025-11-18T07:54:39.899774
- Generator: World's Best Repo Book Generator v1.0.0
