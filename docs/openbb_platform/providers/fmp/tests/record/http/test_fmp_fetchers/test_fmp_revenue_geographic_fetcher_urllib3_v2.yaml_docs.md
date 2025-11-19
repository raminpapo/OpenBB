# File Documentation: test_fmp_revenue_geographic_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_revenue_geographic_fetcher_urllib3_v2.yaml`
- **Size**: 2,298 bytes
- **Lines**: 65
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
    uri: https://financialmodelingprep.com/stable/revenue-geographic-segmentation?apikey=MOCK_API_KEY&period=annual&structure=flat&symbol=AAPL
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA62XTYvbMBCG7/srTM4JSKMZSdNb2H5A6WHp0sNSenATpzVsPnCyh6Xsf6/ixEuQ
        YivCCiQQaSxLj2bemfl5VxT/3LcoJvvX9e/t8+RDMZnPH75NpqfRVb1flM9PVdm4GRCA5/Fd1dTb
        5dH681Nn21S7bXOolvcvTVNtFq/H2R+PH7vpZXmojkPHVWaCZ2AvZko3c9qI+z9fu9UX5b54rP6s
        q83BzUltBJJoP9PO7tNLs91Vl1ZCKrCe1Zemcm9uivu/9aa8MNaaCTzbr+Wu3FzYAInA5nu1PxTb
        VTHf12XxUC7qVb24eEQJTecttE+8ud+3aSpnlYWzOnJWIokzkBYxzozAeCNmA0Qcw4xAJg0zsJY0
        GjNkwQytO2MSZn73kgHMJKVv1IsZz3466M1skjErMx6zzIJZtpgpBTMpF44xzJaV8LH0ioZV2l8w
        wGzRJooGaNWF3QjMIgtm0WLWKZgBiaKYtdVnzYhjRqGEjWGWGERHBLNkcnc9ErPkHJglp+dApxrS
        l90QswDrY+nFrLSJY6YghGKYjem2MAKzzYLZtpg5CTOIzksGMMO74EYxk2SMVhrSKP+lUczY6dYI
        zCYLZpNcaXCno0OUCVnZGykjGu1Hh0/ZeWYyZXd7PJqyzkJZJxcaVmsZ9WXksBLupWyRY77sdCqo
        wmOUlSYcTZmyUKbkBOicNHC90JeFUreWGWSN9LudgLIrmVOFmUSG/JelB5SnHtD0Ue4j4+q5QBGu
        3Ii2LMZHbZYuTKrhTN93Uleto3+/106qJY/PApDlpDCcbHtPCob9yLh2UsE4/k6z9CJSJiuxsioI
        6WOYzs5h2nKgQFsDGQFjojUboRrvElm6CSmSmzZAZP+AHigL8XZDWh1NVIqt9Dnd/foPQEYo3hUT
        AAA=
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
      - Tue, 23 Sep 2025 03:08:23 GMT
      Etag:
      - W/"1315-JVMI2y6FNy8PE7xdW/JuIjUDJeA"
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

This is a **config** file named `test_fmp_revenue_geographic_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.916211Z
**Generator**: World's Best Repo Book Generator v1.0
