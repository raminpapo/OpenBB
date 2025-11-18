# Documentation: openbb_platform/providers/yfinance/openbb_yfinance/models/balance_sheet.py

## File Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/balance_sheet.py`
- **Size**: 4,023 characters, 125 lines
- **Words**: 296
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Yahoo Finance Balance Sheet Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.balance_sheet import (
    BalanceSheetData,
    BalanceSheetQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class YFinanceBalanceSheetQueryParams(BalanceSheetQueryParams):
    """Yahoo Finance Balance Sheet Query.

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


class YFinanceBalanceSheetData(BalanceSheetData):
    """Yahoo Finance Balance Sheet Data."""

    __alias_dict__ = {
        "short_term_investments": "other_short_term_investments",
        "net_receivables": "receivables",
        "inventories": "inventory",
        "total_current_assets": "current_assets",
        "plant_property_equipment_gross": "gross_ppe",
        "plant_property_equipment_net": "net_ppe",
        "total_common_equity": "stockholders_equity",
        "total_equity_non_controlling_interests": "total_equity_gross_minority_interest",
    }

    @field_validator("period_ending", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return datetime object from string."""
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S").date()
        return v


class YFinanceBalanceSheetFetcher(
    Fetcher[
        YFinanceBalanceSheetQueryParams,
        list[YFinanceBalanceSheetData],
    ]
):
    """Yahoo Finance Balance Sheet Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> YFinanceBalanceSheetQueryParams:
        """Transform the query parameters."""
        return YFinanceBalanceSheetQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFinanceBalanceSheetQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
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
        ).get_balance_sheet(as_dict=False, pretty=False, freq=period)

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
        query: YFinanceBalanceSheetQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFinanceBalanceSheetData]:
        """Transform the data."""
        return [YFinanceBalanceSheetData.model_validate(d) for d in data]

```

## High-Level Overview

Yahoo Finance Balance Sheet Model.

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.balance_sheet import (
BalanceSheetData,
BalanceSheetQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class YFinanceBalanceSheetQueryParams(BalanceSheetQueryParams):
Yahoo Finance Balance Sheet Query.



## Detailed Structure

### Python File Structure

**Classes** (3):
`YFinanceBalanceSheetQueryParams`, `YFinanceBalanceSheetData`, `YFinanceBalanceSheetFetcher`

**Functions** (4):
`date_validate`, `transform_query`, `extract_data`, `transform_data`

**Imports** (23):
`datetime`, `datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.balance_sheet`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`, `string.`, `the`, `json`, `curl_adapter`, `CurlCffiAdapter`, `numpy`, `nan`, `openbb_core.provider.utils.errors`, `EmptyDataError`


## Key Components

**Class `YFinanceBalanceSheetQueryParams`**: Yahoo Finance Balance Sheet Query.

    Source: https://finance.yahoo.com/

**Class `YFinanceBalanceSheetData`**: Yahoo Finance Balance Sheet Data.

**Class `YFinanceBalanceSheetFetcher`**: Yahoo Finance Balance Sheet Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.balance_sheet`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `json`
- `curl_adapter`
- `numpy`
- `openbb_core.provider.utils.errors`

## Notes
- Generated: 2025-11-18T07:54:43.556412
- Generator: World's Best Repo Book Generator v1.0.0
