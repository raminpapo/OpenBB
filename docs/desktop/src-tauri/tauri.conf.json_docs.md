# File Documentation: tauri.conf.json

## Metadata
- **Path**: `desktop/src-tauri/tauri.conf.json`
- **Size**: 1,730 bytes
- **Lines**: 67
- **Category**: config
- **Extension**: .json

---

## Original Source

```json
{
  "$schema": "https://schema.tauri.app/config/2",
  "productName": "Open Data Platform by OpenBB",
  "version": "1.0.0",
  "identifier": "co.openbb.platform",
  "build": {
    "frontendDist": "../dist",
    "devUrl": "http://localhost:1470",
    "beforeDevCommand": "npm run dev",
    "beforeBuildCommand": "npm run build"
  },
  "app": {
    "windows": [
      {
        "backgroundThrottling": "disabled",
        "acceptFirstMouse": true,
        "visible": false,
        "resizable": true,
        "title": "Open Data Platform",
        "width": 1024,
        "height": 768,
        "minWidth": 740,
        "minHeight": 400,
        "skipTaskbar": false,
        "decorations": true,
        "theme": "Dark",
        "titleBarStyle": "Transparent",
        "windowClassname": "odp-window",
        "windowEffects": {
          "effects": [
            "titlebar",
            "mica"
          ]
        }
      }
    ],
    "security": {
      "csp": null,
      "capabilities": []
    }
  },
  "bundle": {
    "active": true,
    "createUpdaterArtifacts": true,
    "icon": [
      "icons/32x32.png",
      "icons/128x128.png",
      "icons/128x128@2x.png",
      "icons/icon.icns",
      "icons/icon.ico"
    ],
    "category": "DeveloperTool",
    "publisher": "OpenBB, Inc.",
    "copyright": "Copyright © 2025 OpenBB, Inc.",
    "license": "AGPLv3",
    "licenseFile": "./LICENSE"
  },
  "plugins": {
    "updater": {
      "endpoints": [
        "https://github.com/OpenBB-finance/OpenBB/releases/download/ODP/latest.json"
      ],
      "pubkey": "dW50cnVzdGVkIGNvbW1lbnQ6IG1pbmlzaWduIHB1YmxpYyBrZXk6IDEzNEQ2NzFCNjVENDhEMgpSV1RTU0YyMmNkWTBBY0IrOHRRWlVYVkZ3S1p4cmpER2RSYXZldjVEOWxFTnVueExBTXZTeUl3Ywo="
    }
  }
}

```



---

## High-Level Overview

This is a **config** file named `tauri.conf.json`.

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

**Generated**: 2025-11-19T02:16:45.408064Z
**Generator**: World's Best Repo Book Generator v1.0
