# Documentation: openbb_platform/providers/ecb/openbb_ecb/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/ecb/openbb_ecb/__init__.py`
- **Size**: 922 characters, 21 lines
- **Words**: 75
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

ECB provider module.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_ecb.models.balance_of_payments`, `ECBBalanceOfPaymentsFetcher`, `openbb_ecb.models.currency_reference_rates`, `ECBCurrencyReferenceRatesFetcher`, `openbb_ecb.models.yield_curve`, `ECBYieldCurveFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_ecb.models.balance_of_payments`
- `openbb_ecb.models.currency_reference_rates`
- `openbb_ecb.models.yield_curve`

## Notes
- Generated: 2025-11-18T07:54:37.682844
- Generator: World's Best Repo Book Generator v1.0.0
