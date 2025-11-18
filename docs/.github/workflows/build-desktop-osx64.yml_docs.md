# Documentation: .github/workflows/build-desktop-osx64.yml

## File Metadata
- **Path**: `.github/workflows/build-desktop-osx64.yml`
- **Size**: 3,979 characters, 121 lines
- **Words**: 297
- **Extension**: .yml
- **Classification**: Text file

## Original Source

```yaml
name: build-macos-x64

on:
  workflow_call:
    inputs:
      release:
        required: false
        type: boolean
        default: false
  workflow_dispatch:
    inputs:
      release:
        description: 'Set to true to create a release build'
        required: false
        type: boolean
        default: false

jobs:
  build-and-sign:
    runs-on: "macos-15-intel"
    permissions:
      contents: write
    defaults:
      run:
        working-directory: desktop
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Import Code Signing Certificate
        uses: apple-actions/import-codesign-certs@v3
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          MACOS_CERTIFICATE: ${{ secrets.MACOS_CERTIFICATE }}
          MACOS_CERTIFICATE_PWD: ${{ secrets.MACOS_CERTIFICATE_PWD }}
        with:
          p12-file-base64: ${{ secrets.MACOS_CERTIFICATE }}
          p12-password: ${{ secrets.MACOS_CERTIFICATE_PWD }}

      - name: Setup Cargo Cache
        uses: actions/cache@v4
        with:
          path: |
            ~/.cargo/registry
            ~/.cargo/git
          key: macos-x64-cargo-registry-${{ hashFiles('desktop/**/Cargo.lock') }}
          restore-keys: |
            macos-x64-cargo-registry-

      - name: Setup Node Cache
        uses: actions/cache@v4
        with:
          path: ~/.npm
          key: macos-x64-node-${{ hashFiles('desktop/**/package-lock.json') }}
          restore-keys: |
            macos-x64-node-

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: lts/*

      - name: Install cyclonedx-npm
        run: npm install -g @cyclonedx/cyclonedx-npm

      - name: install Rust stable
        uses: dtolnay/rust-toolchain@stable
        with:
          targets: "x86_64-apple-darwin"

      - name: Install Modules
        run: |
          npm install
          cyclonedx-npm --output-format XML --gather-license-texts --output-file src-tauri/open-data-platform-SBOM-npm.cdx.xml

      - name: Install cargo-cyclonedx
        run: |
          cargo install cargo-cyclonedx
          cargo cyclonedx
          if [ -f "src-tauri/openbb-platform.cdx.xml" ]; then
            mv src-tauri/openbb-platform.cdx.xml "src-tauri/open-data-platform-SBOM-cargo.cdx.xml"
          fi

      - name: Build Tauri App
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          APPLE_CERTIFICATE: ${{ secrets.MACOS_CERTIFICATE }}
          APPLE_CERTIFICATE_PASSWORD: ${{ secrets.MACOS_CERTIFICATE_PWD }}
          APPLE_ID: ${{ secrets.NOTARIZE_APPLE_ID }}
          APPLE_PASSWORD: ${{ secrets.NOTARIZE_APPLE_PWD }}
          APPLE_TEAM_ID: ${{ secrets.NOTARIZE_APPLE_TEAM_ID }}
          TAURI_SIGNING_PRIVATE_KEY: ${{ secrets.TAURI_SIGNING_PRIVATE_KEY }}
          TAURI_SIGNING_PRIVATE_KEY_PASSWORD: ${{ secrets.TAURI_SIGNING_PRIVATE_KEY_PASSWORD }}
        run: npm run tauri build

      - name: Rename artifacts
        run: |
          VERSION=$(jq -r .version src-tauri/tauri.conf.json)
          cd target/release/bundle/dmg
          for file in *.dmg; do mv "$file" "Open-Data-Platform_${VERSION}_x86_64.dmg"; done
          cd ../macos
          for file in *.app.tar.gz; do mv "$file" "Open-Data-Platform_${VERSION}_x86_64.app.tar.gz"; done
          for file in *.app.tar.gz.sig; do mv "$file" "Open-Data-Platform_${VERSION}_x86_64.app.tar.gz.sig"; done

      - name: Upload Artifacts
        uses: actions/upload-artifact@v4
        with:
          name: macos-x64-artifacts
          path: |
            desktop/target/release/bundle/dmg/*.dmg
            desktop/target/release/bundle/macos/*.app.tar.gz
            desktop/target/release/bundle/macos/*.app.tar.gz.sig

      - name: Clean old bundle artifacts
        if: always()
        run: |
          bundlePath="${{ github.workspace }}/desktop/target/release/bundle"
          if [ -d "$bundlePath" ]; then
            rm -rf "$bundlePath"
          fi

```

## High-Level Overview

This is a .yml file containing 121 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.565995
- Generator: World's Best Repo Book Generator v1.0.0
