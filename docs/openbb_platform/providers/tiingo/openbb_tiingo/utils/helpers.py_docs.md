# Documentation: openbb_platform/providers/tiingo/openbb_tiingo/utils/helpers.py

## File Metadata
- **Path**: `openbb_platform/providers/tiingo/openbb_tiingo/utils/helpers.py`
- **Size**: 1,357 characters, 40 lines
- **Words**: 121
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Tiingo Helpers Module.


async def get_data(url: str) -> dict | list:
Get data from Tiingo endpoint and parse the JSON response.
pylint: disable=import-outside-toplevel

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`get_data`

**Imports** (10):
`Tiingo`, `json`, `JSONDecodeError`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `openbb_core.provider.utils.helpers`, `amake_request`, `e`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `json`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:41.723529
- Generator: World's Best Repo Book Generator v1.0.0
