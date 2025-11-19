# File Documentation: tauri.macos.conf.json

## Metadata
- **Path**: `desktop/src-tauri/tauri.macos.conf.json`
- **Size**: 766 bytes
- **Lines**: 35
- **Category**: config
- **Extension**: .json

---

## Original Source

```json
{
  "build": {
    "beforeBundleCommand": "sh /Users/runner/work/OpenBB/OpenBB/desktop/src-tauri/scripts/fix_dylibs.sh"
  },
  "bundle": {
    "targets": "all",
    "resources": [
      "open-data-platform-SBOM-cargo.cdx.xml",
      "open-data-platform-SBOM-npm.cdx.xml"
    ],
    "macOS": {
      "frameworks": [
        "frameworks/libcrypto.3.dylib",
        "frameworks/libssl.3.dylib"
      ],
      "dmg": {
        "appPosition": {
          "x": 180,
          "y": 170
        },
        "applicationFolderPosition": {
          "x": 480,
          "y": 170
        },
        "windowSize": {
          "height": 400,
          "width": 660
        }
      },
      "minimumSystemVersion": "10.15",
      "entitlements": "./entitlements.plist"
    }
  }
}

```



---

## High-Level Overview

This is a **config** file named `tauri.macos.conf.json`.

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

**Generated**: 2025-11-19T02:16:45.410422Z
**Generator**: World's Best Repo Book Generator v1.0
