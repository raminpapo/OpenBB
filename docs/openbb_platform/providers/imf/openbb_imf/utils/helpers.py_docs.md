# Documentation: openbb_platform/providers/imf/openbb_imf/utils/helpers.py

## File Metadata
- **Path**: `openbb_platform/providers/imf/openbb_imf/utils/helpers.py`
- **Size**: 1,184 characters, 35 lines
- **Words**: 120
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""IMF Helper Utilities."""


async def get_data(url: str) -> list[dict]:
    """Get data from the IMF API."""
    # pylint: disable=import-outside-toplevel

    from aiohttp.client_exceptions import ContentTypeError  # noqa
    from json.decoder import JSONDecodeError
    from openbb_core.provider.utils.helpers import amake_request
    from openbb_core.app.model.abstract.error import OpenBBError

    try:
        response = await amake_request(url, timeout=20)
    except (JSONDecodeError, ContentTypeError) as e:
        raise OpenBBError(
            "Error fetching data; This might be rate-limiting. Try again later."
        ) from e

    if "ErrorDetails" in response:
        raise OpenBBError(
            f"{response['ErrorDetails'].get('Code')} -> {response['ErrorDetails'].get('Message')}"  # type: ignore
        )

    series = response.get("CompactData", {}).get("DataSet", {}).pop("Series", {})  # type: ignore

    if not series:
        raise OpenBBError(f"No time series data found -> {response}")

    # If there is only one series, they ruturn a dict instead of a list.
    if series and isinstance(series, dict):
        series = [series]

    return series

```

## High-Level Overview

IMF Helper Utilities.


async def get_data(url: str) -> list[dict]:
Get data from the IMF API.
pylint: disable=import-outside-toplevel
If there is only one series, they ruturn a dict instead of a list.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`get_data`

**Imports** (10):
`the`, `aiohttp.client_exceptions`, `ContentTypeError`, `json.decoder`, `JSONDecodeError`, `openbb_core.provider.utils.helpers`, `amake_request`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `e`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `aiohttp.client_exceptions`
- `json.decoder`
- `openbb_core.provider.utils.helpers`
- `openbb_core.app.model.abstract.error`

## Notes
- Generated: 2025-11-18T07:54:40.024582
- Generator: World's Best Repo Book Generator v1.0.0
