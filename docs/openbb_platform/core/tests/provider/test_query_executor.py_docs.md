# Documentation: openbb_platform/core/tests/provider/test_query_executor.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/test_query_executor.py`
- **Size**: 4,454 characters, 123 lines
- **Words**: 328
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Query Executor."""

# pylint: disable=W0621

from unittest.mock import MagicMock, patch

import pytest
from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.provider import Provider
from openbb_core.provider.query_executor import QueryExecutor
from pydantic import SecretStr


@pytest.fixture
def mock_query_executor():
    """Mock the query executor."""
    registry = MagicMock()
    registry.providers = {
        "test_provider": Provider(
            name="Test",
            description="Test provider",
            fetcher_dict={"test_fetcher": Fetcher},
        ),
    }
    executor = QueryExecutor(registry=registry)
    return executor


def test_get_provider_success(mock_query_executor):
    """Test if the method can retrieve a provider successfully."""
    provider = mock_query_executor.get_provider("test_provider")
    assert provider.name == "Test"


def test_get_provider_failure(mock_query_executor):
    """Test if the method fails properly when the provider does not exist."""
    with pytest.raises(OpenBBError, match="Provider 'nonexistent' not found"):
        mock_query_executor.get_provider("nonexistent")


def test_get_fetcher_success(mock_query_executor):
    """Test if the method can retrieve a fetcher successfully."""
    provider = mock_query_executor.get_provider("test_provider")
    fetcher = mock_query_executor.get_fetcher(provider, "test_fetcher")
    assert issubclass(fetcher, Fetcher)


def test_get_fetcher_failure(mock_query_executor):
    """Test if the method fails properly when the fetcher does not exist."""
    provider = mock_query_executor.get_provider("test_provider")
    with pytest.raises(OpenBBError, match="Fetcher not found"):
        mock_query_executor.get_fetcher(provider, "nonexistent_fetcher")


def test_filter_credentials_success(mock_query_executor):
    """Test if credentials are properly filtered."""
    provider = mock_query_executor.get_provider("test_provider")
    provider.credentials = ["test_provider_api_key"]
    credentials = {
        "test_provider_api_key": SecretStr("12345"),
        "other_api_key": SecretStr("12345"),
    }

    filtered_credentials = mock_query_executor.filter_credentials(
        credentials, provider, True
    )

    assert filtered_credentials == {"test_provider_api_key": "12345"}


def test_filter_credentials_missing_require(mock_query_executor):
    """Test if the proper error is raised when a credential is missing."""
    provider = mock_query_executor.get_provider("test_provider")
    provider.credentials = ["test_provider_api_key"]
    credentials = {"other_api_key": SecretStr("12345")}

    with pytest.raises(OpenBBError, match="Missing credential"):
        mock_query_executor.filter_credentials(credentials, provider, True)


def test_filter_credentials_empty_require(mock_query_executor):
    """Test if the proper error is raised when a credential is missing."""
    provider = mock_query_executor.get_provider("test_provider")
    provider.credentials = ["test_provider_api_key"]
    credentials = {
        "test_provider_api_key": SecretStr(""),
        "other_api_key": SecretStr("12345"),
    }

    with pytest.raises(OpenBBError, match="Missing credential"):
        mock_query_executor.filter_credentials(credentials, provider, True)


def test_filter_credentials_missing_dont_require(mock_query_executor):
    """Test if the proper error is raised when a credential is missing."""
    provider = mock_query_executor.get_provider("test_provider")
    provider.credentials = ["test_provider_api_key"]
    credentials = {"other_api_key": SecretStr("12345")}

    filtered_credentials = mock_query_executor.filter_credentials(
        credentials, provider, False
    )

    assert filtered_credentials == {}


@pytest.mark.asyncio
async def test_execute_success(mock_query_executor: QueryExecutor):
    """Test if the method can execute a query successfully."""
    mock_result = {"data": "test_data"}

    params = {"param1": "value1"}
    credentials = {"api_key": SecretStr("12345")}

    with patch.object(Fetcher, "fetch_data", return_value=mock_result) as mock_fetch:
        result = await mock_query_executor.execute(
            "test_provider", "test_fetcher", params, credentials
        )

        assert result == mock_result
        mock_fetch.assert_called_once_with(params, {}, **{})

```

## High-Level Overview

Test the Query Executor.

# pylint: disable=W0621

from unittest.mock import MagicMock, patch

import pytest
from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.provider import Provider
from openbb_core.provider.query_executor import QueryExecutor
from pydantic import SecretStr


@pytest.fixture
def mock_query_executor():
Mock the query executor.
Test if the method can retrieve a provider successfully.
provider = mock_query_executor.get_provider("test_provider")
assert provider.name == "Test"

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (10):
`mock_query_executor`, `test_get_provider_success`, `test_get_provider_failure`, `test_get_fetcher_success`, `test_get_fetcher_failure`, `test_filter_credentials_success`, `test_filter_credentials_missing_require`, `test_filter_credentials_empty_require`, `test_filter_credentials_missing_dont_require`, `test_execute_success`

**Imports** (13):
`unittest.mock`, `MagicMock`, `pytest`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.abstract.provider`, `Provider`, `openbb_core.provider.query_executor`, `QueryExecutor`, `pydantic`, `SecretStr`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `pytest`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.abstract.provider`
- `openbb_core.provider.query_executor`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.881994
- Generator: World's Best Repo Book Generator v1.0.0
