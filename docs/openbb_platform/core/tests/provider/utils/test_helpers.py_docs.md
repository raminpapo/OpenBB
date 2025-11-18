# Documentation: openbb_platform/core/tests/provider/utils/test_helpers.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/utils/test_helpers.py`
- **Size**: 4,008 characters, 144 lines
- **Words**: 295
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the provider helpers."""

import pytest
from openbb_core.provider.utils.client import ClientSession
from openbb_core.provider.utils.helpers import (
    amake_request,
    amake_requests,
    get_querystring,
    get_requests_session,
    make_request,
    to_snake_case,
)

# pylint: disable=unused-argument


class MockResponse:
    """Mock the response."""

    def __init__(self):
        """Initialize the mock response."""
        self.status_code = 200
        self.status = 200

    async def json(self):
        """Return the json response."""
        return {"test": "test"}


class MockSession:
    """Mock the ClientSession."""

    def __init__(self):
        """Initialize the mock session."""
        self.response = MockResponse()

    async def request(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Mock the ClientSession.request method."""
        if kwargs.get("raise_for_status", False):
            raise Exception("Test")

        return self.response

    @staticmethod
    async def mock_callback(response, session):
        """Mock the response_callback."""
        assert response.status == 200
        return await response.json()


def test_get_querystring_exclude():
    """Test the get_querystring helper."""
    items = {
        "key1": "value1",
        "key2": "value2",
        "key3": None,
        "key4": ["value3", "value4"],
    }
    exclude = ["key2"]

    querystring = get_querystring(items, exclude)
    assert querystring == "key1=value1&key4=value3&key4=value4"


def test_get_querystring_no_exclude():
    """Test the get_querystring helper with no exclude list."""
    items = {
        "key1": "value1",
        "key2": "value2",
        "key3": None,
        "key4": ["value3", "value4"],
    }

    querystring = get_querystring(items, [])
    assert querystring == "key1=value1&key2=value2&key4=value3&key4=value4"


def test_make_request(monkeypatch):
    """Test the make_request helper."""

    def mock_get(*args, **kwargs):
        """Mock the requests.get method."""
        return MockResponse()

    client_session = get_requests_session()
    monkeypatch.setattr(client_session, "get", mock_get)

    response = make_request("http://mock.url", session=client_session)
    assert response.status_code == 200

    with pytest.raises(ValueError):
        make_request("http://mock.url", method="PUT")


def test_to_snake_case():
    """Test the to_snake_case helper."""
    assert to_snake_case("SomeRandomString") == "some_random_string"
    assert to_snake_case("someRandomString") == "some_random_string"
    assert to_snake_case("already_snake_case") == "already_snake_case"


@pytest.mark.asyncio
async def test_amake_request(monkeypatch):
    """Test the amake_request helper."""

    mock_callback = MockSession.mock_callback

    client_session = MockSession()
    monkeypatch.setattr(ClientSession, "request", client_session.request)

    response = await amake_request("http://mock.url", response_callback=mock_callback)
    assert response == {"test": "test"}

    with pytest.raises(Exception):
        await amake_request(
            "http://mock.url",
            response_callback=mock_callback,
            raise_for_status=True,
        )

    with pytest.raises(ValueError):
        await amake_request("http://mock.url", method="PUT")  # type: ignore[arg-type]


@pytest.mark.asyncio
async def test_amake_requests(monkeypatch):
    """Test the amake_requests helper."""

    mock_callback = MockSession.mock_callback

    client_session = MockSession()
    monkeypatch.setattr(ClientSession, "request", client_session.request)

    multi_response = await amake_requests(
        ["http://mock.url", "http://mock.url"],
        response_callback=mock_callback,
    )
    assert multi_response == [{"test": "test"}, {"test": "test"}]

    with pytest.raises(ValueError):
        await amake_requests(
            ["http://mock.url", "http://mock.url"], method="PUT", raise_for_status=True
        )

```

## High-Level Overview

Test the provider helpers.

import pytest
from openbb_core.provider.utils.client import ClientSession
from openbb_core.provider.utils.helpers import (
amake_request,
amake_requests,
get_querystring,
get_requests_session,
make_request,
to_snake_case,
)

# pylint: disable=unused-argument


class MockResponse:
Mock the response.
Initialize the mock response.
self.status_code = 200

## Detailed Structure

### Python File Structure

**Classes** (2):
`MockResponse`, `MockSession`

**Functions** (12):
`__init__`, `json`, `__init__`, `request`, `mock_callback`, `test_get_querystring_exclude`, `test_get_querystring_no_exclude`, `test_make_request`, `mock_get`, `test_to_snake_case`, `test_amake_request`, `test_amake_requests`

**Imports** (4):
`pytest`, `openbb_core.provider.utils.client`, `ClientSession`, `openbb_core.provider.utils.helpers`


## Key Components

**Class `MockResponse`**: Mock the response.

**Class `MockSession`**: Mock the ClientSession.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.provider.utils.client`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:35.890158
- Generator: World's Best Repo Book Generator v1.0.0
