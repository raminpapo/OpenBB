# Documentation: openbb_platform/providers/government_us/openbb_government_us/models/treasury_prices.py

## File Metadata
- **Path**: `openbb_platform/providers/government_us/openbb_government_us/models/treasury_prices.py`
- **Size**: 5,064 characters, 148 lines
- **Words**: 358
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""US Government Treasury Prices."""

# pylint: disable=unused-argument

from typing import Any, Literal

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.treasury_prices import (
    TreasuryPricesData,
    TreasuryPricesQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class GovernmentUSTreasuryPricesQueryParams(TreasuryPricesQueryParams):
    """US Government Treasury Prices Query."""

    cusip: str | None = Field(description="Filter by CUSIP.", default=None)
    security_type: Literal["bill", "note", "bond", "tips", "frn"] | None = Field(
        description="Filter by security type.",
        default=None,
    )


class GovernmentUSTreasuryPricesData(TreasuryPricesData):
    """US Government Treasury Prices Data."""


class GovernmentUSTreasuryPricesFetcher(
    Fetcher[
        GovernmentUSTreasuryPricesQueryParams,
        list[GovernmentUSTreasuryPricesData],
    ]
):
    """US Government Treasury Prices Fetcher."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> GovernmentUSTreasuryPricesQueryParams:
        """Transform query params."""
        # pylint: disable=import-outside-toplevel
        from datetime import date, timedelta

        today = date.today()
        last_bd = (
            today - timedelta(today.weekday() - 4) if today.weekday() > 4 else today
        )
        if params.get("date") is None:
            params["date"] = last_bd
        return GovernmentUSTreasuryPricesQueryParams(**params)

    @staticmethod
    def extract_data(
        query: GovernmentUSTreasuryPricesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> str:
        """Extract the raw data from US Treasury website."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import make_request
        from openbb_government_us.utils.helpers import get_random_agent

        url = "https://treasurydirect.gov/GA-FI/FedInvest/securityPriceDetail"

        HEADERS = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://treasurydirect.gov/",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://treasurydirect.gov",
            "User-Agent": get_random_agent(),
        }

        payload = (
            f"priceDateDay={query.date.day}"  # type: ignore
            f"&priceDateMonth={query.date.month}"  # type: ignore
            f"&priceDateYear={query.date.year}"  # type: ignore
            "&fileType=csv"
            "&csv=CSV+FORMAT"
        )

        r = make_request(url=url, method="POST", headers=HEADERS, data=payload)

        if r.status_code != 200:
            raise OpenBBError("Error with the request: " + str(r.status_code))

        if r.encoding != "ISO-8859-1":
            raise OpenBBError(f"Expected ISO-8859-1 encoding but got: {r.encoding}")

        return r.content.decode("utf-8")

    @staticmethod
    def transform_data(
        query: GovernmentUSTreasuryPricesQueryParams,
        data: str,
        **kwargs: Any,
    ) -> list[GovernmentUSTreasuryPricesData]:
        """Transform the data."""
        # pylint: disable=import-outside-toplevel
        from io import StringIO  # noqa
        from pandas import Index, read_csv, to_datetime  # noqa

        try:
            if not data:
                raise EmptyDataError("Data not found")
            results = read_csv(StringIO(data), header=0)
            results.columns = Index(
                [
                    "cusip",
                    "security_type",
                    "rate",
                    "maturity_date",
                    "call_date",
                    "bid",
                    "offer",
                    "eod_price",
                ]
            )
            results["date"] = query.date.strftime("%Y-%m-%d")  # type: ignore
            for col in ["maturity_date", "call_date"]:
                results[col] = (
                    (
                        to_datetime(results[col], format="%m/%d/%Y").dt.strftime(
                            "%Y-%m-%d"
                        )
                    )
                    .fillna("-")
                    .replace("-", None)
                )

        except Exception as e:
            raise OpenBBError(e) from e

        if query.security_type is not None:
            results = results[
                results["security_type"].str.contains(query.security_type, case=False)
            ]
        if query.cusip is not None:
            results = results[results["cusip"] == query.cusip]
        return [
            GovernmentUSTreasuryPricesData.model_validate(d)
            for d in results.to_dict("records")
        ]

```

## High-Level Overview

US Government Treasury Prices.

# pylint: disable=unused-argument

from typing import Any, Literal

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.treasury_prices import (
TreasuryPricesData,
TreasuryPricesQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class GovernmentUSTreasuryPricesQueryParams(TreasuryPricesQueryParams):
US Government Treasury Prices Query.
US Government Treasury Prices Data.


## Detailed Structure

### Python File Structure

**Classes** (3):
`GovernmentUSTreasuryPricesQueryParams`, `GovernmentUSTreasuryPricesData`, `GovernmentUSTreasuryPricesFetcher`

**Functions** (3):
`transform_query`, `extract_data`, `transform_data`

**Imports** (23):
`typing`, `Any`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.treasury_prices`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `datetime`, `date`, `US`, `openbb_core.provider.utils.helpers`, `make_request`, `openbb_government_us.utils.helpers`, `get_random_agent`, `io`, `StringIO`


## Key Components

**Class `GovernmentUSTreasuryPricesQueryParams`**: US Government Treasury Prices Query.

**Class `GovernmentUSTreasuryPricesData`**: US Government Treasury Prices Data.

**Class `GovernmentUSTreasuryPricesFetcher`**: US Government Treasury Prices Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.treasury_prices`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `datetime`
- `openbb_core.provider.utils.helpers`
- `openbb_government_us.utils.helpers`
- `io`

## Notes
- Generated: 2025-11-18T07:54:39.904963
- Generator: World's Best Repo Book Generator v1.0.0
