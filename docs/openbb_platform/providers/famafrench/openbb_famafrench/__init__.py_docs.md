# Documentation: openbb_platform/providers/famafrench/openbb_famafrench/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/famafrench/openbb_famafrench/__init__.py`
- **Size**: 1,582 characters, 36 lines
- **Words**: 88
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

OpenBB Fama-French Provider module.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (10):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_famafrench.models.breakpoints`, `FamaFrenchBreakpointFetcher`, `openbb_famafrench.models.country_portfolio_returns`, `openbb_famafrench.models.factors`, `FamaFrenchFactorsFetcher`, `openbb_famafrench.models.international_index_returns`, `openbb_famafrench.models.regional_portfolio_returns`, `openbb_famafrench.models.us_portfolio_returns`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_famafrench.models.breakpoints`
- `openbb_famafrench.models.country_portfolio_returns`
- `openbb_famafrench.models.factors`
- `openbb_famafrench.models.international_index_returns`
- `openbb_famafrench.models.regional_portfolio_returns`
- `openbb_famafrench.models.us_portfolio_returns`

## Notes
- Generated: 2025-11-18T07:54:38.313705
- Generator: World's Best Repo Book Generator v1.0.0
