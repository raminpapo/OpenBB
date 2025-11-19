# File Documentation: tauri.windows.conf.json

## Metadata
- **Path**: `desktop/src-tauri/tauri.windows.conf.json`
- **Size**: 725 bytes
- **Lines**: 34
- **Category**: config
- **Extension**: .json

---

## Original Source

```json
{
  "build": {
    "beforeBundleCommand": "pwsh -File src-tauri/scripts/sign.ps1"
  },
  "plugins": {
    "updater": {
      "windows": {
        "installMode": "passive"
      }
    }
  },
  "bundle": {
    "targets": ["nsis"],
    "resources": [
      "./libcrypto-3-x64.dll",
      "./libssl-3-x64.dll",
      "./open-data-platform-SBOM-cargo.cdx.xml",
      "./open-data-platform-SBOM-npm.cdx.xml"
    ],
    "category": "Finance",
    "windows": {
      "webviewInstallMode": {
        "silent": true,
        "type": "downloadBootstrapper"
      },
      "nsis": {
        "installMode": "currentUser",
        "installerIcon": "icons/icon.ico",
        "sidebarImage": "icons/windows_vertical.bmp"
      }
    }
  }
}

```



---

## High-Level Overview

This is a **config** file named `tauri.windows.conf.json`.

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

**Generated**: 2025-11-19T02:16:45.411371Z
**Generator**: World's Best Repo Book Generator v1.0
