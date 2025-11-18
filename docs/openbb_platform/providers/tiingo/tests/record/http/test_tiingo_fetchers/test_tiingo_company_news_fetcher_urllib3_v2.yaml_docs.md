# Documentation: openbb_platform/providers/tiingo/tests/record/http/test_tiingo_fetchers/test_tiingo_company_news_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/tiingo/tests/record/http/test_tiingo_fetchers/test_tiingo_company_news_fetcher_urllib3_v2.yaml`
- **Size**: 1,939 characters, 43 lines
- **Words**: 111
- **Extension**: .yaml
- **Classification**: Text file

## Original Source

```yaml
interactions:
- request:
    body: null
    headers:
      Accept:
      - application/json
      Accept-Encoding:
      - gzip, deflate
      Connection:
      - keep-alive
    method: GET
    uri: https://api.tiingo.com/tiingo/news?limit=2&tickers=AAPL%2CMSFT&token=MOCK_TOKEN
  response:
    body:
      string: "[{\"id\":88022478,\"publishedDate\":\"2025-09-23T23:41:49Z\",\"title\":\"How
        to double your ASX share portfolio without chasing risky stocks\",\"url\":\"https://www.fool.com.au/2025/09/24/how-to-double-your-asx-share-portfolio-without-chasing-risky-stocks/\",\"description\":\"It
        isn't as hard as you might think to double your ASX share portfolio. Here's
        what you need to know...\",\"source\":\"fool.com.au\",\"tags\":[\"Healthcare\",\"Stock\",\"Technology\",\"Unknown
        Sector\"],\"crawlDate\":\"2025-09-23T23:44:57.142650Z\",\"tickers\":[\"aapl\",\"brn\",\"gmg\",\"hvn\",\"msft\",\"rmd\",\"rmd\",\"tls\"]},{\"id\":88021957,\"publishedDate\":\"2025-09-23T23:10:24Z\",\"title\":\"Forget
        Scratchgate \u2014 iPhone 17 reportedly dropping calls and suffering from
        cellular connectivity issues\",\"url\":\"https://www.tomsguide.com/phones/iphones/forget-scratchgate-iphone-17-reportedly-dropping-calls-and-suffering-from-cellular-connectivity-issues\",\"description\":\"Another
        issue for Apple's latest smartphone\",\"source\":\"tomsguide.com\",\"tags\":[\"Communication
        Services\",\"Stock\",\"Technology\"],\"crawlDate\":\"2025-09-23T23:11:33.929839Z\",\"tickers\":[\"aapl\",\"t\",\"vz\",\"vza\"]}]"
    headers:
      Allow:
      - GET, HEAD, OPTIONS
      Content-Length:
      - '1093'
      Content-Type:
      - application/json
      Date:
      - Tue, 23 Sep 2025 23:58:37 GMT
      Server:
      - nginx/1.18.0 (Ubuntu)
      Vary:
      - Cookie, Origin
      x-frame-options:
      - SAMEORIGIN
    status:
      code: 200
      message: OK
version: 1

```

## High-Level Overview

This is a .yaml file containing 43 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:41.736264
- Generator: World's Best Repo Book Generator v1.0.0
