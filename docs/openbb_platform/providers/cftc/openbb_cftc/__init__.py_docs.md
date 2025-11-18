# Documentation: openbb_platform/providers/cftc/openbb_cftc/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/cftc/openbb_cftc/__init__.py`
- **Size**: 1,122 characters, 24 lines
- **Words**: 108
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""CFTC provider extension module."""

from openbb_cftc.models.cot import CftcCotFetcher
from openbb_cftc.models.cot_search import CftcCotSearchFetcher
from openbb_core.provider.abstract.provider import Provider

cftc_provider = Provider(
    name="cftc",
    website="https://cftc.gov/",
    description="""The mission of the Commodity Futures Trading Commission (CFTC) is to promote the integrity,
    resilience, and vibrancy of the U.S. derivatives markets through sound regulation.""",
    credentials=["app_token"],  # This is optional
    fetcher_dict={
        "COT": CftcCotFetcher,
        "COTSearch": CftcCotSearchFetcher,
    },
    repr_name="Commodity Futures Trading Commission (CFTC) Public Reporting API",
    instructions="""Credentials are not required, but your IP address may be subject to throttling limits.
    API requests made using an application token are not throttled.
    Create an account here: https://evergreen.data.socrata.com/signup
    and then generate the app_token by signing in with the credentials
    here: https://publicreporting.cftc.gov/profile/edit/developer_settings.""",
)

```

## High-Level Overview

CFTC provider extension module.

from openbb_cftc.models.cot import CftcCotFetcher
from openbb_cftc.models.cot_search import CftcCotSearchFetcher
from openbb_core.provider.abstract.provider import Provider

cftc_provider = Provider(
name="cftc",
website="https://cftc.gov/",
description="""The mission of the Commodity Futures Trading Commission (CFTC) is to promote the integrity,
resilience, and vibrancy of the U.S. derivatives markets through sound regulation.""",
credentials=["app_token"],  # This is optional
fetcher_dict={
"COT": CftcCotFetcher,
"COTSearch": CftcCotSearchFetcher,
},
repr_name="Commodity Futures Trading Commission (CFTC) Public Reporting API",
instructions="""Credentials are not required, but your IP address may be subject to throttling limits.
API requests made using an application token are not throttled.
Create an account here: https://evergreen.data.socrata.com/signup

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (6):
`openbb_cftc.models.cot`, `CftcCotFetcher`, `openbb_cftc.models.cot_search`, `CftcCotSearchFetcher`, `openbb_core.provider.abstract.provider`, `Provider`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_cftc.models.cot`
- `openbb_cftc.models.cot_search`
- `openbb_core.provider.abstract.provider`

## Notes
- Generated: 2025-11-18T07:54:37.567862
- Generator: World's Best Repo Book Generator v1.0.0
