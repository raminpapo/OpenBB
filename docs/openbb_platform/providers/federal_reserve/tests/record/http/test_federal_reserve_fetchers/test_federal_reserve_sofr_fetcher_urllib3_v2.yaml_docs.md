# File Documentation: test_federal_reserve_sofr_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/federal_reserve/tests/record/http/test_federal_reserve_fetchers/test_federal_reserve_sofr_fetcher_urllib3_v2.yaml`
- **Size**: 1,775 bytes
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
    uri: https://markets.newyorkfed.org/api/rates/secured/sofr/search.json?startDate=2024-06-01&endDate=2024-06-06
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAEA6pWUCpKTQtKLEktVrJSiFaoVlBKTUtLTS7JLEt1SSxJVbJSUDIyMDLRNTDTNTBT
        0lFQKqksAIsG+7sFKSnoKBWkFiWn5pWAjFCyUjDVMzZGCAZA5DJzUg3BckaW2OSMTMGSxkbYJM0h
        kiYG2CQtLcE6TUwUdJTK8nNKc1M985wyc3Iy8/NA3jEyMLBQ0FEqSi3LLM7Mz/PMS8lMTizJLwJ5
        SkmhVge/b00p9a0xVjcT41tjrOEE8y0ogLH41tDSAqSNTN+aUOpbusetJSi9kOlbY6J8a4otzQ1I
        Sja0NMTnW8AUYhVqAQ8xhrzKAwAA
    headers:
      Access-Control-Allow-Headers:
      - Content-Type,Content-Disposition
      Access-Control-Allow-Methods:
      - OPTIONS,GET
      Access-Control-Allow-Origin:
      - '*'
      Access-Control-Expose-Headers:
      - Content-Disposition
      Cache-Control:
      - no-store
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Length:
      - '249'
      Content-Type:
      - application/json; charset=utf-8
      Date:
      - Thu, 27 Jun 2024 10:22:36 GMT
      Pragma:
      - no-cache
      Vary:
      - Accept-Encoding
      strict-transport-security:
      - max-age=31536000; includeSubDomains
      x-amz-apigw-id:
      - aBaJCEsPiYcFdlQ=
      x-amzn-requestid:
      - 79bfb88b-47c7-4921-a8c4-f1bb33fd1e41
      x-amzn-trace-id:
      - Root=1-667d3d6c-1dc4236a875e19392ac99ad5;Parent=7e8d1f0f7d2a5a62;Sampled=0;lineage=e7c0e2ee:0
      x-frame-options:
      - SAMEORIGIN
      x-xss-protection:
      - 1; mode=block
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_federal_reserve_sofr_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:49.704611Z
**Generator**: World's Best Repo Book Generator v1.0
