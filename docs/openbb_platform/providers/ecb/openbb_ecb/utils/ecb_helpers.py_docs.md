# Documentation: openbb_platform/providers/ecb/openbb_ecb/utils/ecb_helpers.py

## File Metadata
- **Path**: `openbb_platform/providers/ecb/openbb_ecb/utils/ecb_helpers.py`
- **Size**: 1,290 characters, 41 lines
- **Words**: 135
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ECB helpers"""


async def get_series_data(series_id: str, start_date: str = "", end_date: str = ""):
    """Get ECB data

    Parameters
    ----------
    series_id: str
        ECB ID of data
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    """
    # pylint: disable=import-outside-toplevel
    import json  # noqa
    from openbb_core.app.model.abstract.error import OpenBBError  # noqa
    from openbb_core.provider.utils.helpers import amake_request  # noqa

    start_date = start_date.replace("-", "")
    end_date = end_date.replace("-", "")
    url = f"https://data.ecb.europa.eu/data-detail-api/{series_id}"
    data: list = []  # type: ignore
    try:
        data = await amake_request(  # type: ignore
            url=url,
            params={"startPeriod": start_date, "endPeriod": end_date},
        )
    except KeyboardInterrupt as interrupt:
        raise interrupt
    except json.JSONDecodeError as exc:
        raise OpenBBError("Invalid JSON response from ECB") from exc

    if start_date:
        data = [item for item in data if item["PERIOD"][0] >= start_date]
    if end_date:
        data = [item for item in data if item["PERIOD"][0] <= end_date]

    return data

```

## High-Level Overview

ECB helpers


async def get_series_data(series_id: str, start_date: str = "", end_date: str = ""):
Get ECB data

# pylint: disable=import-outside-toplevel
import json  # noqa
from openbb_core.app.model.abstract.error import OpenBBError  # noqa
from openbb_core.provider.utils.helpers import amake_request  # noqa

start_date = start_date.replace("-", "")
end_date = end_date.replace("-", "")
url = f"https://data.ecb.europa.eu/data-detail-api/{series_id}"
data: list = []  # type: ignore
try:
data = await amake_request(  # type: ignore
url=url,
params={"startPeriod": start_date, "endPeriod": end_date},
)

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`get_series_data`

**Imports** (7):
`json`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.utils.helpers`, `amake_request`, `ECB`, `exc`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `json`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:37.692119
- Generator: World's Best Repo Book Generator v1.0.0
