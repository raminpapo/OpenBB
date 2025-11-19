# File Documentation: test_fmp_price_target_consensus_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_price_target_consensus_fetcher_urllib3_v2.yaml`
- **Size**: 2,577 bytes
- **Lines**: 95
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
    uri: https://financialmodelingprep.com/stable/price-target-consensus?apikey=MOCK_API_KEY&symbol=MSFT
  response:
    body:
      string: "[\n  {\n    \"symbol\": \"MSFT\",\n    \"targetHigh\": 675,\n    \"targetLow\":
        515,\n    \"targetConsensus\": 613.91,\n    \"targetMedian\": 630\n  }\n]"
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
      Content-Length:
      - '133'
      Content-Type:
      - application/json; charset=utf-8
      Date:
      - Tue, 23 Sep 2025 03:08:26 GMT
      Etag:
      - W/"85-pngYnWGRrrHmKzPk4DA2qeAt9oY"
      Server:
      - nginx/1.18.0 (Ubuntu)
      X-Frame-Options:
      - SAMEORIGIN
      X-Powered-By:
      - Express
    status:
      code: 200
      message: OK
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
    uri: https://financialmodelingprep.com/stable/price-target-consensus?apikey=MOCK_API_KEY&symbol=AAPL
  response:
    body:
      string: "[\n  {\n    \"symbol\": \"AAPL\",\n    \"targetHigh\": 310,\n    \"targetLow\":
        173,\n    \"targetConsensus\": 236.38,\n    \"targetMedian\": 227.5\n  }\n]"
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
      Content-Length:
      - '135'
      Content-Type:
      - application/json; charset=utf-8
      Date:
      - Tue, 23 Sep 2025 03:08:26 GMT
      Etag:
      - W/"87-/rBEAUFlIK4NeqtTV8mA6/THNsA"
      Server:
      - nginx/1.18.0 (Ubuntu)
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

This is a **config** file named `test_fmp_price_target_consensus_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.911001Z
**Generator**: World's Best Repo Book Generator v1.0
