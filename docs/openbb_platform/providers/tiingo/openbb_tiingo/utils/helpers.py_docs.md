# File Documentation: helpers.py

## Metadata
- **Path**: `openbb_platform/providers/tiingo/openbb_tiingo/utils/helpers.py`
- **Size**: 1,357 bytes
- **Lines**: 40
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Tiingo Helpers Module."""


async def get_data(url: str) -> dict | list:
    """Get data from Tiingo endpoint and parse the JSON response."""
    # pylint: disable=import-outside-toplevel
    from json import JSONDecodeError  # noqa
    from openbb_core.app.model.abstract.error import OpenBBError
    from openbb_core.provider.utils.errors import EmptyDataError, UnauthorizedError
    from openbb_core.provider.utils.helpers import amake_request

    response: dict | list | None = None

    try:
        response = await amake_request(url)
        if (
            response
            and isinstance(response, dict)
            and len(list(response.keys())) == 1
            and response.get("detail")
        ):
            if (
                "token" in response["detail"]
                or "access" in response["detail"]
                or "permission" in response["detail"]
                or "authorized" in response["detail"]
            ):
                raise UnauthorizedError(
                    f"Unauthorized Tiingo request -> {response['detail']}"
                )
            raise OpenBBError(response["detail"])

        if not response:
            raise EmptyDataError("The response is empty")

        return response

    except JSONDecodeError as e:
        raise OpenBBError(f"Failed to parse JSON response -> {e}") from e

```



---

## High-Level Overview

This is a **python** file named `helpers.py`.

**Python Module**

- **Functions** (1): get_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `EmptyDataError`
- `JSONDecodeError`
- `OpenBBError`
- `amake_request`
- `json`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:53.020408Z
**Generator**: World's Best Repo Book Generator v1.0
