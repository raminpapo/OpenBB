# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/wsj/openbb_wsj/__init__.py`
- **Size**: 1,071 bytes
- **Lines**: 26
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""WSJ provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_wsj.models.active import WSJActiveFetcher
from openbb_wsj.models.gainers import WSJGainersFetcher
from openbb_wsj.models.losers import WSJLosersFetcher

wsj_provider = Provider(
    name="wsj",
    website="https://www.wsj.com",
    description="""WSJ (Wall Street Journal) is a business-focused, English-language
international daily newspaper based in New York City. The Journal is published six
days a week by Dow Jones & Company, a division of News Corp, along with its Asian
and European editions. The newspaper is published in the broadsheet format and
online. The Journal has been printed continuously since its inception on
July 8, 1889, by Charles Dow, Edward Jones, and Charles Bergstresser.
The WSJ is the largest newspaper in the United States, by circulation.
    """,
    fetcher_dict={
        "ETFGainers": WSJGainersFetcher,
        "ETFLosers": WSJLosersFetcher,
        "ETFActive": WSJActiveFetcher,
    },
    repr_name="Wall Street Journal (WSJ)",
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
- `Provider`
- `WSJActiveFetcher`
- `WSJGainersFetcher`
- `WSJLosersFetcher`
- `openbb_core.provider.abstract.provider`
- `openbb_wsj.models.active`
- `openbb_wsj.models.gainers`
- `openbb_wsj.models.losers`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.110945Z
**Generator**: World's Best Repo Book Generator v1.0
