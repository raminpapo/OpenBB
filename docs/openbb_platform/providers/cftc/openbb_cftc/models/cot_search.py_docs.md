# Documentation: openbb_platform/providers/cftc/openbb_cftc/models/cot_search.py

## File Metadata
- **Path**: `openbb_platform/providers/cftc/openbb_cftc/models/cot_search.py`
- **Size**: 2,923 characters, 91 lines
- **Words**: 203
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""CFTC Commitment of Traders Reports Search Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cot_search import (
    CotSearchData,
    CotSearchQueryParams,
)
from pydantic import Field


class CftcCotSearchQueryParams(CotSearchQueryParams):
    """CFTC Commitment of Traders Reports Search Query.

    Source: https://publicreporting.cftc.gov/stories/s/r4w3-av2u
    """


class CftcCotSearchData(CotSearchData):
    """CFTC Commitment of Traders Reports Search Data."""

    __alias_dict__ = {
        "code": "cftc_contract_market_code",
        "name": "contract_market_name",
        "category": "commodity_group_name",
        "subcategory": "commodity_subgroup_name",
    }

    commodity: str | None = Field(default=None, description="Name of the commodity.")


class CftcCotSearchFetcher(Fetcher[CftcCotSearchQueryParams, list[CftcCotSearchData]]):
    """CFTC COT Search Fetcher."""

    require_credentials = False

    @staticmethod
    def transform_query(params: dict[str, Any]) -> CftcCotSearchQueryParams:
        """Transform the query params."""
        return CftcCotSearchQueryParams(**params)

    @staticmethod
    def extract_data(
        query: CftcCotSearchQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Search a curated list of CFTC Commitment of Traders Reports."""
        # pylint: disable=import-outside-toplevel
        from importlib.resources import files  # noqa
        from pathlib import Path
        from pandas import read_json

        assets_path = Path(str(files("openbb_cftc").joinpath("assets")))

        with open(assets_path.joinpath("cot_ids.json"), encoding="utf-8") as f:
            available_cot = read_json(f)

        query_string = query.query  # noqa
        return (
            available_cot[
                available_cot["contract_market_name"].str.contains(
                    query_string, case=False
                )
                | available_cot["cftc_contract_market_code"].str.contains(
                    query_string, case=False
                )
                | available_cot["commodity_name"].str.contains(query_string, case=False)
                | available_cot["commodity_group_name"].str.contains(
                    query_string, case=False
                )
                | available_cot["commodity_subgroup_name"].str.contains(
                    query_string, case=False
                )
            ]
            .reset_index(drop=True)
            .to_dict("records")
        )

    @staticmethod
    def transform_data(
        query: CotSearchQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[CftcCotSearchData]:
        """Transform the data."""
        return [CftcCotSearchData.model_validate(d) for d in data]

```

## High-Level Overview

CFTC Commitment of Traders Reports Search Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cot_search import (
CotSearchData,
CotSearchQueryParams,
)
from pydantic import Field


class CftcCotSearchQueryParams(CotSearchQueryParams):
CFTC Commitment of Traders Reports Search Query.



class CftcCotSearchData(CotSearchData):

## Detailed Structure

### Python File Structure

**Classes** (3):
`CftcCotSearchQueryParams`, `CftcCotSearchData`, `CftcCotSearchFetcher`

**Functions** (3):
`transform_query`, `extract_data`, `transform_data`

**Imports** (13):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.cot_search`, `pydantic`, `Field`, `importlib.resources`, `files`, `pathlib`, `Path`, `pandas`, `read_json`


## Key Components

**Class `CftcCotSearchQueryParams`**: CFTC Commitment of Traders Reports Search Query.

    Source: https://publicreporting.cftc.gov/stories/s/r4w3-av2u

**Class `CftcCotSearchData`**: CFTC Commitment of Traders Reports Search Data.

**Class `CftcCotSearchFetcher`**: CFTC COT Search Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.cot_search`
- `pydantic`
- `importlib.resources`
- `pathlib`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:37.577072
- Generator: World's Best Repo Book Generator v1.0.0
