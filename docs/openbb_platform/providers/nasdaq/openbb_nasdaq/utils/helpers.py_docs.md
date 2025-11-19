# File Documentation: helpers.py

## Metadata
- **Path**: `openbb_platform/providers/nasdaq/openbb_nasdaq/utils/helpers.py`
- **Size**: 2,473 bytes
- **Lines**: 79
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Nasdaq Helpers Module."""

from functools import lru_cache


def remove_html_tags(text: str):
    """Remove HTML tags from a string."""
    # pylint: disable=import-outside-toplevel
    import re

    clean = re.compile("<.*?>")
    return re.sub(clean, " ", text)


def get_random_agent() -> str:
    """Generate a random user agent for a request."""
    # pylint: disable=import-outside-toplevel
    from random_user_agent.user_agent import UserAgent

    user_agent_rotator = UserAgent(limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent


def get_headers(accept_type: str = "json") -> dict:
    """Get the headers for the request."""
    if accept_type not in ["json", "text"]:
        raise ValueError("Invalid accept_type. Must be either 'json' or 'text'.")

    return (
        {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
            "Host": "api.nasdaq.com",
            "User-Agent": get_random_agent(),
            "Connection": "keep-alive",
        }
        if accept_type == "text"
        else {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
            "Host": "api.nasdaq.com",
            "Origin": "https://www.nasdaq.com",
            "Referer": "https://www.nasdaq.com/",
            "User-Agent": get_random_agent(),
            "Connection": "keep-alive",
        }
    )


def date_range(start_date, end_date):
    """Yield dates between start_date and end_date."""
    # pylint: disable=import-outside-toplevel
    from datetime import timedelta

    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


@lru_cache(maxsize=1)
def get_nasdaq_directory() -> str:
    """Get the Nasdaq directory from the FTP site."""
    # pylint: disable=import-outside-toplevel
    from openbb_core.app.model.abstract.error import OpenBBError  # noqa
    from urllib.error import URLError
    from urllib.request import urlopen

    url = "ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqtraded.txt"

    try:
        with urlopen(url) as response:  # noqa: S310
            data = response.read().decode("utf-8")
    except URLError as e:
        raise OpenBBError(e) from e

    return data

```



---

## High-Level Overview

This is a **python** file named `helpers.py`.

**Python Module**

- **Functions** (5): remove_html_tags, get_random_agent, get_headers, date_range, get_nasdaq_directory
- **Import Statements**: 6


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`remove_html_tags(text: str)`**
- **`date_range(start_date, end_date)`**

#### Decorators Used

lru_cache


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `OpenBBError`
- `URLError`
- `UserAgent`
- `datetime`
- `functools`
- `lru_cache`
- `openbb_core.app.model.abstract.error`
- `random_user_agent.user_agent`
- `re`
- `timedelta`
- `urllib.error`
- `urllib.request`
- `urlopen`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.658930Z
**Generator**: World's Best Repo Book Generator v1.0
