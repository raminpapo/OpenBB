# File Documentation: balance_of_payments.py

## Metadata
- **Path**: `openbb_platform/providers/ecb/openbb_ecb/models/balance_of_payments.py`
- **Size**: 3,593 bytes
- **Lines**: 118
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ECB Balance of Payments Model."""

# pylint: disable=unused-argument,too-many-ancestors

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.balance_of_payments import (
    BalanceOfPaymentsQueryParams,
    ECBCountry,
    ECBDirectInvestment,
    ECBInvestmentIncome,
    ECBMain,
    ECBOtherInvestment,
    ECBPortfolioInvestment,
    ECBServices,
    ECBSummary,
)
from openbb_ecb.utils.bps_series import (
    BPS_COUNTRIES,
    BPS_FREQUENCIES,
    BPS_REPORT_TYPES,
    generate_bps_series_ids,
)
from pydantic import Field


class ECBBalanceOfPaymentsQueryParams(BalanceOfPaymentsQueryParams):
    """ECB Balance of Payments Query."""

    report_type: BPS_REPORT_TYPES = Field(
        default="main",
        description="The report type, the level of detail in the data.",
    )
    frequency: BPS_FREQUENCIES = Field(
        default="monthly",
        description="The frequency of the data.  Monthly is valid only for ['main', 'summary'].",
    )
    country: BPS_COUNTRIES = Field(
        default=None,
        description="The country/region of the data.  This parameter will override the 'report_type' parameter.",
    )


class ECBBalanceOfPaymentsData(
    ECBMain,
    ECBSummary,
    ECBServices,
    ECBInvestmentIncome,
    ECBDirectInvestment,
    ECBPortfolioInvestment,
    ECBOtherInvestment,
    ECBCountry,
):
    """ECB Balance of Payments Data."""


class ECBBalanceOfPaymentsFetcher(
    Fetcher[ECBBalanceOfPaymentsQueryParams, list[ECBBalanceOfPaymentsData]]
):
    """Transform the query, extract and transform the data from the ECB endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> ECBBalanceOfPaymentsQueryParams:
        """Transform query."""
        return ECBBalanceOfPaymentsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: ECBBalanceOfPaymentsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        from openbb_ecb.utils.ecb_helpers import get_series_data  # noqa
        from pandas import DataFrame  # noqa

        results: list[dict] = []

        _series_ids = generate_bps_series_ids(
            query.frequency, query.report_type, country=query.country
        )
        names = list(_series_ids)
        series_ids = list(_series_ids.values())
        data: dict = {}

        async def get_one(series_id, name):
            result = {}
            temp = await get_series_data(series_id)
            result.update({name: {d["PERIOD"]: d["OBS_VALUE_AS_IS"] for d in temp}})
            data.update(result)

        await asyncio.gather(
            *[get_one(series_id, name) for series_id, name in zip(series_ids, names)]
        )

        try:
            results = (
                DataFrame(data)
                .sort_index()
                .reset_index()
                .rename(columns={"index": "period"})
                .to_dict("records")
            )
            return results
        except Exception as error:
            raise OpenBBError() from error

    @staticmethod
    def transform_data(
        query: ECBBalanceOfPaymentsQueryParams, data: list[dict], **kwargs: Any
    ) -> list[ECBBalanceOfPaymentsData]:
        """Transform and validate data through the model."""
        return [ECBBalanceOfPaymentsData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `balance_of_payments.py`.

**Python Module**

- **Classes** (3): ECBBalanceOfPaymentsQueryParams, ECBBalanceOfPaymentsData, ECBBalanceOfPaymentsFetcher
- **Functions** (4): transform_query, aextract_data, get_one, transform_data
- **Import Statements**: 5


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ECBBalanceOfPaymentsQueryParams`**(BalanceOfPaymentsQueryParams)
- **`ECBBalanceOfPaymentsData`**(
    ECBMain,
    ECBSummary,
    ECBServices,
    ECBInvestmentIncome,
    ECBDirectInvestment,
    ECBPortfolioInvestment,
    ECBOtherInvestment,
    ECBCountry,
)
- **`ECBBalanceOfPaymentsFetcher`**(
    Fetcher[ECBBalanceOfPaymentsQueryParams, list[ECBBalanceOfPaymentsData]]
)

#### Functions

- **`get_one(series_id, name)`**

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `DataFrame`
- `Fetcher`
- `Field`
- `OpenBBError`
- `asyncio`
- `get_series_data`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.balance_of_payments`
- `openbb_ecb.utils.bps_series`
- `openbb_ecb.utils.ecb_helpers`
- `pandas`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.790419Z
**Generator**: World's Best Repo Book Generator v1.0
