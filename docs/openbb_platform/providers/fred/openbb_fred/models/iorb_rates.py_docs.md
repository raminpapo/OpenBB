# Documentation: openbb_platform/providers/fred/openbb_fred/models/iorb_rates.py

## File Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/iorb_rates.py`
- **Size**: 1,727 characters, 63 lines
- **Words**: 146
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FRED IORB Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.iorb_rates import (
    IORBData,
    IORBQueryParams,
)
from pydantic import field_validator


class FREDIORBQueryParams(IORBQueryParams):
    """FRED IORB Query."""


class FREDIORBData(IORBData):
    """FRED IORB Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDIORBFetcher(Fetcher[FREDIORBQueryParams, list[FREDIORBData]]):
    """FRED IORB Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FREDIORBQueryParams:
        """Transform query."""
        return FREDIORBQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FREDIORBQueryParams, credentials: dict[str, str] | None, **kwargs: Any
    ) -> dict:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_fred.utils.fred_base import Fred

        key = credentials.get("fred_api_key") if credentials else ""
        fred_series = "IORB"
        fred = Fred(key)
        data = fred.get_series(fred_series, query.start_date, query.end_date, **kwargs)
        return data

    @staticmethod
    def transform_data(
        query: FREDIORBQueryParams, data: dict, **kwargs: Any
    ) -> list[FREDIORBData]:
        """Transform data."""
        keys = ["date", "value"]
        return [FREDIORBData(**{k: x[k] for k in keys}) for x in data]

```

## High-Level Overview

FRED IORB Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.iorb_rates import (
IORBData,
IORBQueryParams,
)
from pydantic import field_validator


class FREDIORBQueryParams(IORBQueryParams):
FRED IORB Query.
FRED IORB Data.

__alias_dict__ = {"rate": "value"}


## Detailed Structure

### Python File Structure

**Classes** (3):
`FREDIORBQueryParams`, `FREDIORBData`, `FREDIORBFetcher`

**Functions** (4):
`value_validate`, `transform_query`, `extract_data`, `transform_data`

**Imports** (9):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.iorb_rates`, `pydantic`, `field_validator`, `openbb_fred.utils.fred_base`, `Fred`


## Key Components

**Class `FREDIORBQueryParams`**: FRED IORB Query.

**Class `FREDIORBData`**: FRED IORB Data.

**Class `FREDIORBFetcher`**: FRED IORB Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.iorb_rates`
- `pydantic`
- `openbb_fred.utils.fred_base`

## Notes
- Generated: 2025-11-18T07:54:39.680897
- Generator: World's Best Repo Book Generator v1.0.0
