# File Documentation: test_intrinio_latest_attributes_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_latest_attributes_urllib3_v2.yaml`
- **Size**: 2,793 bytes
- **Lines**: 127
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
    uri: https://api-v2.intrinio.com/companies/MSFT/data_point/ceo?api_key=MOCK_API_KEY
  response:
    body:
      string: !!binary |
        H4sIAGo7fWYAA1IKTiypTFTwS0xJzclJVAIAAAD//wMAZxmyKw8AAAA=
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:02 GMT
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
    uri: https://api-v2.intrinio.com/companies/AAPL/data_point/marketcap?api_key=MOCK_API_KEY
  response:
    body:
      string: !!binary |
        H4sIAGo7fWYAAzI2sjS3MLE0tDQxMjXQMwAAAAD//wMANEcZLw8AAAA=
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:02 GMT
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
    uri: https://api-v2.intrinio.com/companies/AAPL/data_point/ceo?api_key=MOCK_API_KEY
  response:
    body:
      string: !!binary |
        H4sIAGo7fWYAA1IKyczNL8moVHDRU3DOz89WAgAAAP//AwBIpQsVEQAAAA==
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:02 GMT
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
    uri: https://api-v2.intrinio.com/companies/MSFT/data_point/marketcap?api_key=MOCK_API_KEY
  response:
    body:
      string: !!binary |
        H4sIAGo7fWYAAzI2NrcwNbY0NTIAAj0DAAAAAP//AwC52O5DDwAAAA==
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:02 GMT
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

This is a **config** file named `test_intrinio_latest_attributes_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.546568Z
**Generator**: World's Best Repo Book Generator v1.0
