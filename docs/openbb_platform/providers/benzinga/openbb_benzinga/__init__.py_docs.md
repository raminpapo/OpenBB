# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/benzinga/openbb_benzinga/__init__.py`
- **Size**: 898 bytes
- **Lines**: 23
- **Category**: python
- **Extension**: .py

---

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
- `BenzingaAnalystSearchFetcher`
- `BenzingaCompanyNewsFetcher`
- `BenzingaPriceTargetFetcher`
- `BenzingaWorldNewsFetcher`
- `Provider`
- `openbb_benzinga.models.analyst_search`
- `openbb_benzinga.models.company_news`
- `openbb_benzinga.models.price_target`
- `openbb_benzinga.models.world_news`
- `openbb_core.provider.abstract.provider`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.273327Z
**Generator**: World's Best Repo Book Generator v1.0
