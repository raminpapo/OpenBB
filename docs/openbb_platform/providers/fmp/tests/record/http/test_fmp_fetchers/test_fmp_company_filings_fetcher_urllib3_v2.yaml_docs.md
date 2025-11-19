# File Documentation: test_fmp_company_filings_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_company_filings_fetcher_urllib3_v2.yaml`
- **Size**: 1,683 bytes
- **Lines**: 57
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
    uri: https://financialmodelingprep.com/stable/sec-filings-search/symbol?apikey=MOCK_API_KEY&from=2024-09-20&limit=2&page=0&symbol=AAPL&to=2024-10-20
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA72RO2vDMBSF9/wKoTm2rh6xHW2G0ilDhw6FUopqq7aIX9gidij975XtOumQQoa0
        QgJx7uHec/meVwh9uIcQ7o7lW11giXAcP+zwelYTsx8lcIczoFu+FN5NYarsTlk91hkw4VHwaIgA
        5HQXo0oS3VidXrDSSHKQNDr1rNvy8dhMNrGIbswUIbe26SQhfd/7nU78rD6QuE1yc9Ad0WmmWpIq
        q8gck5wTM+G+lAY/JM9FmEXPVKke/NyW58UqVexuNnToinsuNk+wIf3eGzcUrzRkWwaCUeoPZYHd
        3M/1jUFAdDUIZ/0Gwf8FhLgEQvwxCPEbiEiwIIDwBGL18gVOB1KyFAMAAA==
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
      - Tue, 23 Sep 2025 17:03:38 GMT
      Etag:
      - W/"314-4qkaMdUuoYBonX1MeZ/iPTKCBkg"
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

This is a **config** file named `test_fmp_company_filings_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.745267Z
**Generator**: World's Best Repo Book Generator v1.0
