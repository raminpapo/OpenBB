# Documentation: openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_historical_attributes_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_historical_attributes_urllib3_v2.yaml`
- **Size**: 4,143 characters, 139 lines
- **Words**: 231
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
    uri: https://api-v2.intrinio.com/historical_data/AAPL/ebit?api_key=MOCK_API_KEY&end_date=2023-01-01&frequency=yearly&page_size=1000&provider=intrinio&sort_order=desc&start_date=2013-01-01
  response:
    body:
      string: !!binary |
        H4sIAGk7fWYAA3TQ2wrCMAwG4Hfp9ZQkPaTdq4iMokMHZYpuIoy9u7U3LaPrVWg+/qZZxH14T4/X
        cPGhu/rJi/a0iFj0ohUERAdwB1KiER8f5niJ6BAkpHOEtSkxJqwLDI6A6xgSNhkbhhhds+iStYXV
        LOu5aJN12TK5nYGR/1ZCkavAuro1200YlEx1q7d/Y9Ko61Yly9lqqezOvHK7Bx3fyrnnRoz9d+qe
        /hZ74xzC+gMAAP//AwAceBCU4AEAAA==
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:01 GMT
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
    uri: https://api-v2.intrinio.com/historical_data/MSFT/ebit?api_key=MOCK_API_KEY&end_date=2023-01-01&frequency=yearly&page_size=1000&provider=intrinio&sort_order=desc&start_date=2013-01-01
  response:
    body:
      string: !!binary |
        H4sIAGk7fWYAA2zQ3QrCMAwF4HfJ9SZJ09+9isgoOnRQpmgnwti7O0RQ2uQqJB/n4ixwGR/5eh+P
        MfWnmCN0+wW2ZYAOFCrVom0ZoYFnTPN29OzI4md2uDb/lkrriFDJFktrGFnOpVBazdZ72frSstVO
        y9aVVoWAJFtbWWM5yNaUlrxBJ1td5Tr/rayyXFs0v34PDUzDK/e3eN5+05zS+gYAAP//AwAidEj3
        3gEAAA==
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:01 GMT
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
    uri: https://api-v2.intrinio.com/historical_data/MSFT/marketcap?api_key=MOCK_API_KEY&end_date=2023-01-01&frequency=yearly&page_size=1000&provider=intrinio&sort_order=desc&start_date=2013-01-01
  response:
    body:
      string: !!binary |
        H4sIAGk7fWYAA2TQ22oCQQwG4HeZ61Um54mvIkWGVlRYbGl3pSC+u8EryeQqJB8/Ifdyvvwt37+X
        zz4fvvrSy25/L9Ecy65gRdwAbgjKVG59XmMIpu6ClZFct/UxvWvIGrlpdYlChqzrkK1MSg1ixzkb
        fNDBBaqQVLSsW9bGyt6sERhlbBkrEBmSOdmQrBkzoxLiKz5jyZhc2Kk5Cw+YB0wIrnE4s2RMw6uV
        4gJgl9YCf0zlevxfDj/9FMvrOs+PJwAAAP//AwCqcps57AEAAA==
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:01 GMT
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
    uri: https://api-v2.intrinio.com/historical_data/AAPL/marketcap?api_key=MOCK_API_KEY&end_date=2023-01-01&frequency=yearly&page_size=1000&provider=intrinio&sort_order=desc&start_date=2013-01-01
  response:
    body:
      string: !!binary |
        H4sIAGk7fWYAA2TQW0pDQQwG4L3M82lJ/kwu062IlEGLFg5V9FSE0r13fJPMSwjJR0hyK+/n7+3j
        6/zS1+Nr33o5PN3KSE7lUEDAjrETLkv56et1FEFqHBYGIPZ0X/5rnnQ0qFcRVZKsadKAaq3s7FaT
        5pY1w5mkqSi3lnVk7SD3WhFBnLFnHBCwkMFkwpaxOjxEndmmNXTCUs20Sh2XZlznyc0Q3iQ0P48l
        43EbyEZs9Df5eSmX0+92/Oxvo3m5ruv9AQAA//8DAPeSJDvsAQAA
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:01 GMT
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

This is a .yaml file containing 139 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.226848
- Generator: World's Best Repo Book Generator v1.0.0
