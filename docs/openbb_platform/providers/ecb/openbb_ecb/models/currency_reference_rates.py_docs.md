# File Documentation: currency_reference_rates.py

## Metadata
- **Path**: `openbb_platform/providers/ecb/openbb_ecb/models/currency_reference_rates.py`
- **Size**: 2,439 bytes
- **Lines**: 71
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `currency_reference_rates.py`.

**Python Module**

- **Classes** (3): ECBCurrencyReferenceRatesQueryParams, ECBCurrencyReferenceRatesData, ECBCurrencyReferenceRatesFetcher
- **Functions** (3): transform_query, extract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ECBCurrencyReferenceRatesQueryParams`**(CurrencyReferenceRatesQueryParams)
- **`ECBCurrencyReferenceRatesData`**(CurrencyReferenceRatesData)
- **`ECBCurrencyReferenceRatesFetcher`**(
    Fetcher[ECBCurrencyReferenceRatesQueryParams, ECBCurrencyReferenceRatesData]
)

#### Decorators Used

currency, rate, staticmethod, time


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `OpenBBError`
- `make_request`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.currency_reference_rates`
- `openbb_core.provider.utils.helpers`
- `typing`
- `xmltodict`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.792244Z
**Generator**: World's Best Repo Book Generator v1.0
