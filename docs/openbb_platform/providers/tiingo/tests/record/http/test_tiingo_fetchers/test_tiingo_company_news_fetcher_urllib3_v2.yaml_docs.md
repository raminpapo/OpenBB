# File Documentation: test_tiingo_company_news_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/tiingo/tests/record/http/test_tiingo_fetchers/test_tiingo_company_news_fetcher_urllib3_v2.yaml`
- **Size**: 1,939 bytes
- **Lines**: 43
- **Category**: config
- **Extension**: .yaml

---

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



---

## High-Level Overview

This is a **config** file named `test_tiingo_company_news_fetcher_urllib3_v2.yaml`.

**Configuration File**

This file contains configuration settings for the project.


---

## Detailed Analysis

### Configuration Structure

This configuration file defines settings and parameters for the project.


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:53.023731Z
**Generator**: World's Best Repo Book Generator v1.0
