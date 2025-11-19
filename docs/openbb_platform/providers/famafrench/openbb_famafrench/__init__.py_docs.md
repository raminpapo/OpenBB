# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/famafrench/openbb_famafrench/__init__.py`
- **Size**: 1,582 bytes
- **Lines**: 36
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OpenBB Fama-French Provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_famafrench.models.breakpoints import FamaFrenchBreakpointFetcher
from openbb_famafrench.models.country_portfolio_returns import (
    FamaFrenchCountryPortfolioReturnsFetcher,
)
from openbb_famafrench.models.factors import FamaFrenchFactorsFetcher
from openbb_famafrench.models.international_index_returns import (
    FamaFrenchInternationalIndexReturnsFetcher,
)
from openbb_famafrench.models.regional_portfolio_returns import (
    FamaFrenchRegionalPortfolioReturnsFetcher,
)
from openbb_famafrench.models.us_portfolio_returns import (
    FamaFrenchUSPortfolioReturnsFetcher,
)

famafrench_provider = Provider(
    name="famafrench",
    website="https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html",
    description="""
    This provider implements the Fama-French research portfolios and factors data library,
    maintained and hosted by Kenneth R. French at Dartmouth College.
    """,
    fetcher_dict={
        "FamaFrenchBreakpoints": FamaFrenchBreakpointFetcher,
        "FamaFrenchCountryPortfolioReturns": FamaFrenchCountryPortfolioReturnsFetcher,
        "FamaFrenchFactors": FamaFrenchFactorsFetcher,
        "FamaFrenchInternationalIndexReturns": FamaFrenchInternationalIndexReturnsFetcher,
        "FamaFrenchRegionalPortfolioReturns": FamaFrenchRegionalPortfolioReturnsFetcher,
        "FamaFrenchUSPortfolioReturns": FamaFrenchUSPortfolioReturnsFetcher,
    },
    repr_name="Fama-French Research Portfolios and Factors",
)

```



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `FamaFrenchBreakpointFetcher`
- `FamaFrenchFactorsFetcher`
- `Provider`
- `openbb_core.provider.abstract.provider`
- `openbb_famafrench.models.breakpoints`
- `openbb_famafrench.models.country_portfolio_returns`
- `openbb_famafrench.models.factors`
- `openbb_famafrench.models.international_index_returns`
- `openbb_famafrench.models.regional_portfolio_returns`
- `openbb_famafrench.models.us_portfolio_returns`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:49.439125Z
**Generator**: World's Best Repo Book Generator v1.0
