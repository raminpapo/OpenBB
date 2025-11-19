# File Documentation: test_intrinio_historical_dividends_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_historical_dividends_fetcher_urllib3_v2.yaml`
- **Size**: 1,219 bytes
- **Lines**: 39
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
    uri: https://api-v2.intrinio.com/securities/AAPL/prices/adjustments?api_key=MOCK_API_KEY&end_date=2023-06-06&page_size=100&start_date=2023-01-01
  response:
    body:
      string: !!binary |
        H4sIAG07fWYAA5RRW2vCMBT+KyPPKklr7OVN2ZDB5i7icIwRQhpjtE1Lkg6r+N934gbDvu3xfNdz
        khNyvhZ71lgtJOPFrnW+ksY7lH+cUMG9RDmKcBQPMR2SCA3QhgtfW5TjUZalE5ImmOKYZgkZoEJ/
        6UKaIpDR+G9morVWGtFB1mp5CyGuKbVnlntdo5yM8HnQK4uGBPfLxgmlOE3IhJC4Vxb/q+wTMAky
        7UF0QhoyAsC42lm1A4eoq4abjl0YGNhiPZkfn0LW5bXkQWy5UfJH4A6K1cdHm3UgMLwKV0ybppQ3
        90Zc0ooA3b0sw9DfzmuxlzZYps8Pv921016yKyZfBfdGKw3AbDbHGM+yd7qOriw9fv36Pg5Lb7mV
        TJTcuSsFWdJF+paCAr6/4rZjpXZeG4Vyb1t5hmvkwbOGK9jftGV5/gYAAP//AwCKhFgOLwIAAA==
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:05 GMT
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

This is a **config** file named `test_intrinio_historical_dividends_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.533177Z
**Generator**: World's Best Repo Book Generator v1.0
