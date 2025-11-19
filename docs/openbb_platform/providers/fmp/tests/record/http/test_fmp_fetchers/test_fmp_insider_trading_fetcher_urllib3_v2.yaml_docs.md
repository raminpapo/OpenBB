# File Documentation: test_fmp_insider_trading_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_insider_trading_fetcher_urllib3_v2.yaml`
- **Size**: 1,808 bytes
- **Lines**: 59
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
    uri: https://financialmodelingprep.com/stable/insider-trading/search?apikey=MOCK_API_KEY&limit=1&page=0&statistics=False&symbol=AAPL&transactionType=P-Purchase
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA21RyU7DMBC99yuinEnsbKXpLWoRQkJNRUEcEAfjuK3V2A620xAh/h07qdnKIZIz
        b5mZN08Tz3s3n+f5qmcvovbnnl8U61v/YqxuaU35bok0sUgMoyyAl0E8c7iWiCuENRX8jJQ6kiSN
        kNr4LOjBMiCEEczyOMkcAwvWIN5/4zAxNnnyT5v7vhnarIN1K/EeKeJIiuBWUk2JKjtOKkNKpun0
        7wwrxAb9Y3G9urrzNg+bYvXVxniXW6uWllJRSbAW0sEIv7ZUUTtFKZdUNWL8GUJzpFFUyhs+vgzI
        27p2eQrJ3Abp+eD3pz2H6WMTw4nRSIqtJorjMP+t6t1CC8GY4N5GC3xwzq0cLrrXulFzALquC40s
        3IkjKEx49EgUINUOSVAhjcAYOrD5z/I8TpMoM6eaQfijFNjrDsWA8oq8hXvNfNPtY/L8CZrULrRO
        AgAA
    headers:
      Access-Control-Allow-Credentials:
      - 'true'
      Access-Control-Allow-Headers:
      - X-Requested-With, content-type, auth-token, Authorization, stripe-signature,
        APPS, publicauthkey, privateauthkey
      Access-Control-Allow-Methods:
      - GET, POST, OPTIONS
      Access-Control-Allow-Origin:
      - '*'
      Access-Control-Max-Age:
      - '3600'
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json; charset=utf-8
      Date:
      - Tue, 23 Sep 2025 03:08:25 GMT
      Etag:
      - W/"24e-Mor+agkJ3s63+PC2x3+NMIFde1Q"
      Server:
      - nginx/1.18.0 (Ubuntu)
      Transfer-Encoding:
      - chunked
      Vary:
      - Accept-Encoding
      X-Frame-Options:
      - SAMEORIGIN
      X-Powered-By:
      - Express
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_fmp_insider_trading_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.900143Z
**Generator**: World's Best Repo Book Generator v1.0
