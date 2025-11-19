# File Documentation: test_fmp_key_executives_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_key_executives_fetcher_urllib3_v2.yaml`
- **Size**: 2,052 bytes
- **Lines**: 62
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
    uri: https://financialmodelingprep.com/stable/key-executives?apikey=MOCK_API_KEY&symbol=AAPL
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA72W32/aMBDH3/tXnHjoXhBa+BHK3lroupVVsLKtD9MeLOdCTjg2uth00bT/fQ6U
        UdqkGlvYQyTnbEf++Hv3vXw9AfjhH4CGJauw8QYaM9RkGL6QRJgyZhShtmBiuDOsonv/CjeCF2hJ
        zxvNzWYt0vXeG27BFeMc4Npk9yQW2wVLkft57ZR6CEjHjFrm0/VE4/NstF06Rx0hF8FU+BM9RHMU
        fGFY739lfegZaYn7cSEtrYqYZYc+9LNZAjpMCGOYolkqhEkce2CGU6jkv0UrSD1DzlowQuKIEWDy
        6oIJ9T51Nww6nXBwAHiMFejBIOzXgV7OeAqbK3lLWmhJQm1vpUzmMa6EBpgKxkVyDJmDQb9dI+uI
        GKX1A6/k0PDSsLAI51Iap6tSeZgwZQBjoyNzDMS6Mvl5ru4IR7hCZZapnyhDPI+Y1joikxTHgPQ6
        duuAfCzge73CrBjfohKWjM6ess1cIjLSBF5EoSMWqXGK/onvvwq4M9uhSVOnvTilnIX9jH2W+hSG
        d27u0MJHJ/KdEn+FWmlAdQFvjGayRJ+jvvheMpprjGPGHC5bcEdKkUizfbZu2On3znoH4FW7ay2Z
        WuquTbhC7XGVF9TpDNW61Uj2TYXzUlWFTXxRaoQPRZmWYAdnr38f+E+wX2ortYBvVL38jtIVqx81
        1W3xlgn8iVJjkxxG3nCNefLLEITtzqAXtg/ArIYMDoU8+fYLDfRoWiIJAAA=
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
      - Tue, 23 Sep 2025 03:08:21 GMT
      Etag:
      - W/"922-nfaK9C8pWUf7lA9Re8An07lGMy0"
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

This is a **config** file named `test_fmp_key_executives_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.903502Z
**Generator**: World's Best Repo Book Generator v1.0
