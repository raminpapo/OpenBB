# Documentation: openbb_platform/providers/finra/openbb_finra/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/finra/openbb_finra/__init__.py`
- **Size**: 719 characters, 19 lines
- **Words**: 54
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

FINRA provider module.

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


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (6):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_finra.models.equity_short_interest`, `FinraShortInterestFetcher`, `openbb_finra.models.otc_aggregate`, `FinraOTCAggregateFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_finra.models.equity_short_interest`
- `openbb_finra.models.otc_aggregate`

## Notes
- Generated: 2025-11-18T07:54:38.614898
- Generator: World's Best Repo Book Generator v1.0.0
