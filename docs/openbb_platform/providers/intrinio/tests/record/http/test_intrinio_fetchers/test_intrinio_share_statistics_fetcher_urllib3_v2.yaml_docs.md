# File Documentation: test_intrinio_share_statistics_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_share_statistics_fetcher_urllib3_v2.yaml`
- **Size**: 2,166 bytes
- **Lines**: 96
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
    uri: https://api-v2.intrinio.com/companies/AAPL/data_point/weightedavebasicdilutedsharesos/number?api_key=MOCK_API_KEY
  response:
    body:
      string: !!binary |
        H4sIAHA7fWYAAzI0NTY2MbAwMjAw0DMAAAAA//8DAB00zBcNAAAA
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:08 GMT
      Transfer-Encoding:
      - chunked
      Vary:
      - Origin,Accept-Encoding
    status:
      code: 200
      message: OK
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
    uri: https://api-v2.intrinio.com/companies/AAPL/data_point/public_float/number?api_key=MOCK_API_KEY
  response:
    body:
      string: !!binary |
        H4sIAHA7fWYAAzIytTQ0NDM1AAM9AwAAAAD//wMAWSojCg8AAAA=
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:08 GMT
      Transfer-Encoding:
      - chunked
      Vary:
      - Origin,Accept-Encoding
    status:
      code: 200
      message: OK
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
    uri: https://api-v2.intrinio.com/companies/AAPL/data_point/adjweightedavebasicdilutedsharesos/number?api_key=MOCK_API_KEY
  response:
    body:
      string: !!binary |
        H4sIAHA7fWYAAzI0NTY2MbAwMjAw0DMAAAAA//8DAB00zBcNAAAA
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:08 GMT
      Transfer-Encoding:
      - chunked
      Vary:
      - Origin,Accept-Encoding
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_intrinio_share_statistics_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.585267Z
**Generator**: World's Best Repo Book Generator v1.0
