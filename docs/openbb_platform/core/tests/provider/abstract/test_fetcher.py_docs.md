# Documentation: openbb_platform/core/tests/provider/abstract/test_fetcher.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/abstract/test_fetcher.py`
- **Size**: 1,985 characters, 69 lines
- **Words**: 180
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Fetcher."""

from typing import Any

import pytest
from openbb_core.provider.abstract.fetcher import Data, Fetcher, QueryParams

# Step 1: Create a dummy subclass of Fetcher


class MockData(Data):
    """Mock data class."""


class MockQueryParams(QueryParams):
    """Mock query params class."""


class MockFetcher(Fetcher[MockQueryParams, list[MockData]]):
    """Mock fetcher class."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> MockQueryParams:
        """Transform the params to the provider-specific query."""
        return MockQueryParams()

    @staticmethod
    def extract_data(query: MockQueryParams, credentials: dict[str, str] | None) -> Any:
        """Extract the data from the provider."""
        return [{"mock_key": "mock_value"}]  # Mocking a data response

    @staticmethod
    def transform_data(query: MockQueryParams, data: Any, **kwargs) -> list[MockData]:
        """Transform the provider-specific data."""
        return [MockData(**item) for item in data]


@pytest.mark.asyncio
async def test_fetcher_methods():
    """Test the Fetcher abstract methods using a mock Fetcher subclass."""
    params = {"param1": "value1"}
    mock_fetcher = MockFetcher()

    fetched_data = await mock_fetcher.fetch_data(params=params)
    assert isinstance(fetched_data, list)
    assert isinstance(fetched_data[0], MockData)
    assert fetched_data[0].model_dump() == {"mock_key": "mock_value"}


def test_fetcher_query_params_type():
    """Test the query_params_type classproperty."""
    assert MockFetcher.query_params_type == MockQueryParams


def test_fetcher_return_type():
    """Test the return_type classproperty."""
    assert MockFetcher.return_type == list[MockData]


def test_fetcher_data_type():
    """Test the data_type classproperty."""
    assert MockFetcher.data_type == MockData


def test_fetcher_test():
    """Test the test method."""
    tested = MockFetcher.test(params={})
    assert tested is None

```

## High-Level Overview

Test the Fetcher.

from typing import Any

import pytest
from openbb_core.provider.abstract.fetcher import Data, Fetcher, QueryParams

# Step 1: Create a dummy subclass of Fetcher


class MockData(Data):
Mock data class.
Mock query params class.


class MockFetcher(Fetcher[MockQueryParams, list[MockData]]):
Mock fetcher class.
Transform the params to the provider-specific query.
return MockQueryParams()


## Detailed Structure

### Python File Structure

**Classes** (4):
`of`, `MockData`, `MockQueryParams`, `MockFetcher`

**Functions** (8):
`transform_query`, `extract_data`, `transform_data`, `test_fetcher_methods`, `test_fetcher_query_params_type`, `test_fetcher_return_type`, `test_fetcher_data_type`, `test_fetcher_test`

**Imports** (6):
`typing`, `Any`, `pytest`, `openbb_core.provider.abstract.fetcher`, `Data`, `the`


## Key Components

**Class `of`**: Mock data class.

**Class `MockQueryParams`**: Mock query params class.

**Class `MockFetcher`**: Mock fetcher class.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `pytest`
- `openbb_core.provider.abstract.fetcher`

## Notes
- Generated: 2025-11-18T07:54:35.876918
- Generator: World's Best Repo Book Generator v1.0.0
