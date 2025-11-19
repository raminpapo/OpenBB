# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/finra/openbb_finra/__init__.py`
- **Size**: 719 bytes
- **Lines**: 19
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FINRA provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_finra.models.equity_short_interest import FinraShortInterestFetcher
from openbb_finra.models.otc_aggregate import FinraOTCAggregateFetcher

finra_provider = Provider(
    name="finra",
    website="https://www.finra.org/finra-data",
    description="""FINRA Data provides centralized access to the abundance of data FINRA
makes available to the public, media, researchers and member firms.""",
    credentials=None,
    fetcher_dict={
        "OTCAggregate": FinraOTCAggregateFetcher,
        "EquityShortInterest": FinraShortInterestFetcher,
    },
    repr_name="Financial Industry Regulatory Authority (FINRA)",
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
- `FinraOTCAggregateFetcher`
- `FinraShortInterestFetcher`
- `Provider`
- `openbb_core.provider.abstract.provider`
- `openbb_finra.models.equity_short_interest`
- `openbb_finra.models.otc_aggregate`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:49.786336Z
**Generator**: World's Best Repo Book Generator v1.0
