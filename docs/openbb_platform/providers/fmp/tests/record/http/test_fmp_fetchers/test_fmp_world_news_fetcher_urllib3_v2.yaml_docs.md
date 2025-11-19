# File Documentation: test_fmp_world_news_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_world_news_fetcher_urllib3_v2.yaml`
- **Size**: 1,819 bytes
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
    uri: https://financialmodelingprep.com/stable/news/general-latest?apikey=MOCK_API_KEY&from=None&limit=1&page=0&to=None
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA4WQsU7DMBCG9z7FKRNITVMiKtEuiBaQKjFULAyI4ZJcGlPHjuxLQ4WQeAfekCfh
        nFIEXRg82P7v+//7HwcAr3IAIr+rM6ujGZhW6+H+rWkzrXxFxTUyyVeUjtNJPJ7GaQrp2WySzs4v
        oiOtC7ql2ZJn61YaczooWLHuKQ9Ka7gXJCxa9rA0pQ4XhHmbZZouDwOqxnU/UDE3fpYk/YMflcqg
        yRXq2haklVk3jppRbuvEUOeTTvCxE2KcCz5We3yMcdbj47DEeJqmo+dmfbDyar+g+g7ehOAB+ROe
        XjgI7tAzdESbIXBFcEsFOZRtyJPbEogjKMPkhAIhg4dOcQXCzDcexIYlLyADadrKfwFb1C2yssbD
        5/sHZDvwtiaoCX0rmGEQWweG0PWWlVpXgf5rzhpwlFtXwElQzNuyJGYptlA5yjaApuhnF1ermxBL
        WWALBsWHO3s6OmzZOv2n7+M2ktBdMp7+13ESCe9t8PQF6g8WLGACAAA=
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
      - W/"260-W1kNXsbSjZzHooJekG8u5og0O8c"
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

This is a **config** file named `test_fmp_world_news_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.923042Z
**Generator**: World's Best Repo Book Generator v1.0
