# Documentation: desktop/src-tauri/tauri.windows.conf.json

## File Metadata
- **Path**: `desktop/src-tauri/tauri.windows.conf.json`
- **Size**: 725 characters, 34 lines
- **Words**: 53
- **Extension**: .json
- **Classification**: Text file

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

## High-Level Overview

This is a .json file containing 34 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.119017
- Generator: World's Best Repo Book Generator v1.0.0
