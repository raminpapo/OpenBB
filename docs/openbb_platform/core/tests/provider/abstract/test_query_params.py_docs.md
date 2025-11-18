# Documentation: openbb_platform/core/tests/provider/abstract/test_query_params.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/abstract/test_query_params.py`
- **Size**: 993 characters, 31 lines
- **Words**: 81
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test QueryParams."""

from openbb_core.provider.abstract.query_params import QueryParams


def test_query_params_repr():
    """Test the __repr__ method of QueryParams."""
    params = QueryParams(param1="value1", param2="value2")  # type: ignore[call-arg]
    assert "param1='value1'" in str(params)
    assert "param2='value2'" in str(params)


def test_query_params_no_alias():
    """Test model_dump without aliases."""
    params = QueryParams(param1="value1", param2="value2")  # type: ignore[call-arg]
    dumped_params = params.model_dump()

    assert dumped_params == {"param1": "value1", "param2": "value2"}


def test_query_params_with_alias():
    """Test model_dump with aliases."""

    class AliasedQueryParams(QueryParams):
        __alias_dict__ = {"param1": "alias1"}

    params = AliasedQueryParams(param1="value1", param2="value2")  # type: ignore[call-arg]
    dumped_params = params.model_dump()

    assert dumped_params == {"alias1": "value1", "param2": "value2"}

```

## High-Level Overview

Test QueryParams.

from openbb_core.provider.abstract.query_params import QueryParams


def test_query_params_repr():
Test the __repr__ method of QueryParams.
Test model_dump without aliases.
params = QueryParams(param1="value1", param2="value2")  # type: ignore[call-arg]
dumped_params = params.model_dump()

assert dumped_params == {"param1": "value1", "param2": "value2"}


def test_query_params_with_alias():
Test model_dump with aliases.

## Detailed Structure

### Python File Structure

**Classes** (1):
`AliasedQueryParams`

**Functions** (3):
`test_query_params_repr`, `test_query_params_no_alias`, `test_query_params_with_alias`

**Imports** (2):
`openbb_core.provider.abstract.query_params`, `QueryParams`


## Key Components

**Class `AliasedQueryParams`**: No documentation

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.query_params`

## Notes
- Generated: 2025-11-18T07:54:35.879339
- Generator: World's Best Repo Book Generator v1.0.0
