# Documentation: openbb_platform/core/openbb_core/provider/standard_models/search_financial_attributes.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/search_financial_attributes.py`
- **Size**: 1,709 characters, 45 lines
- **Words**: 173
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Search Financial Attributes Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class SearchFinancialAttributesQueryParams(QueryParams):
    """Search Financial Attributes Query."""

    query: str = Field(description="Query to search for.")
    limit: int | None = Field(default=1000, description=QUERY_DESCRIPTIONS.get("limit"))


class SearchFinancialAttributesData(Data):
    """Search Financial Attributes Data."""

    id: str = Field(description="ID of the financial attribute.")
    name: str = Field(description="Name of the financial attribute.")
    tag: str = Field(description="Tag of the financial attribute.")
    statement_code: str = Field(description="Code of the financial statement.")
    statement_type: str | None = Field(
        default=None, description="Type of the financial statement."
    )
    parent_name: str | None = Field(
        default=None, description="Parent's name of the financial attribute."
    )
    sequence: int | None = Field(
        default=None, description="Sequence of the financial statement."
    )
    factor: str | None = Field(
        default=None, description="Unit of the financial attribute."
    )
    transaction: str | None = Field(
        default=None,
        description="Transaction type (credit/debit) of the financial attribute.",
    )
    type: str | None = Field(
        default=None, description="Type of the financial attribute."
    )
    unit: str | None = Field(
        default=None, description="Unit of the financial attribute."
    )

```

## High-Level Overview

Search Financial Attributes Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class SearchFinancialAttributesQueryParams(QueryParams):
Search Financial Attributes Query.
Search Financial Attributes Data.

id: str = Field(description="ID of the financial attribute.")
name: str = Field(description="Name of the financial attribute.")
tag: str = Field(description="Tag of the financial attribute.")
statement_code: str = Field(description="Code of the financial statement.")
statement_type: str | None = Field(
default=None, description="Type of the financial statement."
)
parent_name: str | None = Field(

## Detailed Structure

### Python File Structure

**Classes** (2):
`SearchFinancialAttributesQueryParams`, `SearchFinancialAttributesData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `SearchFinancialAttributesQueryParams`**: Search Financial Attributes Query.

**Class `SearchFinancialAttributesData`**: Search Financial Attributes Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.730209
- Generator: World's Best Repo Book Generator v1.0.0
