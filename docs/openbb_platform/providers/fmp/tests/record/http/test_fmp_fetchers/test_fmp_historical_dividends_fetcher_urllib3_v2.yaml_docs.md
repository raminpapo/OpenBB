# Documentation: openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_historical_dividends_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_historical_dividends_fetcher_urllib3_v2.yaml`
- **Size**: 1,489 characters, 56 lines
- **Words**: 98
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
    uri: https://financialmodelingprep.com/stable/dividends?apikey=MOCK_API_KEY&limit=1&symbol=AAPL
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA3WNPQvCMBRF9/6KkNlK89GauhU6OugsDrF5QiRNNaZCEP+7KbUFUYe3nHvuffsE
        oUc8hPAttMfO4DXCVbXd4MVIlfQwMJrRPM1ESsiUOGg6p+q/+UWGFqz/Evg8DY2RTnrd2U9plbJ5
        Rapzre9agVVRyJa0mNo/adBgRsS5KAUjIieszFlR8rdxcnDtwTZh+LfrpfPgTMAxfCaHFwwicKcP
        AQAA
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
      - Tue, 23 Sep 2025 03:08:32 GMT
      Etag:
      - W/"10f-K0MvcS0xniNGvOUlg+I3gcjmoY0"
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

## High-Level Overview

This is a .yaml file containing 56 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:39.600146
- Generator: World's Best Repo Book Generator v1.0.0
