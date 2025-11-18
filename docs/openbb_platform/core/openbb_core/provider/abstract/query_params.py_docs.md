# Documentation: openbb_platform/core/openbb_core/provider/abstract/query_params.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/abstract/query_params.py`
- **Size**: 2,696 characters, 72 lines
- **Words**: 268
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

The OpenBB Standardized QueryParams Model that holds the query input parameters.

from typing import Any

from pydantic import BaseModel, ConfigDict


class QueryParams(BaseModel):
The OpenBB Standardized QueryParams Model.

## Detailed Structure

### Python File Structure

**Classes** (2):
`QueryParams`, `is`

**Functions** (2):
`__repr__`, `model_dump`

**Imports** (4):
`typing`, `Any`, `pydantic`, `BaseModel`


## Key Components

**Class `QueryParams`**: The OpenBB Standardized QueryParams Model.

    The `QueryParams` class is designed to hold query parameters, to be extended by
    providers and to be used by fetchers when making data provider reque

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.515761
- Generator: World's Best Repo Book Generator v1.0.0
