# File Documentation: test_obb_pipeline.py

## Metadata
- **Path**: `examples/openbb-apachebeam/tests/test_obb_pipeline.py`
- **Size**: 1,882 bytes
- **Lines**: 49
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
import unittest
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.options.pipeline_options import PipelineOptions
import asyncio
import apache_beam as beam
from openbb_yfinance.models.equity_quote import YFinanceEquityQuoteFetcher as quote_fetcher
from openbb_yfinance.models.equity_profile import YFinanceEquityProfileFetcher as profile_fetcher
from openbb_yfinance.models.company_news import YFinanceCompanyNewsFetcher as news_fetcher


class AsyncProcess(beam.DoFn):

    def __init__(self, credentials, fetcher):
        self.credentials = credentials
        self.fetcher = fetcher

    async def fetch_data(self, element: str):
        params = dict(symbol=element)
        data = await self.fetcher.fetch_data(params, self.credentials)
        return [d.model_dump(exclude_none=True) for d in data]

    def process(self, element: str):
        return asyncio.run(self.fetch_data(element))

class MyTestCase(unittest.TestCase):


    def test_sample_pipeline(self):
        credentials = {} # Running OBB endpoints which do not require credentials
        debug_sink = beam.Map(print)
        ticker = 'AAPL'

        with TestPipeline(options=PipelineOptions()) as p:
            quote = (p | 'Start Quote' >> beam.Create([ticker])
                     | 'Run Quote' >> beam.ParDo(AsyncProcess(credentials, quote_fetcher))
                     | 'Print quote' >> debug_sink)

            profile = (p | 'Start Profile' >> beam.Create([ticker])
                     | 'Run Profile' >> beam.ParDo(AsyncProcess(credentials, profile_fetcher))
                     | 'Print profile' >> debug_sink)

            news = (p | 'Start News' >> beam.Create([ticker])
                       | 'Run News' >> beam.ParDo(AsyncProcess(credentials, news_fetcher))
                       | 'Print nes' >> debug_sink)


if __name__ == '__main__':
    unittest.main()

```



---

## High-Level Overview

This is a **python** file named `test_obb_pipeline.py`.

**Python Module**

- **Classes** (2): AsyncProcess, MyTestCase
- **Functions** (4): __init__, fetch_data, process, test_sample_pipeline
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AsyncProcess`**(beam.DoFn)
- **`MyTestCase`**(unittest.TestCase)

#### Functions

- **`__init__(self, credentials, fetcher)`**
- **`fetch_data(self, element: str)`**
- **`process(self, element: str)`**
- **`test_sample_pipeline(self)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `PipelineOptions`
- `TestPipeline`
- `YFinanceCompanyNewsFetcher`
- `YFinanceEquityProfileFetcher`
- `YFinanceEquityQuoteFetcher`
- `apache_beam`
- `apache_beam.options.pipeline_options`
- `apache_beam.testing.test_pipeline`
- `asyncio`
- `openbb_yfinance.models.company_news`
- `openbb_yfinance.models.equity_profile`
- `openbb_yfinance.models.equity_quote`
- `unittest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:45.973185Z
**Generator**: World's Best Repo Book Generator v1.0
