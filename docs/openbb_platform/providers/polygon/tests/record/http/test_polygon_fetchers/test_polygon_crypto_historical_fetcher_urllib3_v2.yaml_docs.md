# Documentation: openbb_platform/providers/polygon/tests/record/http/test_polygon_fetchers/test_polygon_crypto_historical_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/polygon/tests/record/http/test_polygon_fetchers/test_polygon_crypto_historical_fetcher_urllib3_v2.yaml`
- **Size**: 1,747 characters, 50 lines
- **Words**: 77
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
    uri: https://api.polygon.io/v2/aggs/ticker/X:BTCUSD/range/1/day/2023-01-01/2023-01-10?apiKey=MOCK_API_KEY&limit=49999&sort=asc
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAA/0zUy6rcRhAG4HfptSjqftEyzi6LLJJAIIRwLhrixNh4RuMQDufdjWbUPdKqWwg+
        /VXV/dbWjy//Luc2t9/nH3798NsvP7apfb0u5/8/fLl+XttMOLXzcrl+Wi+HN0+v/1wv6/La5vV8
        XcYXbf7jrX1rM7EggpCZiJAXy9S+/ddmctMC09Kpfblthaf2sq2cCCyn9vdtozq1T9tKC6e2oR5s
        QozbM7XPbeZiMX2f7qARF3CWGUqVygC9GIywg07WQXco28FE2UFTBuNhOoU/TLHkqt1kYlTg2lBN
        HWAioIyE7gkyyAKNTm51vJNV4EMMVDyI4Yw9JZc4ArGLb8VAz46mGFSGD7QgdjRVQfmOBmLuqKtB
        xkOtnb2pRpzZc5KXGnhWWClF8EDZgYt70tQaSZMNvHrS7GgYAj7QDM9D1Awz7FGT1cG4FMnLffvV
        XVUENKauso2opQnoe1TGXl8PhHy0tFwOY6RhQbSrbl5gElrGwcTbfNzVEgN9qGUENFQG6V2t6mqh
        3Ab6rgpqHQaJuZTH8BJJgheRK4ey1lCDIDB7hbc+7GoQG9B+XoKSukoISkMlcTwemTKzXZXQCAij
        QDZx6VGDVSEM96hBOsgIqE5qL28QMtRoqjDzYZLciNQPTWVArooINxXvppCAeUg3N0l3VlVAe1dt
        6++dvRdjVwXzMErmgUjvf07tsj6t10ub288/te2a+npdLutfH1/b3F6f0NFOz6cTxxNm5ImfGU+2
        5PJi+fzcpvbSb7z37wEAAP//Iq77pikFAAA=
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Length:
      - '596'
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:53 GMT
      Server:
      - nginx/1.19.2
      Strict-Transport-Security:
      - max-age=15724800; includeSubDomains
      Vary:
      - Accept-Encoding
      X-Request-Id:
      - da0605fbff27a0878f2b20f5e8ec58bb
    status:
      code: 200
      message: OK
version: 1

```

## High-Level Overview

This is a .yaml file containing 50 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.533499
- Generator: World's Best Repo Book Generator v1.0.0
