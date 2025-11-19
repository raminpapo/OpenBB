# File Documentation: test_query_params.py

## Metadata
- **Path**: `openbb_platform/core/tests/provider/abstract/test_query_params.py`
- **Size**: 993 bytes
- **Lines**: 31
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_query_params.py`.

**Python Module**

- **Classes** (1): AliasedQueryParams
- **Functions** (3): test_query_params_repr, test_query_params_no_alias, test_query_params_with_alias
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AliasedQueryParams`**(QueryParams)

#### Functions

- **`test_query_params_repr()`**
- **`test_query_params_no_alias()`**
- **`test_query_params_with_alias()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `QueryParams`
- `openbb_core.provider.abstract.query_params`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.715406Z
**Generator**: World's Best Repo Book Generator v1.0
