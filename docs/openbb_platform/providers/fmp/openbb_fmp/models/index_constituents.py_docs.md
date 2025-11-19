# File Documentation: index_constituents.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/index_constituents.py`
- **Size**: 5,005 bytes
- **Lines**: 154
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP Index Constituents Model."""

# pylint: disable=unused-argument

from datetime import (
    date as dateType,
    datetime,
)
from typing import Any, Literal

from dateutil import parser
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_constituents import (
    IndexConstituentsData,
    IndexConstituentsQueryParams,
)
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field, field_validator


class FMPIndexConstituentsQueryParams(IndexConstituentsQueryParams):
    """FMP Index Constituents Query.

    Source: https://site.financialmodelingprep.com/developer/docs#sp-500
    """

    symbol: Literal["dowjones", "sp500", "nasdaq"] = Field(
        default="dowjones",
    )
    historical: bool = Field(
        default=False,
        description="Flag to retrieve historical removals and additions.",
    )


class FMPIndexConstituentsData(IndexConstituentsData):
    """FMP Index Constituents Data."""

    __alias_dict__ = {
        "headquarter": "headQuarter",
        "date_added": "dateFirstAdded",
        "industry": "subSector",
        "name": "addedSecurity",
        "removed_symbol": "removedTicker",
        "removed_name": "removedSecurity",
    }

    sector: str | None = Field(
        default=None,
        description="Sector classification for the constituent company in the index.",
    )
    industry: str | None = Field(
        default=None,
        description="Industry classification for the constituent company in the index.",
    )
    headquarter: str | None = Field(
        default=None,
        description="Location of the company's headquarters.",
    )
    date_added: dateType | str | None = Field(
        default=None, description="Date the constituent company was added to the index."
    )
    cik: str | None = Field(
        description=DATA_DESCRIPTIONS.get("cik", ""),
        default=None,
        coerce_numbers_to_str=True,
    )
    founded: dateType | str | None = Field(
        default=None,
        description="When the company was founded.",
    )
    removed_symbol: str | None = Field(
        default=None,
        description="Symbol of the company removed from the index.",
    )
    removed_name: str | None = Field(
        default=None,
        description="Name of the company removed from the index.",
    )
    reason: str | None = Field(
        default=None,
        description="Reason for the removal from the index.",
    )
    date: dateType | None = Field(
        default=None,
        description="Date of the historical constituent data.",
    )

    @field_validator("date_added", "founded", "date", mode="before", check_fields=False)
    @classmethod
    def date_first_added_validate(cls, v):
        """Return the date_first_added date as a datetime object for valid cases."""
        if not v:
            return None

        try:
            # First try ISO format for performance
            return datetime.fromisoformat(str(v)).date()
        except (ValueError, TypeError):
            try:
                # Fall back to dateutil parser for flexible parsing
                return parser.parse(str(v)).date()
            except Exception:
                # Return as string if all parsing fails
                return str(v)

    @field_validator(
        "removed_symbol", "removed_name", "reason", mode="before", check_fields=False
    )
    @classmethod
    def _clean_empty_strings(cls, v):  # pylint: disable=E0213
        """Return the removed fields as strings."""
        if not v or v in ("''", "", "None"):
            return None
        return v


class FMPIndexConstituentsFetcher(
    Fetcher[
        FMPIndexConstituentsQueryParams,
        list[FMPIndexConstituentsData],
    ]
):
    """FMP Index Constituents Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPIndexConstituentsQueryParams:
        """Transform the query params."""
        return FMPIndexConstituentsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPIndexConstituentsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/stable"
        url = f"{base_url}/{'historical-' if query.historical else ''}{query.symbol}-constituent/?apikey={api_key}"

        return await get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPIndexConstituentsQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPIndexConstituentsData]:
        """Transform the raw data into a list of FMPIndexConstituentsData."""
        return [FMPIndexConstituentsData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `index_constituents.py`.

**Python Module**

- **Classes** (3): FMPIndexConstituentsQueryParams, FMPIndexConstituentsData, FMPIndexConstituentsFetcher
- **Functions** (5): date_first_added_validate, _clean_empty_strings, transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPIndexConstituentsQueryParams`**(IndexConstituentsQueryParams)
- **`FMPIndexConstituentsData`**(IndexConstituentsData)
- **`FMPIndexConstituentsFetcher`**(
    Fetcher[
        FMPIndexConstituentsQueryParams,
        list[FMPIndexConstituentsData],
    ]
)

#### Functions

- **`date_first_added_validate(cls, v)`**
- **`_clean_empty_strings(cls, v)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `DATA_DESCRIPTIONS`
- `Fetcher`
- `Field`
- `datetime`
- `dateutil`
- `get_data_many`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.index_constituents`
- `openbb_core.provider.utils.descriptions`
- `openbb_fmp.utils.helpers`
- `parser`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.664292Z
**Generator**: World's Best Repo Book Generator v1.0
