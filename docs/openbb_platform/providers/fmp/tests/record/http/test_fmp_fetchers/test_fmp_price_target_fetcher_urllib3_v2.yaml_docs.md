# File Documentation: test_fmp_price_target_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_price_target_fetcher_urllib3_v2.yaml`
- **Size**: 1,811 bytes
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
    uri: https://financialmodelingprep.com/stable/price-target-news?apikey=MOCK_API_KEY&limit=1&page=0&symbol=AAPL
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA3WRQWvcMBCF7/kVgynkklnL3rhu9rbJEloIrWlcAg05zFrTWFlbMpK2xi3975W8
        m7It9CAd9N7wvdF7PAP4GQ5A4qZ+a7pkBcl6Xd0lF4fXYb/tlGtZbshzFHORFyiuMM9rUazEcrUs
        F0KIr68Dmkf35fNdtLbeD26VpuM4Lrasfyj9TIvG9GlPdsfepZ6bNs2LVFyll2X5LsvF23Rkud27
        1qEkjeo7O2zVLtw0DB3jYFXD6Mk+s0dvcJkJdDQ5VENrNGNWouSetERvqdkFIgZHViC1TBLNt9l4
        mrVWvpsX25CGD4EH7yMP1pEHVeRBPfOgNvAmAC/gPhDhvDJO+ZCwm+B+b0Myx/IcPmnYzAmgtvTC
        jTd2gltjQVUxIWTlK500dZPzH6n/i//n5yP6QA5y5B7H5Ev1H2keeWhZh2ieZdDyy2JRnGxbHeu0
        kXh97OT0O67J8bG+08r+yXxj+oH0FF0Ph76SoP86e/oNrhBxOVACAAA=
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
      - Tue, 23 Sep 2025 03:08:26 GMT
      Etag:
      - W/"250-dyxOcIdb6GQxOT7RkTpgT9qtR7c"
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

This is a **config** file named `test_fmp_price_target_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.912837Z
**Generator**: World's Best Repo Book Generator v1.0
