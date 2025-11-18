# Documentation: openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_share_statistics_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_share_statistics_fetcher_urllib3_v2.yaml`
- **Size**: 2,166 characters, 96 lines
- **Words**: 165
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

## High-Level Overview

This is a .yaml file containing 96 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.277583
- Generator: World's Best Repo Book Generator v1.0.0
