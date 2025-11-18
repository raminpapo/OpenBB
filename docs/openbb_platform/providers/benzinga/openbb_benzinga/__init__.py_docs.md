# Documentation: openbb_platform/providers/benzinga/openbb_benzinga/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/benzinga/openbb_benzinga/__init__.py`
- **Size**: 898 characters, 23 lines
- **Words**: 58
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Benzinga provider module."""

from openbb_benzinga.models.analyst_search import BenzingaAnalystSearchFetcher
from openbb_benzinga.models.company_news import BenzingaCompanyNewsFetcher
from openbb_benzinga.models.price_target import BenzingaPriceTargetFetcher
from openbb_benzinga.models.world_news import BenzingaWorldNewsFetcher
from openbb_core.provider.abstract.provider import Provider

benzinga_provider = Provider(
    name="benzinga",
    website="https://www.benzinga.com",
    description="""Benzinga is a financial data provider that offers an API
focused on information that moves the market.""",
    credentials=["api_key"],
    fetcher_dict={
        "AnalystSearch": BenzingaAnalystSearchFetcher,
        "CompanyNews": BenzingaCompanyNewsFetcher,
        "WorldNews": BenzingaWorldNewsFetcher,
        "PriceTarget": BenzingaPriceTargetFetcher,
    },
    repr_name="Benzinga",
)

```

## High-Level Overview

Benzinga provider module.

from openbb_benzinga.models.analyst_search import BenzingaAnalystSearchFetcher
from openbb_benzinga.models.company_news import BenzingaCompanyNewsFetcher
from openbb_benzinga.models.price_target import BenzingaPriceTargetFetcher
from openbb_benzinga.models.world_news import BenzingaWorldNewsFetcher
from openbb_core.provider.abstract.provider import Provider

benzinga_provider = Provider(
name="benzinga",
website="https://www.benzinga.com",
description="""Benzinga is a financial data provider that offers an API
focused on information that moves the market.""",
credentials=["api_key"],
fetcher_dict={
"AnalystSearch": BenzingaAnalystSearchFetcher,
"CompanyNews": BenzingaCompanyNewsFetcher,
"WorldNews": BenzingaWorldNewsFetcher,
"PriceTarget": BenzingaPriceTargetFetcher,
},

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (10):
`openbb_benzinga.models.analyst_search`, `BenzingaAnalystSearchFetcher`, `openbb_benzinga.models.company_news`, `BenzingaCompanyNewsFetcher`, `openbb_benzinga.models.price_target`, `BenzingaPriceTargetFetcher`, `openbb_benzinga.models.world_news`, `BenzingaWorldNewsFetcher`, `openbb_core.provider.abstract.provider`, `Provider`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_benzinga.models.analyst_search`
- `openbb_benzinga.models.company_news`
- `openbb_benzinga.models.price_target`
- `openbb_benzinga.models.world_news`
- `openbb_core.provider.abstract.provider`

## Notes
- Generated: 2025-11-18T07:54:37.270399
- Generator: World's Best Repo Book Generator v1.0.0
