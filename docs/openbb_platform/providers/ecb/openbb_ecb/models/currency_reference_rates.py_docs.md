# Documentation: openbb_platform/providers/ecb/openbb_ecb/models/currency_reference_rates.py

## File Metadata
- **Path**: `openbb_platform/providers/ecb/openbb_ecb/models/currency_reference_rates.py`
- **Size**: 2,439 characters, 71 lines
- **Words**: 172
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ECB Currency Reference Rates Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.currency_reference_rates import (
    CurrencyReferenceRatesData,
    CurrencyReferenceRatesQueryParams,
)


class ECBCurrencyReferenceRatesQueryParams(CurrencyReferenceRatesQueryParams):
    """
    ECB Currency Reference Rates Query.

    source: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/
    """


class ECBCurrencyReferenceRatesData(CurrencyReferenceRatesData):
    """ECB Currency Reference Rates Data."""


class ECBCurrencyReferenceRatesFetcher(
    Fetcher[ECBCurrencyReferenceRatesQueryParams, ECBCurrencyReferenceRatesData]
):
    """Transform the query, extract and transform the data from the ECB endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> ECBCurrencyReferenceRatesQueryParams:
        """Transform query."""
        return ECBCurrencyReferenceRatesQueryParams(**params)

    @staticmethod
    def extract_data(
        query: ECBCurrencyReferenceRatesQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Extract the raw data from the ECB website."""
        # pylint: disable=import-outside-toplevel
        import xmltodict
        from openbb_core.provider.utils.helpers import make_request

        results = {}
        url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
        response = make_request(url)
        if response.status_code != 200:
            raise OpenBBError(
                "Failed to fetch data from ECB."
                + f" -> Status Code: {response.status_code}"
            )
        data = xmltodict.parse(response.content)
        rates_data = data["gesmes:Envelope"]["Cube"]["Cube"]["Cube"]
        rates = {d["@currency"]: d["@rate"] for d in rates_data}
        results["date"] = data["gesmes:Envelope"]["Cube"]["Cube"]["@time"]
        results["EUR"] = 1
        results.update(rates)

        return results

    @staticmethod
    def transform_data(
        query: ECBCurrencyReferenceRatesQueryParams, data: dict, **kwargs: Any
    ) -> ECBCurrencyReferenceRatesData:
        """Transform data."""
        return ECBCurrencyReferenceRatesData.model_validate(data)

```

## High-Level Overview

ECB Currency Reference Rates Model.

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.currency_reference_rates import (
CurrencyReferenceRatesData,
CurrencyReferenceRatesQueryParams,
)


class ECBCurrencyReferenceRatesQueryParams(CurrencyReferenceRatesQueryParams):




class ECBCurrencyReferenceRatesData(CurrencyReferenceRatesData):

## Detailed Structure

### Python File Structure

**Classes** (3):
`ECBCurrencyReferenceRatesQueryParams`, `ECBCurrencyReferenceRatesData`, `ECBCurrencyReferenceRatesFetcher`

**Functions** (3):
`transform_query`, `extract_data`, `transform_data`

**Imports** (13):
`typing`, `Any`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.currency_reference_rates`, `the`, `the`, `xmltodict`, `openbb_core.provider.utils.helpers`, `make_request`, `ECB.`


## Key Components

**Class `ECBCurrencyReferenceRatesQueryParams`**: ECB Currency Reference Rates Query.

    source: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/

**Class `ECBCurrencyReferenceRatesData`**: ECB Currency Reference Rates Data.

**Class `ECBCurrencyReferenceRatesFetcher`**: Transform the query, extract and transform the data from the ECB endpoints.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.currency_reference_rates`
- `xmltodict`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:37.686339
- Generator: World's Best Repo Book Generator v1.0.0
