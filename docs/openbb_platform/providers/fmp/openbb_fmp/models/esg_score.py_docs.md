# File Documentation: esg_score.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/esg_score.py`
- **Size**: 2,441 bytes
- **Lines**: 83
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP ESG Score Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.esg_score import (
    EsgScoreData,
    EsgScoreQueryParams,
)


class FMPEsgScoreQueryParams(EsgScoreQueryParams):
    """FMP ESG Score Query."""

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class FMPEsgScoreData(EsgScoreData):
    """FMP ESG Score Data."""

    __alias_dict__ = {
        "period_ending": "date",
        "disclosure_date": "acceptedDate",
        "esg_score": "ESGScore",
    }


class FMPEsgScoreFetcher(
    Fetcher[
        FMPEsgScoreQueryParams,
        list[FMPEsgScoreData],
    ]
):
    """FMP ESG Score Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPEsgScoreQueryParams:
        """Transform the query."""
        return FMPEsgScoreQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPEsgScoreQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        import warnings
        from openbb_core.provider.utils.errors import EmptyDataError
        from openbb_fmp.utils.helpers import get_data

        api_key = credentials.get("fmp_api_key") if credentials else ""
        symbols = query.symbol.split(",")
        results: list = []

        async def get_one(symbol):
            """Get data for one symbol."""
            url = f"https://financialmodelingprep.com/stable/esg-disclosures?symbol={symbol}&apikey={api_key}"
            result = await get_data(url, **kwargs)

            if not result:
                warnings.warn(f"Symbol Error: No data found for {symbol}")
            elif result:
                results.extend(result)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data found for the given symbols.")

        return sorted(results, key=lambda x: x.get("date", ""), reverse=True)

    @staticmethod
    def transform_data(
        query: FMPEsgScoreQueryParams, data: list, **kwargs: Any
    ) -> list[FMPEsgScoreData]:
        """Return the transformed data."""
        return [FMPEsgScoreData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `esg_score.py`.

**Python Module**

- **Classes** (3): FMPEsgScoreQueryParams, FMPEsgScoreData, FMPEsgScoreFetcher
- **Functions** (4): transform_query, aextract_data, get_one, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPEsgScoreQueryParams`**(EsgScoreQueryParams)
- **`FMPEsgScoreData`**(EsgScoreData)
- **`FMPEsgScoreFetcher`**(
    Fetcher[
        FMPEsgScoreQueryParams,
        list[FMPEsgScoreData],
    ]
)

#### Functions

- **`get_one(symbol)`**

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `EmptyDataError`
- `Fetcher`
- `asyncio`
- `get_data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.esg_score`
- `openbb_core.provider.utils.errors`
- `openbb_fmp.utils.helpers`
- `typing`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.626926Z
**Generator**: World's Best Repo Book Generator v1.0
