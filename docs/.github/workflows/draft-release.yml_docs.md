# File Documentation: draft-release.yml

## Metadata
- **Path**: `.github/workflows/draft-release.yml`
- **Size**: 2,252 bytes
- **Lines**: 77
- **Category**: config
- **Extension**: .yml

---

## Original Source

```yaml
name: Build Desktop Draft Release

on:
  workflow_dispatch:
    inputs:
      draft:
        description: "Create as draft release"
        required: false
        default: true
        type: boolean

jobs:
  build-windows:
    uses: ./.github/workflows/build-desktop-win64.yml
    with:
      release: true
    secrets: inherit
    permissions:
      contents: write

  build-macos-arm:
    uses: ./.github/workflows/build-desktop-osxARM.yml
    with:
      release: true
    secrets: inherit
    permissions:
      contents: write

  build-macos-x64:
    uses: ./.github/workflows/build-desktop-osx64.yml
    with:
      release: true
    secrets: inherit
    permissions:
      contents: write

  publish:
    needs: [build-windows, build-macos-arm, build-macos-x64]
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Download all artifacts
        uses: actions/download-artifact@v4
        with:
          path: artifacts

      - name: Sanitize artifact filenames
        run: |
          find ./artifacts -depth -name "* *" | while read -r file; do mv "$file" "$(echo "$file" | tr ' ' '-')"; done

      - name: Extract Version and Tag
        id: extract_version
        run: |
          INSTALLER_FILE=$(find ./artifacts -name "*.exe" -o -name "*.dmg" | head -n 1)
          VERSION=$(basename "$INSTALLER_FILE" | sed -n 's/.*_\([0-9]\+\.[0-9]\+\.[0-9]\+\)_.*/\1/p')
          echo "version=$VERSION" >> $GITHUB_OUTPUT
          echo "release_name=ODP Desktop v$VERSION" >> $GITHUB_OUTPUT
          echo "versioned_tag=Open-Data-Platform-v$VERSION" >> $GITHUB_OUTPUT

      - name: Prepare assets
        id: prep_assets
        run: |
          mkdir ./release_assets
          find ./artifacts -type f -print -exec cp {} ./release_assets/ \;
          echo "assets_path=./release_assets" >> $GITHUB_OUTPUT

      - name: Create VERSIONED release
        uses: softprops/action-gh-release@v1
        with:
          tag_name: ${{ steps.extract_version.outputs.versioned_tag }}
          name: ${{ steps.extract_version.outputs.release_name }}
          files: ${{ steps.prep_assets.outputs.assets_path }}/*
          draft: true
          prerelease: false
          token: ${{ secrets.GITHUB_TOKEN }}

```



---

## High-Level Overview

This is a **config** file named `draft-release.yml`.

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

**Generated**: 2025-11-19T02:15:18.745451Z
**Generator**: World's Best Repo Book Generator v1.0
