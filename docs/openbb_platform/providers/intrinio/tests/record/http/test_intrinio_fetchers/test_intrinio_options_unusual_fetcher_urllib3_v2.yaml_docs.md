# File Documentation: test_intrinio_options_unusual_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_options_unusual_fetcher_urllib3_v2.yaml`
- **Size**: 1,374 bytes
- **Lines**: 40
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
    uri: https://api-v2.intrinio.com/options/unusual_activity/intraday?activity_type=block&api_key=MOCK_API_KEY&end_date=2023-11-21&minimum_total_value=10000000&page_size=1000&sentiment=neutral&source=delayed&start_date=2023-11-20
  response:
    body:
      string: !!binary |
        H4sIAGI7fWYAA8zU3U7CMBQA4Hfp9Wj6s7PT7tYXMNFEozFLGQ1ZKN2yHwIS3t0OMVHYAI0X7K5n
        p6dnX9ttSVubmW1I+rolzWY5LR1JycP98xOJSFssbdOaZRVCggk54Xwi2COHNIaUAVUSX/q0TWVD
        xtSV+aIflq1x2cq4LkR5whBRq69wU7z3UcYiYla2NnObVXWRHzIphsS89KGnvD30kWUiZoInd0xo
        YOEJS5hmkZk2s2ubd21R+v1sTTEi02J2+gZoEpHG+v57fF/X2y4s4UKlzs9s7TaFn3/2cTSZUbaL
        fgPDdSqBcuCXYETCpMbe4QcMDMBgqKhHYCSHAKMEjMKgVFQNwqCUVN8ejFQxS05OzBAMKE3lWRiN
        4zCg+QgMKKTs/2DOu2DKJA1bcdEFJFcA4gqXJPSvj1my7+flDEuiEyqGLxJqCjfHgsA1u4pFybj/
        EYyz4JlrpGLRmw6wKLEH+zPLWxTy121WhV5J6jvndh8AAAD//wMAhrSB85YFAAA=
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:13:54 GMT
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

This is a **config** file named `test_intrinio_options_unusual_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.578610Z
**Generator**: World's Best Repo Book Generator v1.0
