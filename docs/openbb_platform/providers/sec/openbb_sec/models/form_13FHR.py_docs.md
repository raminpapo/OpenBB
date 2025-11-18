# Documentation: openbb_platform/providers/sec/openbb_sec/models/form_13FHR.py

## File Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/models/form_13FHR.py`
- **Size**: 3,341 characters, 108 lines
- **Words**: 277
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""SEC Form 13F-HR Model."""

# pylint: disable =unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.form_13FHR import (
    Form13FHRData,
    Form13FHRQueryParams,
)
from pydantic import Field


class SecForm13FHRQueryParams(Form13FHRQueryParams):
    """SEC Form 13F-HR Query Params.

    Source: https://www.sec.gov/Archives/edgar/data/
    """


class SecForm13FHRData(Form13FHRData):
    """SEC Form 13F-HR Data."""

    __alias_dict__ = {
        "issuer": "nameOfIssuer",
        "asset_class": "titleOfClass",
        "option_type": "putCall",
    }

    weight: float = Field(
        description="The weight of the security relative to the market value of all securities in the filing"
        + " , as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )


class SecForm13FHRFetcher(Fetcher[SecForm13FHRQueryParams, list[SecForm13FHRData]]):
    """SEC Form 13F-HR Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> SecForm13FHRQueryParams:
        """Transform the query."""
        return SecForm13FHRQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: SecForm13FHRQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the SEC endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        from openbb_core.app.model.abstract.error import OpenBBError
        from openbb_core.provider.utils.errors import EmptyDataError
        from openbb_sec.utils import parse_13f

        symbol = query.symbol
        urls: list = []
        cik = symbol.isnumeric()
        try:
            filings = (
                await parse_13f.get_13f_candidates(symbol=symbol)
                if cik is False
                else await parse_13f.get_13f_candidates(cik=symbol)
            )
            if query.limit and query.date is None:
                urls = filings.iloc[: query.limit].to_list()
            if query.date is not None:
                date = parse_13f.date_to_quarter_end(query.date.strftime("%Y-%m-%d"))
                filings.index = filings.index.astype(str)
                urls = [filings.loc[date]]

            results: list = []

            async def get_filing(url):
                """Get a single 13F-HR filing and parse it."""
                data = await parse_13f.parse_13f_hr(url)

                if len(data) > 0:
                    results.extend(data)

            await asyncio.gather(*[get_filing(url) for url in urls])

            if not results:
                raise EmptyDataError("No data was returned with the given parameters.")

            return results
        except OpenBBError as e:
            raise e from e

    @staticmethod
    def transform_data(
        query: SecForm13FHRQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[SecForm13FHRData]:
        """Transform the data."""
        return [
            SecForm13FHRData.model_validate(d)
            for d in sorted(
                data,
                key=lambda d: [d["period_ending"], d["weight"]],
                reverse=True,
            )
        ]

```

## High-Level Overview

SEC Form 13F-HR Model.

# pylint: disable =unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.form_13FHR import (
Form13FHRData,
Form13FHRQueryParams,
)
from pydantic import Field


class SecForm13FHRQueryParams(Form13FHRQueryParams):
SEC Form 13F-HR Query Params.



class SecForm13FHRData(Form13FHRData):

## Detailed Structure

### Python File Structure

**Classes** (3):
`SecForm13FHRQueryParams`, `SecForm13FHRData`, `SecForm13FHRFetcher`

**Functions** (4):
`transform_query`, `aextract_data`, `get_filing`, `transform_data`

**Imports** (16):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.form_13FHR`, `pydantic`, `Field`, `the`, `asyncio`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `openbb_sec.utils`, `parse_13f`, `e`


## Key Components

**Class `SecForm13FHRQueryParams`**: SEC Form 13F-HR Query Params.

    Source: https://www.sec.gov/Archives/edgar/data/

**Class `SecForm13FHRData`**: SEC Form 13F-HR Data.

**Class `SecForm13FHRFetcher`**: SEC Form 13F-HR Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.form_13FHR`
- `pydantic`
- `asyncio`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`
- `openbb_sec.utils`

## Notes
- Generated: 2025-11-18T07:54:40.591349
- Generator: World's Best Repo Book Generator v1.0.0
