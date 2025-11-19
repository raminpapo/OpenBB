# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/ecb/openbb_ecb/__init__.py`
- **Size**: 922 bytes
- **Lines**: 21
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ECB provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_ecb.models.balance_of_payments import ECBBalanceOfPaymentsFetcher
from openbb_ecb.models.currency_reference_rates import ECBCurrencyReferenceRatesFetcher
from openbb_ecb.models.yield_curve import ECBYieldCurveFetcher

ecb_provider = Provider(
    name="ECB",
    website="https://data.ecb.europa.eu",
    description="""The ECB Data Portal provides access to all official ECB statistics.
The portal also provides options to download data and comprehensive metadata for each dataset.
Statistical publications and dashboards offer a compilation of key data on selected topics.""",
    fetcher_dict={
        "BalanceOfPayments": ECBBalanceOfPaymentsFetcher,
        "CurrencyReferenceRates": ECBCurrencyReferenceRatesFetcher,
        "YieldCurve": ECBYieldCurveFetcher,
    },
    repr_name="European Central Bank (ECB)",
)

```



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `ECBBalanceOfPaymentsFetcher`
- `ECBCurrencyReferenceRatesFetcher`
- `ECBYieldCurveFetcher`
- `Provider`
- `openbb_core.provider.abstract.provider`
- `openbb_ecb.models.balance_of_payments`
- `openbb_ecb.models.currency_reference_rates`
- `openbb_ecb.models.yield_curve`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.787798Z
**Generator**: World's Best Repo Book Generator v1.0
