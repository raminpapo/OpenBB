# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/__init__.py`
- **Size**: 2,452 bytes
- **Lines**: 51
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""SEC provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_sec.models.cik_map import SecCikMapFetcher
from openbb_sec.models.company_filings import SecCompanyFilingsFetcher
from openbb_sec.models.compare_company_facts import SecCompareCompanyFactsFetcher
from openbb_sec.models.equity_ftd import SecEquityFtdFetcher
from openbb_sec.models.equity_search import SecEquitySearchFetcher
from openbb_sec.models.form_13FHR import SecForm13FHRFetcher
from openbb_sec.models.htm_file import SecHtmFileFetcher
from openbb_sec.models.insider_trading import SecInsiderTradingFetcher
from openbb_sec.models.institutions_search import SecInstitutionsSearchFetcher
from openbb_sec.models.latest_financial_reports import SecLatestFinancialReportsFetcher
from openbb_sec.models.management_discussion_analysis import (
    SecManagementDiscussionAnalysisFetcher,
)
from openbb_sec.models.nport_disclosure import SecNportDisclosureFetcher
from openbb_sec.models.rss_litigation import SecRssLitigationFetcher
from openbb_sec.models.schema_files import SecSchemaFilesFetcher
from openbb_sec.models.sec_filing import SecFilingFetcher
from openbb_sec.models.sic_search import SecSicSearchFetcher
from openbb_sec.models.symbol_map import SecSymbolMapFetcher

sec_provider = Provider(
    name="sec",
    website="https://www.sec.gov/data",
    description="SEC is the public listings regulatory body for the United States.",
    credentials=None,
    fetcher_dict={
        "CikMap": SecCikMapFetcher,
        "CompanyFilings": SecCompanyFilingsFetcher,
        "CompareCompanyFacts": SecCompareCompanyFactsFetcher,
        "EquityFTD": SecEquityFtdFetcher,
        "EquitySearch": SecEquitySearchFetcher,
        "Filings": SecCompanyFilingsFetcher,
        "Form13FHR": SecForm13FHRFetcher,
        "SecHtmFile": SecHtmFileFetcher,
        "InsiderTrading": SecInsiderTradingFetcher,
        "InstitutionsSearch": SecInstitutionsSearchFetcher,
        "LatestFinancialReports": SecLatestFinancialReportsFetcher,
        "ManagementDiscussionAnalysis": SecManagementDiscussionAnalysisFetcher,
        "NportDisclosure": SecNportDisclosureFetcher,
        "RssLitigation": SecRssLitigationFetcher,
        "SchemaFiles": SecSchemaFilesFetcher,
        "SecFiling": SecFilingFetcher,
        "SicSearch": SecSicSearchFetcher,
        "SymbolMap": SecSymbolMapFetcher,
    },
    repr_name="Securities and Exchange Commission (SEC)",
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
- `Provider`
- `SecCikMapFetcher`
- `SecCompanyFilingsFetcher`
- `SecCompareCompanyFactsFetcher`
- `SecEquityFtdFetcher`
- `SecEquitySearchFetcher`
- `SecFilingFetcher`
- `SecForm13FHRFetcher`
- `SecHtmFileFetcher`
- `SecInsiderTradingFetcher`
- `SecInstitutionsSearchFetcher`
- `SecLatestFinancialReportsFetcher`
- `SecNportDisclosureFetcher`
- `SecRssLitigationFetcher`
- `SecSchemaFilesFetcher`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.965572Z
**Generator**: World's Best Repo Book Generator v1.0
