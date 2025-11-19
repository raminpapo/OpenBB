# File Documentation: test_oecd_unemployment_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/oecd/tests/record/http/test_oecd_fetchers/test_oecd_unemployment_fetcher_urllib3_v2.yaml`
- **Size**: 1,849 bytes
- **Lines**: 45
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
      - application/vnd.sdmx.data+csv; charset=utf-8
      Accept-Encoding:
      - gzip, deflate
      Connection:
      - keep-alive
    method: GET
    uri: https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_LFS@DF_IALFS_UNE_M,1.0/USA..._Z.N._T.Y_GE15..M?detail=dataonly&dimensionAtObservation=TIME_PERIOD&endPeriod=2023-06&startPeriod=2023-01
  response:
    body:
      string: "DATAFLOW,REF_AREA,MEASURE,UNIT_MEASURE,TRANSFORMATION,ADJUSTMENT,SEX,AGE,ACTIVITY,FREQ,TIME_PERIOD,OBS_VALUE,BASE_PER,OBS_STATUS,UNIT_MULT,DECIMALS\r\nOECD.SDD.TPS:DSD_LFS@DF_IALFS_UNE_M(1.0),USA,UNE_LF_M,PT_LF_SUB,_Z,N,_T,Y_GE15,_Z,M,2023-02,3.9,,,,\r\nOECD.SDD.TPS:DSD_LFS@DF_IALFS_UNE_M(1.0),USA,UNE_LF_M,PT_LF_SUB,_Z,N,_T,Y_GE15,_Z,M,2023-01,3.9,,,,\r\nOECD.SDD.TPS:DSD_LFS@DF_IALFS_UNE_M(1.0),USA,UNE_LF_M,PT_LF_SUB,_Z,N,_T,Y_GE15,_Z,M,2023-06,3.8,,,,\r\nOECD.SDD.TPS:DSD_LFS@DF_IALFS_UNE_M(1.0),USA,UNE_LF_M,PT_LF_SUB,_Z,N,_T,Y_GE15,_Z,M,2023-05,3.4,,,,\r\nOECD.SDD.TPS:DSD_LFS@DF_IALFS_UNE_M(1.0),USA,UNE_LF_M,PT_LF_SUB,_Z,N,_T,Y_GE15,_Z,M,2023-04,3.1,,,,\r\nOECD.SDD.TPS:DSD_LFS@DF_IALFS_UNE_M(1.0),USA,UNE_LF_M,PT_LF_SUB,_Z,N,_T,Y_GE15,_Z,M,2023-03,3.6,,,,\r\n"
    headers:
      Accept-Ranges:
      - values
      Cache-Control:
      - no-store,no-cache
      Content-Encoding:
      - gzip
      Content-Language:
      - en,en-US
      Content-Type:
      - application/vnd.sdmx.data+csv; charset=utf-8
      Date:
      - Thu, 27 Jun 2024 10:14:29 GMT
      Pragma:
      - no-cache
      Strict-Transport-Security:
      - max-age=2592000
      Transfer-Encoding:
      - chunked
      Vary:
      - Accept,Accept-Encoding,Accept-Encoding
      X-Server-Node:
      - Server 1
      api-supported-versions:
      - '1'
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_oecd_unemployment_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.837736Z
**Generator**: World's Best Repo Book Generator v1.0
