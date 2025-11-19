# File Documentation: ecb_helpers.py

## Metadata
- **Path**: `openbb_platform/providers/ecb/openbb_ecb/utils/ecb_helpers.py`
- **Size**: 1,290 bytes
- **Lines**: 41
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `ecb_helpers.py`.

**Python Module**

- **Functions** (1): get_series_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`get_series_data(series_id: str, start_date: str = "", end_date: str = "")`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `OpenBBError`
- `amake_request`
- `json`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.helpers`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.800356Z
**Generator**: World's Best Repo Book Generator v1.0
