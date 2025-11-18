# Documentation: openbb_platform/providers/oecd/openbb_oecd/models/country_interest_rates.py

## File Metadata
- **Path**: `openbb_platform/providers/oecd/openbb_oecd/models/country_interest_rates.py`
- **Size**: 6,272 characters, 170 lines
- **Words**: 472
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OECD Country Interest Rates Data."""

# pylint: disable=unused-argument

from datetime import date
from typing import Any, Literal
from warnings import warn

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.country_interest_rates import (
    CountryInterestRatesData,
    CountryInterestRatesQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_oecd.utils.constants import CODE_TO_COUNTRY_IR, COUNTRY_TO_CODE_IR
from pydantic import Field, field_validator

COUNTRIES = list(CODE_TO_COUNTRY_IR.values()) + ["all"]

DURATION_DICT = {
    "immediate": "IRSTCI",
    "short": "IR3TIB",
    "long": "IRLT",
}


class OecdCountryInterestRatesQueryParams(CountryInterestRatesQueryParams):
    """OECD Country Interest Rates Query."""

    __json_schema_extra__ = {
        "country": {
            "multiple_items_allowed": True,
            "choices": COUNTRIES,
        },
        "frequency": {
            "multiple_items_allowed": False,
            "choices": ["monthly", "quarter", "annual"],
        },
        "duration": {
            "multiple_items_allowed": False,
            "choices": ["immediate", "short", "long"],
        },
    }

    duration: Literal["immediate", "short", "long"] = Field(
        description="Duration of the interest rate."
        + " 'immediate' is the overnight rate, 'short' is the 3-month rate, and 'long' is the 10-year rate.",
        default="short",
    )
    frequency: Literal["monthly", "quarter", "annual"] = Field(
        description="Frequency to get interest rate for for.", default="monthly"
    )

    @field_validator("country", mode="before", check_fields=False)
    @classmethod
    def validate_country(cls, c):
        """Validate country."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import check_item

        result: list = []
        values = c.replace(" ", "_").split(",")
        for v in values:
            if v.upper() in CODE_TO_COUNTRY_IR:
                result.append(CODE_TO_COUNTRY_IR.get(v.upper()))
                continue
            try:
                check_item(v.lower(), COUNTRIES)
            except Exception as e:
                if len(values) == 1:
                    raise e from e
                warn(f"Invalid country: {v}. Skipping...")
                continue
            result.append(v.lower())
        if result:
            return ",".join(result)
        raise OpenBBError(f"No valid country found. -> {values}")


class OecdCountryInterestRatesData(CountryInterestRatesData):
    """OECD Country Interest Rates Data."""


class OecdCountryInterestRatesFetcher(
    Fetcher[OecdCountryInterestRatesQueryParams, list[OecdCountryInterestRatesData]]
):
    """OECD Country Interest Rates Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> OecdCountryInterestRatesQueryParams:
        """Transform the query."""
        transformed_params = params.copy()
        if transformed_params.get("start_date") is None:
            transformed_params["start_date"] = (
                date(2020, 1, 1)
                if transformed_params.get("country") == "all"
                else date(1954, 1, 1)
            )
        if transformed_params.get("end_date") is None:
            transformed_params["end_date"] = date(date.today().year, 12, 31)
        if transformed_params.get("country") is None:
            transformed_params["country"] = "united_states"

        return OecdCountryInterestRatesQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: OecdCountryInterestRatesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the OECD endpoint."""
        # pylint: disable=import-outside-toplevel
        from io import StringIO  # noqa
        from openbb_oecd.utils.helpers import oecd_date_to_python_date
        from pandas import read_csv
        from openbb_core.provider.utils.helpers import make_request

        frequency = query.frequency[0].upper()

        def country_string(input_str: str):
            if input_str == "all":
                return ""
            _countries = input_str.split(",")
            return "+".join([COUNTRY_TO_CODE_IR[country] for country in _countries])

        country = country_string(query.country) if query.country else ""
        start_date = query.start_date.strftime("%Y-%m") if query.start_date else ""
        end_date = query.end_date.strftime("%Y-%m") if query.end_date else ""

        url = (
            "https://sdmx.oecd.org/public/rest/data/OECD.SDD.STES,DSD_KEI@DF_KEI,4.0"
            + f"/{country}.{frequency}.{DURATION_DICT[query.duration]}....?"
            + f"startPeriod={start_date}&endPeriod={end_date}"
            + "&dimensionAtObservation=TIME_PERIOD&detail=dataonly"
        )
        headers = {"Accept": "application/vnd.sdmx.data+csv; charset=utf-8"}
        response = make_request(url, headers=headers, timeout=20)
        if response.status_code != 200:
            raise Exception(f"Error with the OECD request: {response.status_code}")
        df = read_csv(StringIO(response.text)).get(
            ["REF_AREA", "TIME_PERIOD", "OBS_VALUE"]
        )
        if df.empty:
            raise EmptyDataError()
        df = df.rename(
            columns={"REF_AREA": "country", "TIME_PERIOD": "date", "OBS_VALUE": "value"}
        )
        df.country = [CODE_TO_COUNTRY_IR.get(d, d) for d in df.country]
        df.date = df.date.apply(oecd_date_to_python_date)
        df.value = df.value.astype(float) / 100
        df = (
            df.query("value.notnull()")
            .set_index(["date", "country"])
            .sort_index()
            .reset_index()
        )

        return df.to_dict("records")

    @staticmethod
    def transform_data(
        query: OecdCountryInterestRatesQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[OecdCountryInterestRatesData]:
        """Transform the data from the OECD endpoint."""
        return [OecdCountryInterestRatesData.model_validate(d) for d in data]

```

## High-Level Overview

OECD Country Interest Rates Data.

# pylint: disable=unused-argument

from datetime import date
from typing import Any, Literal
from warnings import warn

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.country_interest_rates import (
CountryInterestRatesData,
CountryInterestRatesQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_oecd.utils.constants import CODE_TO_COUNTRY_IR, COUNTRY_TO_CODE_IR
from pydantic import Field, field_validator

COUNTRIES = list(CODE_TO_COUNTRY_IR.values()) + ["all"]


## Detailed Structure

### Python File Structure

**Classes** (3):
`OecdCountryInterestRatesQueryParams`, `OecdCountryInterestRatesData`, `OecdCountryInterestRatesFetcher`

**Functions** (5):
`validate_country`, `transform_query`, `extract_data`, `country_string`, `transform_data`

**Imports** (30):
`datetime`, `date`, `typing`, `Any`, `warnings`, `warn`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.country_interest_rates`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `openbb_oecd.utils.constants`, `CODE_TO_COUNTRY_IR`, `pydantic`, `Field`, `openbb_core.provider.utils.helpers`, `check_item`, `e`


## Key Components

**Class `OecdCountryInterestRatesQueryParams`**: OECD Country Interest Rates Query.

**Class `OecdCountryInterestRatesData`**: OECD Country Interest Rates Data.

**Class `OecdCountryInterestRatesFetcher`**: OECD Country Interest Rates Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `warnings`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.country_interest_rates`
- `openbb_core.provider.utils.errors`
- `openbb_oecd.utils.constants`
- `pydantic`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:40.442879
- Generator: World's Best Repo Book Generator v1.0.0
