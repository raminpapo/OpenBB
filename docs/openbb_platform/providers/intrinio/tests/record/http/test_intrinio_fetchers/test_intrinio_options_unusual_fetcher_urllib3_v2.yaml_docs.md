# Documentation: openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_options_unusual_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_options_unusual_fetcher_urllib3_v2.yaml`
- **Size**: 1,374 characters, 40 lines
- **Words**: 63
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

## High-Level Overview

This is a .yaml file containing 40 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.271495
- Generator: World's Best Repo Book Generator v1.0.0
