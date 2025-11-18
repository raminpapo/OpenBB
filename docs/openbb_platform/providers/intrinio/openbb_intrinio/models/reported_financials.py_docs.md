# Documentation: openbb_platform/providers/intrinio/openbb_intrinio/models/reported_financials.py

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/openbb_intrinio/models/reported_financials.py`
- **Size**: 5,677 characters, 148 lines
- **Words**: 430
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Intrinio Reported Financials Model."""

# pylint: disable=unused-argument

from typing import Any, Literal
from warnings import warn

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.reported_financials import (
    ReportedFinancialsData,
    ReportedFinancialsQueryParams,
)
from pydantic import Field

STATEMENT_DICT = {
    "balance": "balance_sheet_statement",
    "income": "income_statement",
    "cash": "cash_flow_statement",
}


class IntrinioReportedFinancialsQueryParams(ReportedFinancialsQueryParams):
    """Intrinio Reported Financials Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_company_fundamentals_v2
    Source: https://docs.intrinio.com/documentation/web_api/get_fundamental_reported_financials_v2
    """

    statement_type: Literal["balance", "income", "cash"] = Field(
        default="income",
        description="Cash flow statements are reported as YTD, Q4 is the same as FY.",
    )
    period: Literal["annual", "quarter"] = Field(default="annual")
    fiscal_year: int | None = Field(
        default=None,
        description="The specific fiscal year.  Reports do not go beyond 2008.",
    )


class IntrinioReportedFinancialsData(ReportedFinancialsData):
    """
    Intrinio Reported Financials Data.

    The fields for this model are generated dynamically from the XBRL tags in the Intrinio response.
    """


class IntrinioReportedFinancialsFetcher(
    Fetcher[
        IntrinioReportedFinancialsQueryParams,
        list[IntrinioReportedFinancialsData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> IntrinioReportedFinancialsQueryParams:
        """Transform the query params."""
        return IntrinioReportedFinancialsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: IntrinioReportedFinancialsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Intrinio endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import (
            ClientResponse,
            amake_requests,
        )
        from openbb_intrinio.utils.helpers import get_data_one
        from pandas import DataFrame

        period_type = ""
        api_key = credentials.get("intrinio_api_key") if credentials else ""
        statement_code = STATEMENT_DICT[query.statement_type]
        period_type = "FY" if query.period == "annual" else "Q"
        ids = []
        ids_url = f"https://api-v2.intrinio.com/companies/{query.symbol}/fundamentals?reported_only=true&statement_code={statement_code}"
        if query.fiscal_year is not None:
            if query.fiscal_year < 2008:
                warn("Financials data is only available from 2008 and later.")
                query.fiscal_year = 2008
            ids_url = ids_url + f"&fiscal_year={query.fiscal_year}"
        ids_url = ids_url + f"&page_size=10000&api_key={api_key}"

        fundamentals_ids = await get_data_one(ids_url, **kwargs)
        filings = DataFrame(fundamentals_ids["fundamentals"])

        _period = "" if query.period is None else period_type
        _statement = "" if statement_code is None else statement_code
        if len(filings) > 0:
            filings = filings[filings["statement_code"].str.contains(_statement)]
            if query.period == "annual":
                filings = filings[filings["fiscal_period"].str.contains(_period)]
            ids = filings.iloc[: query.limit]["id"].to_list()

        if ids == []:
            raise OpenBBError("No reports found.")

        async def callback(response: ClientResponse, _: Any) -> dict:
            """Return the response."""
            statement_data = await response.json()
            return {
                "period_ending": statement_data["fundamental"]["end_date"],  # type: ignore
                "fiscal_year": statement_data["fundamental"]["fiscal_year"],  # type: ignore
                "fiscal_period": statement_data["fundamental"]["fiscal_period"],  # type: ignore
                "financials": statement_data["reported_financials"],  # type: ignore
            }

        urls = [
            f"https://api-v2.intrinio.com/fundamentals/{id}/reported_financials?api_key={api_key}"
            for id in ids
        ]

        return await amake_requests(urls, callback, **kwargs)

    @staticmethod
    def transform_data(
        query: IntrinioReportedFinancialsQueryParams, data: list[dict], **kwargs: Any
    ) -> list[IntrinioReportedFinancialsData]:
        """Return the transformed data."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import to_snake_case

        transformed_data: list[IntrinioReportedFinancialsData] = []
        data_tag = "xbrl_tag"
        for item in data:
            sub_dict: dict[str, Any] = {}

            for sub_item in item["financials"]:
                field_name = to_snake_case(sub_item[data_tag]["tag"])
                if sub_item["value"] and sub_item["value"] != 0:
                    sub_dict[field_name] = float(sub_item["value"])

            sub_dict["period_ending"] = item["period_ending"]
            sub_dict["fiscal_year"] = item["fiscal_year"]
            sub_dict["fiscal_period"] = item["fiscal_period"]

            transformed_data.append(IntrinioReportedFinancialsData(**sub_dict))

        return transformed_data

```

## High-Level Overview

Intrinio Reported Financials Model.

# pylint: disable=unused-argument

from typing import Any, Literal
from warnings import warn

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.reported_financials import (
ReportedFinancialsData,
ReportedFinancialsQueryParams,
)
from pydantic import Field

STATEMENT_DICT = {
"balance": "balance_sheet_statement",
"income": "income_statement",
"cash": "cash_flow_statement",
}

## Detailed Structure

### Python File Structure

**Classes** (3):
`IntrinioReportedFinancialsQueryParams`, `IntrinioReportedFinancialsData`, `IntrinioReportedFinancialsFetcher`

**Functions** (4):
`transform_query`, `aextract_data`, `callback`, `transform_data`

**Imports** (22):
`typing`, `Any`, `warnings`, `warn`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.reported_financials`, `pydantic`, `Field`, `the`, `the`, `the`, `openbb_core.provider.utils.helpers`, `openbb_intrinio.utils.helpers`, `get_data_one`, `pandas`, `DataFrame`, `2008`


## Key Components

**Class `IntrinioReportedFinancialsQueryParams`**: Intrinio Reported Financials Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_company_fundamentals_v2
    Source: https://docs.intrinio.com/documentation/web_api/get_fundamental

**Class `IntrinioReportedFinancialsData`**: Intrinio Reported Financials Data.

    The fields for this model are generated dynamically from the XBRL tags in the Intrinio response.

**Class `IntrinioReportedFinancialsFetcher`**: Transform the query, extract and transform the data from the Intrinio endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `warnings`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.reported_financials`
- `pydantic`
- `openbb_core.provider.utils.helpers`
- `openbb_intrinio.utils.helpers`
- `pandas`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:40.147353
- Generator: World's Best Repo Book Generator v1.0.0
