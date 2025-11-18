# Documentation: desktop/src-tauri/tauri.conf.json

## File Metadata
- **Path**: `desktop/src-tauri/tauri.conf.json`
- **Size**: 1,729 characters, 67 lines
- **Words**: 124
- **Extension**: .json
- **Classification**: Text file

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

## High-Level Overview

This is a .json file containing 67 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.115256
- Generator: World's Best Repo Book Generator v1.0.0
