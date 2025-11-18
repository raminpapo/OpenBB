# Documentation: examples/openbb-apachebeam/tests/test_obb_pipeline.py

## File Metadata
- **Path**: `examples/openbb-apachebeam/tests/test_obb_pipeline.py`
- **Size**: 1,882 characters, 49 lines
- **Words**: 159
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

This is a .py file containing 49 lines of code.

## Detailed Structure

### Python File Structure

**Classes** (2):
`AsyncProcess`, `MyTestCase`

**Functions** (4):
`__init__`, `fetch_data`, `process`, `test_sample_pipeline`

**Imports** (13):
`unittest`, `apache_beam.testing.test_pipeline`, `TestPipeline`, `apache_beam.options.pipeline_options`, `PipelineOptions`, `asyncio`, `apache_beam`, `openbb_yfinance.models.equity_quote`, `YFinanceEquityQuoteFetcher`, `openbb_yfinance.models.equity_profile`, `YFinanceEquityProfileFetcher`, `openbb_yfinance.models.company_news`, `YFinanceCompanyNewsFetcher`


## Key Components

**Class `AsyncProcess`**: No documentation

**Class `MyTestCase`**: No documentation

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest`
- `apache_beam.testing.test_pipeline`
- `apache_beam.options.pipeline_options`
- `asyncio`
- `apache_beam`
- `openbb_yfinance.models.equity_quote`
- `openbb_yfinance.models.equity_profile`
- `openbb_yfinance.models.company_news`

## Notes
- Generated: 2025-11-18T07:54:35.232204
- Generator: World's Best Repo Book Generator v1.0.0
