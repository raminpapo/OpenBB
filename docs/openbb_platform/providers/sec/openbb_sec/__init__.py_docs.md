# Documentation: openbb_platform/providers/sec/openbb_sec/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/__init__.py`
- **Size**: 2,452 characters, 51 lines
- **Words**: 138
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

SEC provider module.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (35):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_sec.models.cik_map`, `SecCikMapFetcher`, `openbb_sec.models.company_filings`, `SecCompanyFilingsFetcher`, `openbb_sec.models.compare_company_facts`, `SecCompareCompanyFactsFetcher`, `openbb_sec.models.equity_ftd`, `SecEquityFtdFetcher`, `openbb_sec.models.equity_search`, `SecEquitySearchFetcher`, `openbb_sec.models.form_13FHR`, `SecForm13FHRFetcher`, `openbb_sec.models.htm_file`, `SecHtmFileFetcher`, `openbb_sec.models.insider_trading`, `SecInsiderTradingFetcher`, `openbb_sec.models.institutions_search`, `SecInstitutionsSearchFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_sec.models.cik_map`
- `openbb_sec.models.company_filings`
- `openbb_sec.models.compare_company_facts`
- `openbb_sec.models.equity_ftd`
- `openbb_sec.models.equity_search`
- `openbb_sec.models.form_13FHR`
- `openbb_sec.models.htm_file`
- `openbb_sec.models.insider_trading`
- `openbb_sec.models.institutions_search`

## Notes
- Generated: 2025-11-18T07:54:40.581415
- Generator: World's Best Repo Book Generator v1.0.0
