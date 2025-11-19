# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/federal_reserve/openbb_federal_reserve/__init__.py`
- **Size**: 2,138 bytes
- **Lines**: 49
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Federal Reserve provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_federal_reserve.models.central_bank_holdings import (
    FederalReserveCentralBankHoldingsFetcher,
)
from openbb_federal_reserve.models.federal_funds_rate import (
    FederalReserveFederalFundsRateFetcher,
)
from openbb_federal_reserve.models.fomc_documents import (
    FederalReserveFomcDocumentsFetcher,
)
from openbb_federal_reserve.models.money_measures import (
    FederalReserveMoneyMeasuresFetcher,
)
from openbb_federal_reserve.models.overnight_bank_funding_rate import (
    FederalReserveOvernightBankFundingRateFetcher,
)
from openbb_federal_reserve.models.primary_dealer_fails import (
    FederalReservePrimaryDealerFailsFetcher,
)
from openbb_federal_reserve.models.primary_dealer_positioning import (
    FederalReservePrimaryDealerPositioningFetcher,
)
from openbb_federal_reserve.models.sofr import FederalReserveSOFRFetcher
from openbb_federal_reserve.models.treasury_rates import (
    FederalReserveTreasuryRatesFetcher,
)
from openbb_federal_reserve.models.yield_curve import FederalReserveYieldCurveFetcher

federal_reserve_provider = Provider(
    name="federal_reserve",
    website="https://www.federalreserve.gov/data.htm",  #  Not a typo, it's really .htm
    description="""Access data provided by the Federal Reserve System, the Central Bank of the United States.""",
    fetcher_dict={
        "CentralBankHoldings": FederalReserveCentralBankHoldingsFetcher,
        "FederalFundsRate": FederalReserveFederalFundsRateFetcher,
        "FomcDocuments": FederalReserveFomcDocumentsFetcher,
        "MoneyMeasures": FederalReserveMoneyMeasuresFetcher,
        "OvernightBankFundingRate": FederalReserveOvernightBankFundingRateFetcher,
        "PrimaryDealerFails": FederalReservePrimaryDealerFailsFetcher,
        "PrimaryDealerPositioning": FederalReservePrimaryDealerPositioningFetcher,
        "SOFR": FederalReserveSOFRFetcher,
        "TreasuryRates": FederalReserveTreasuryRatesFetcher,
        "YieldCurve": FederalReserveYieldCurveFetcher,
    },
    repr_name="Federal Reserve (FED)",
)

```



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `FederalReserveSOFRFetcher`
- `FederalReserveYieldCurveFetcher`
- `Provider`
- `openbb_core.provider.abstract.provider`
- `openbb_federal_reserve.models.central_bank_holdings`
- `openbb_federal_reserve.models.federal_funds_rate`
- `openbb_federal_reserve.models.fomc_documents`
- `openbb_federal_reserve.models.money_measures`
- `openbb_federal_reserve.models.overnight_bank_funding_rate`
- `openbb_federal_reserve.models.primary_dealer_fails`
- `openbb_federal_reserve.models.primary_dealer_positioning`
- `openbb_federal_reserve.models.sofr`
- `openbb_federal_reserve.models.treasury_rates`
- `openbb_federal_reserve.models.yield_curve`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:49.594428Z
**Generator**: World's Best Repo Book Generator v1.0
