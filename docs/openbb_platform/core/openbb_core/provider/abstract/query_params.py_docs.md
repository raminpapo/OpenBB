# File Documentation: query_params.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/abstract/query_params.py`
- **Size**: 2,696 bytes
- **Lines**: 72
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""The OpenBB Standardized QueryParams Model that holds the query input parameters."""

from typing import Any

from pydantic import BaseModel, ConfigDict


class QueryParams(BaseModel):
    """The OpenBB Standardized QueryParams Model.

    The `QueryParams` class is designed to hold query parameters, to be extended by
    providers and to be used by fetchers when making data provider requests.

    Key Features:
    - Alias handling: Utilizes an aliasing mechanism to maintain compatibility with different naming
        conventions across various data formats. The alias is only applied when running `model_dump`.
    - Json schema extra merging:

        Merge different json schema extra, identified by provider.
        Example:
            FMP fetcher:
                __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}
            Intrinio fetcher
                __json_schema_extra__ = {"symbol": {"multiple_items_allowed": False}}

            Creates new fields in the `symbol` schema:
            {
                "type": "string",
                "description": "Symbol to get data for.",
                "fmp": {"multiple_items_allowed": True},
                "intrinio": {"multiple_items_allowed": False}
                ...,
            }

        Multiple fields can be tagged with the same or multiple properties.
        Example:
        __json_schema_extra__ = {
            "<field_name_A>": {"foo": 123, "bar": 456},
            "<field_name_B>": {"foo": 789}
        }

    Attributes:
    __alias_dict__ (Dict[str, str]):
        A dictionary that maps field names to their aliases,
        facilitating the use of different naming conventions.
    __json_schema_extra__ (Dict[str, List[str]]):
        Properties to be included in the json schema extra.
    model_config (ConfigDict):
        A configuration dictionary that defines the model's behavior,
        such as accepting extra fields, populating by name, and alias
        generation.
    """

    __alias_dict__: dict[str, str] = {}
    __json_schema_extra__: dict[str, Any] = {}

    def __repr__(self):
        """Return the string representation of the QueryParams object."""
        return f"{self.__class__.__name__}({', '.join([f'{k}={v}' for k, v in self.model_dump().items()])})"

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    def model_dump(self, *args, **kwargs):
        """Dump the model."""
        original = super().model_dump(*args, **kwargs)
        if self.__alias_dict__:
            return {
                self.__alias_dict__.get(key, key): value
                for key, value in original.items()
            }
        return original

```



---

## High-Level Overview

This is a **python** file named `query_params.py`.

**Python Module**

- **Classes** (2): QueryParams, is
- **Functions** (2): __repr__, model_dump
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`QueryParams`**(BaseModel)

#### Functions

- **`__repr__(self)`**
- **`model_dump(self, *args, **kwargs)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `BaseModel`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.336313Z
**Generator**: World's Best Repo Book Generator v1.0
