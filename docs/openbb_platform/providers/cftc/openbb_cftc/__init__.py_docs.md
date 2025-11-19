# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/cftc/openbb_cftc/__init__.py`
- **Size**: 1,122 bytes
- **Lines**: 24
- **Category**: python
- **Extension**: .py

---

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
- `CftcCotFetcher`
- `CftcCotSearchFetcher`
- `Provider`
- `openbb_cftc.models.cot`
- `openbb_cftc.models.cot_search`
- `openbb_core.provider.abstract.provider`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.652642Z
**Generator**: World's Best Repo Book Generator v1.0
