# Documentation: desktop/src-tauri/tauri.macos.conf.json

## File Metadata
- **Path**: `desktop/src-tauri/tauri.macos.conf.json`
- **Size**: 766 characters, 35 lines
- **Words**: 54
- **Extension**: .json
- **Classification**: Text file

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

## High-Level Overview

This is a .json file containing 35 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.117784
- Generator: World's Best Repo Book Generator v1.0.0
