# File Documentation: test_polygon_currency_historical_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/polygon/tests/record/http/test_polygon_fetchers/test_polygon_currency_historical_fetcher_urllib3_v2.yaml`
- **Size**: 1,528 bytes
- **Lines**: 47
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
    uri: https://api.polygon.io/v2/aggs/ticker/C:EURUSD/range/1/day/2023-01-01/2023-01-10?apiKey=MOCK_API_KEY&limit=49999&sort=asc
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAA/2SUwWrcMBCG32XOooxG0ozsa9pTD4WWnEop3rWXpA0JWdspJey7F9nWjKB7EsZ8
        n//5R/sOy+P593SFHu76T/df7799BAev63T9e/eyPi/Qe3Rwneb1aZmbJ8P4a52XaYR+ua6TvgH9
        93d4g96Tg7c/0PsPyJ138LIfc+wcnLezdMHBgx2f9jckZwfFwUIpeMLyc/BckDe3sSX6KIYXrnhB
        kopn4ah8r/iYlM5e2Ogb9BBQYA5mSDlpAOFUDamwHo5cakjevl8wohl2alVQF7toii5XRYopaAg0
        RUg6pBSjObpDsjs2bHV4TDGYQ6LGwMQag7w3CVmOYEGycG4kG7dKUHJ5XiVJy06EWjazOVgdMVOn
        jo5DU/aOrQ4ruwzhyFCGcDbkf3S2KQWMXdN1XaQowTdoI2Nu0NywReEBRek+cNNzoepwEoktkqCu
        KjPp50sgrVnYdlVXNRBRW/JGVQVti1gVQUvesVWR7bYlu27lZhyOgLnteMPefjiYl2FZZ+jhy2co
        1/x1nebl5+MIPWAaLidkxtP5MkxEeJryxQvJONJwGkZwcK7/GLd/AQAA//9jyROSaQQAAA==
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Length:
      - '451'
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:54 GMT
      Server:
      - nginx/1.19.2
      Strict-Transport-Security:
      - max-age=15724800; includeSubDomains
      Vary:
      - Accept-Encoding
      X-Request-Id:
      - 05afb0660bcfae220be8f1727dd2abad
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_polygon_currency_historical_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.897950Z
**Generator**: World's Best Repo Book Generator v1.0
