# Documentation: openbb_platform/providers/polygon/tests/record/http/test_polygon_fetchers/test_polygon_equity_historical_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/polygon/tests/record/http/test_polygon_fetchers/test_polygon_equity_historical_fetcher_urllib3_v2.yaml`
- **Size**: 1,457 characters, 46 lines
- **Words**: 73
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
    uri: https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-01/2023-01-10?adjusted=True&apiKey=MOCK_API_KEY&limit=49999&sort=asc
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAA/1TSQWvcTAwG4P+iawYhaWYkzdzCd/wK7b2Usl1PaNolIWs7pYT978XxYDs+CuPH
        7yu9wfR4/t2uUOH+/ssnCPAyt+vf/57npwmqBri2cb5M4z44Db/mcWoD1Ok6t+0FqF/f4BUqIwuz
        JeN2Rx7g9Q9UlowmOcAzVI6E4gHO65gswM91WgJclmFCtgATVFYTE6H3J8ATVCZh0nwL75RjYSKN
        sd0tn1klRU2aVkoUvXRKMepKiaPmbF3LuPxl15w87ZoZUZINI2N18o8YuceOGXLcc0nHDM22YKY7
        VZLvlGpO2TfKLCfjfKQcubhsuYg7VVBlq1D2DpfgnSrOckjFnIU6ZUhWyPlYYWRUKbJtK2lerUjI
        uVsRE3erHKwoiQ4NaspxW5di9KKcP8Qq6LJToptksUuMosvqLr0F2awoeqgw51QS3b4FGKfTNI9Q
        4fP/sNzny9zG6fvjABXsh7VTzNLK4ENO7SQtDrEJPzxQsbNBgHO/9Nu/AAAA//8qAqeOGwMAAA==
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Length:
      - '397'
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:46 GMT
      Server:
      - nginx/1.19.2
      Strict-Transport-Security:
      - max-age=15724800; includeSubDomains
      Vary:
      - Accept-Encoding
      X-Request-Id:
      - 7b7ea352e9d8d54ea2e3d3e21ff097c7
    status:
      code: 200
      message: OK
version: 1

```

## High-Level Overview

This is a .yaml file containing 46 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.548301
- Generator: World's Best Repo Book Generator v1.0.0
