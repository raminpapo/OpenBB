# File Documentation: company_filings.py

## Metadata
- **Path**: `openbb_platform/providers/nasdaq/openbb_nasdaq/models/company_filings.py`
- **Size**: 8,540 bytes
- **Lines**: 253
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Nasdaq Company Filings Models."""

# pylint: disable=unused-argument

from datetime import (
    date as dateType,
    datetime,
)
from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.company_filings import (
    CompanyFilingsData,
    CompanyFilingsQueryParams,
)
from pydantic import Field, field_validator, model_validator

form_groups = {
    "annual": "Annual%20Reports",
    "quarterly": "Quarterly%20Reports",
    "proxy": "Proxies%20and%20Info%20Statements",
    "insider": "Insider%20Transactions",
    "8k": "8-K%20Related",
    "registration": "Registration%20Statements",
    "comment": "Comment%20Letters",
}


FormGroups = Literal[
    "annual",
    "quarterly",
    "proxy",
    "insider",
    "8k",
    "registration",
    "comment",
]


class NasdaqCompanyFilingsQueryParams(CompanyFilingsQueryParams):
    """Nasdaq Company Filings Query Parameters."""

    __json_schema_extra__ = {
        "year": {
            "x-widget_config": {
                "options": sorted(
                    [
                        {
                            "label": str(year),
                            "value": year,
                        }
                        for year in range(1994, datetime.now().year + 1)
                    ],
                    key=lambda x: x["label"],  # type: ignore
                    reverse=True,
                ),
                "value": datetime.now().year,
            }
        },
        "symbol": {
            "x-widget_config": {
                "value": "AAPL",
            }
        },
    }

    year: int | None = Field(
        description=(
            "Calendar year of the data, default is current year."
            + " The earliest year available is 1994, for all companies and form types."
        ),
        default=None,
        ge=1994,
    )
    form_group: FormGroups = Field(
        default="8k",
        description="The form group to fetch, default is 8k.",
    )


class NasdaqCompanyFilingsData(CompanyFilingsData):
    """Nasdaq Company Filings Data."""

    __alias_dict__ = {
        "filing_date": "filed",
        "period_ending": "period",
        "report_type": "formType",
        "name": "companyName",
        "reporting_owner": "reportingOwner",
        "report_url": "htmlLink",
        "pdf_url": "pdfLink",
        "xls_url": "xlsLink",
        "xbr_url": "xbrLink",
        "doc_link": "docLink",
    }
    period_ending: dateType | None = Field(
        default=None,
        description="The ending date for the reporting period, if available.",
    )
    name: str | None = Field(
        default=None,
        description="The name of the company, if available.",
    )
    reporting_owner: str | None = Field(
        default=None,
        description="The name of the reporting owner, if applicable.",
    )
    pdf_url: str | None = Field(
        default=None, description="The URL to the PDF document, if available."
    )
    xls_url: str | None = Field(
        default=None, description="The URL to the XLS document, if available."
    )
    xbr_url: str | None = Field(
        default=None, description="The URL to the XBR document, if available."
    )
    doc_link: str | None = Field(
        default=None, description="The URL to the DOC document, if available."
    )

    @field_validator("period_ending", mode="before", check_fields=False)
    @classmethod
    def _validate_period_ending(cls, v):
        """Validate the period ending date."""
        return datetime.strptime(v, "%m/%d/%Y").date() if v else None

    @model_validator(mode="before")
    @classmethod
    def _validate(cls, values):
        """Validate the data."""
        return {k: v for k, v in values.items() if v}


class NasdaqCompanyFilingsFetcher(
    Fetcher[NasdaqCompanyFilingsQueryParams, list[NasdaqCompanyFilingsData]]
):
    """Nasdaq Company Filings Fetcher."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> NasdaqCompanyFilingsQueryParams:
        """Transform query parameters to the correct format."""
        return NasdaqCompanyFilingsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: NasdaqCompanyFilingsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Extract data from the query."""
        # pylint: disable=import-outside-toplevel
        import time  # noqa
        from openbb_core.provider.utils.errors import OpenBBError
        from openbb_core.provider.utils.helpers import get_requests_session
        from openbb_nasdaq.utils.helpers import get_headers
        from requests.exceptions import ReadTimeout
        from urllib3.exceptions import ReadTimeoutError

        if not query.symbol:
            raise OpenBBError("Symbol field is required.")

        base_url = f"https://api.nasdaq.com/api/company/{query.symbol}/sec-filings?"
        base_url += f"Year={query.year or datetime.now().year}&"
        form_group = form_groups.get(query.form_group)
        url_end = "&sortColumn=filed&sortOrder=desc&IsQuoteMedia=true"
        url = base_url + f"limit=100&FormGroup={form_group}" + url_end
        headers = get_headers(accept_type="json")
        del headers["Connection"]
        rows: list = []

        with get_requests_session() as session:
            try:
                response = session.get(url=url, headers=headers, timeout=10)
            except (ReadTimeout, ReadTimeoutError):
                time.sleep(2)
                try:
                    response = session.get(url=url, headers=headers, timeout=10)
                except (ReadTimeout, ReadTimeoutError) as e:
                    raise OpenBBError(e) from e

            if response.status_code != 200:
                raise OpenBBError(
                    f"Error fetching data from Nasdaq: {response.status_code} - {response.reason}"
                )
            data = response.json().get("data", {})
            rows = data.get("rows", [])
            total_records = (
                int(data.get("totalRecords")) if data.get("totalRecords") else 0
            )
            if total_records < 1:
                raise OpenBBError(
                    f"No data found for {query.symbol} in {query.year}, for form group, {form_group}."
                )
            n_rows = len(rows)
            while n_rows < total_records:
                offset = n_rows
                next_url = url + f"&offset={offset}"
                response = session.get(url=next_url, headers=headers, timeout=10)
                if response.status_code != 200:
                    raise OpenBBError(
                        f"Error fetching data from Nasdaq: {response.status_code} - {response.reason}"
                    )
                next_data = response.json().get("data", {})
                new_rows = next_data.get("rows", [])
                if not new_rows:
                    break
                rows.extend(new_rows)
                n_rows = len(rows)

            data["rows"] = rows
            if not data or not data.get("rows"):
                raise OpenBBError(
                    "No reports for the given symbol, year, and form group."
                )

            return data

    @staticmethod
    def transform_data(
        query: NasdaqCompanyFilingsQueryParams,
        data: dict,
        **kwargs: Any,
    ) -> list[NasdaqCompanyFilingsData]:
        """Transform the raw data into the desired format."""
        results: list[NasdaqCompanyFilingsData] = []

        latest = data.get("latest", [])
        if latest and not data.get("rows"):
            # If there are no rows, use the latest data
            for last in latest:
                results.append(
                    NasdaqCompanyFilingsData(
                        **dict(
                            report_url=last.get("value"),
                            filing_date=(
                                last.get("value", "").rsplit("dateFiled=", maxsplit=1)[
                                    -1
                                ]
                            ),
                            report_type=last.get("label"),
                        )
                    )
                )
        else:
            for item in data.get("rows", []):
                links = item.pop("view", {})
                item.update(**links)
                results.append(NasdaqCompanyFilingsData.model_validate(item))

        return results

```



---

## High-Level Overview

This is a **python** file named `company_filings.py`.

**Python Module**

- **Classes** (3): NasdaqCompanyFilingsQueryParams, NasdaqCompanyFilingsData, NasdaqCompanyFilingsFetcher
- **Functions** (5): _validate_period_ending, _validate, transform_query, extract_data, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`NasdaqCompanyFilingsQueryParams`**(CompanyFilingsQueryParams)
- **`NasdaqCompanyFilingsData`**(CompanyFilingsData)
- **`NasdaqCompanyFilingsFetcher`**(
    Fetcher[NasdaqCompanyFilingsQueryParams, list[NasdaqCompanyFilingsData]]
)

#### Functions

- **`_validate_period_ending(cls, v)`**
- **`_validate(cls, values)`**

#### Decorators Used

classmethod, field_validator, model_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Field`
- `OpenBBError`
- `ReadTimeout`
- `ReadTimeoutError`
- `datetime`
- `get_headers`
- `get_requests_session`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.company_filings`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`
- `openbb_nasdaq.utils.helpers`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.643590Z
**Generator**: World's Best Repo Book Generator v1.0
