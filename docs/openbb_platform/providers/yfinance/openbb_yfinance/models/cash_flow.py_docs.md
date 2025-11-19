# File Documentation: cash_flow.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/cash_flow.py`
- **Size**: 3,992 bytes
- **Lines**: 124
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Yahoo Finance Cash Flow Statement Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cash_flow import (
    CashFlowStatementData,
    CashFlowStatementQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class YFinanceCashFlowStatementQueryParams(CashFlowStatementQueryParams):
    """Yahoo Finance Cash Flow Statement Query.

    Source: https://finance.yahoo.com/
    """

    __json_schema_extra__ = {
        "period": {
            "choices": ["annual", "quarter"],
        }
    }

    period: Literal["annual", "quarter"] = Field(
        default="annual",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )
    limit: int | None = Field(
        default=5,
        description=QUERY_DESCRIPTIONS.get("limit", ""),
        le=5,
    )


class YFinanceCashFlowStatementData(CashFlowStatementData):
    """Yahoo Finance Cash Flow Statement Data."""

    __alias_dict__ = {
        "investments_in_property_plant_and_equipment": "purchase_of_ppe",
        "issuance_of_common_equity": "common_stock_issuance",
        "repurchase_of_common_equity": "common_stock_payments",
        "cash_dividends_paid": "payment_of_dividends",
        "net_change_in_cash_and_equivalents": "changes_in_cash",
    }

    @field_validator("period_ending", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):
        """Return datetime object from string."""
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S").date()
        return v


class YFinanceCashFlowStatementFetcher(
    Fetcher[
        YFinanceCashFlowStatementQueryParams,
        list[YFinanceCashFlowStatementData],
    ]
):
    """Yahoo Finance Cash Flow Statement Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFinanceCashFlowStatementQueryParams:
        """Transform the query parameters."""
        return YFinanceCashFlowStatementQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFinanceCashFlowStatementQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[YFinanceCashFlowStatementData]:
        """Extract the data from the Yahoo Finance endpoints."""
        # pylint: disable=import-outside-toplevel
        import json  # noqa
        from curl_adapter import CurlCffiAdapter
        from numpy import nan
        from openbb_core.provider.utils.errors import EmptyDataError
        from openbb_core.provider.utils.helpers import (
            get_requests_session,
            to_snake_case,
        )
        from yfinance import Ticker

        period = "yearly" if query.period == "annual" else "quarterly"  # type: ignore
        session = get_requests_session()
        session.mount("https://", CurlCffiAdapter())
        session.mount("http://", CurlCffiAdapter())

        data = Ticker(
            query.symbol,
            session=session,
        ).get_cash_flow(as_dict=False, pretty=False, freq=period)

        if data is None:
            raise EmptyDataError()

        if query.limit:
            data = data.iloc[:, : query.limit]

        data.index = [to_snake_case(i) for i in data.index]
        data = data.reset_index().sort_index(ascending=False).set_index("index")
        data = data.replace({nan: None}).to_dict()
        data = [{"period_ending": str(key), **value} for key, value in data.items()]

        data = json.loads(json.dumps(data))

        return data

    @staticmethod
    def transform_data(
        query: YFinanceCashFlowStatementQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFinanceCashFlowStatementData]:
        """Transform the data."""
        return [YFinanceCashFlowStatementData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `cash_flow.py`.

**Python Module**

- **Classes** (3): YFinanceCashFlowStatementQueryParams, YFinanceCashFlowStatementData, YFinanceCashFlowStatementFetcher
- **Functions** (4): date_validate, transform_query, extract_data, transform_data
- **Import Statements**: 5


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFinanceCashFlowStatementQueryParams`**(CashFlowStatementQueryParams)
- **`YFinanceCashFlowStatementData`**(CashFlowStatementData)
- **`YFinanceCashFlowStatementFetcher`**(
    Fetcher[
        YFinanceCashFlowStatementQueryParams,
        list[YFinanceCashFlowStatementData],
    ]
)

#### Functions

- **`date_validate(cls, v)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `CurlCffiAdapter`
- `EmptyDataError`
- `Fetcher`
- `Field`
- `QUERY_DESCRIPTIONS`
- `Ticker`
- `curl_adapter`
- `datetime`
- `json`
- `nan`
- `numpy`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.cash_flow`
- `openbb_core.provider.utils.descriptions`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.159447Z
**Generator**: World's Best Repo Book Generator v1.0
