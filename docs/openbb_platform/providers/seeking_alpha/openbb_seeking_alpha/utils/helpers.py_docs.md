# Documentation: openbb_platform/providers/seeking_alpha/openbb_seeking_alpha/utils/helpers.py

## File Metadata
- **Path**: `openbb_platform/providers/seeking_alpha/openbb_seeking_alpha/utils/helpers.py`
- **Size**: 1,435 characters, 44 lines
- **Words**: 137
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Seeking Alpha Utilities."""

from datetime import timedelta

from openbb_core.provider.utils.helpers import amake_request

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0",  # noqa
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Connection": "keep-alive",
}


def date_range(start_date, end_date):
    """Yield dates between start_date and end_date."""
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


async def get_seekingalpha_id(symbol: str, **kwargs) -> str:
    """Map a ticker symbol to its Seeking Alpha ID."""
    session = kwargs.get("session")
    url = "https://seekingalpha.com/api/v3/searches"
    querystring = {
        "filter[type]": "symbols",
        "filter[list]": "all",
        "page[size]": "100",
    }
    querystring["filter[query]"] = symbol
    if session:
        response = await amake_request(
            url, headers=HEADERS, params=querystring, session=session
        )
    else:
        response = await amake_request(url, headers=HEADERS, params=querystring)
    ids = response.get("symbols")  # type: ignore

    return str(ids[0].get("id", "")) if isinstance(ids, list) and ids else ""

```

## High-Level Overview

Seeking Alpha Utilities.

from datetime import timedelta

from openbb_core.provider.utils.helpers import amake_request

HEADERS = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0",  # noqa
"Accept": "*/*",
"Accept-Language": "en-US,en;q=0.9",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"Connection": "keep-alive",
}


def date_range(start_date, end_date):
Yield dates between start_date and end_date.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`date_range`, `get_seekingalpha_id`

**Imports** (4):
`datetime`, `timedelta`, `openbb_core.provider.utils.helpers`, `amake_request`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:41.661280
- Generator: World's Best Repo Book Generator v1.0.0
