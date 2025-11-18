# Documentation: .github/workflows/test-unit-desktop-winARM.yml

## File Metadata
- **Path**: `.github/workflows/test-unit-desktop-winARM.yml`
- **Size**: 3,492 characters, 117 lines
- **Words**: 295
- **Extension**: .yml
- **Classification**: Text file

## Original Source

```yaml
name: Test Windows ARM64

on:
  pull_request:
    branches:
      - develop
    paths:
      - 'desktop/**'

concurrency:
    group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.sha }}
    cancel-in-progress: true

jobs:
  test-windows-arm64:
    runs-on: windows-11-arm
    permissions:
      contents: read
    defaults:
      run:
        working-directory: desktop
    env:
      VCPKG_ROOT: ${{ github.workspace }}/vcpkg
    steps:
      - uses: actions/checkout@v4

      - name: Cache vcpkg
        uses: actions/cache@v4
        with:
          path: ${{ env.VCPKG_ROOT }}
          key: ${{ runner.os }}-vcpkg-arm64-${{ hashFiles('desktop/**/vcpkg.json') }}
          restore-keys: |
            ${{ runner.os }}-vcpkg-arm64-

      - name: Bootstrap vcpkg
        working-directory: ${{ github.workspace }}
        run: |
          if (-not (Test-Path ${{ env.VCPKG_ROOT }})) {
            git clone https://github.com/microsoft/vcpkg.git ${{ env.VCPKG_ROOT }}
          }
          ${{ env.VCPKG_ROOT }}/bootstrap-vcpkg.bat
        shell: pwsh

      - name: Install OpenSSL using vcpkg
        working-directory: ${{ github.workspace }}
        run: ${{ env.VCPKG_ROOT }}/vcpkg install openssl:arm64-windows-static --vcpkg-root ${{ env.VCPKG_ROOT }}
        env:
          VCPKG_DEFAULT_TRIPLET: arm64-windows-static

      - name: Set OpenSSL env
        shell: bash
        run: |
          echo "OPENSSL_DIR=${{ env.VCPKG_ROOT }}/installed/arm64-windows-static" >> $GITHUB_ENV
          echo "OPENSSL_INCLUDE_DIR=${{ env.VCPKG_ROOT }}/installed/arm64-windows-static/include" >> $GITHUB_ENV
          echo "OPENSSL_LIB_DIR=${{ env.VCPKG_ROOT }}/installed/arm64-windows-static/lib" >> $GITHUB_ENV

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: lts/*

      - name: Set up Rust
        uses: actions-rs/toolchain@v1
        with:
          toolchain: stable
          profile: minimal
          components: clippy, rustfmt
          override: true
          target: aarch64-pc-windows-msvc

      - name: Cache cargo registry
        uses: actions/cache@v4
        with:
          path: |
            ~/.cargo/registry
            ~/.cargo/git
          key: windows-arm64-cargo-registry-${{ hashFiles('desktop/**/Cargo.lock') }}
          restore-keys: |
            windows-arm64-cargo-registry-

      - name: Cache cargo build
        uses: actions/cache@v4
        with:
          path: desktop/target
          key: windows-arm64-cargo-build-${{ hashFiles('desktop/**/Cargo.lock') }}
          restore-keys: |
            windows-arm64-cargo-build-

      - name: Check formatting
        run: cargo fmt --all -- --check

      - name: Run clippy linter
        run: cargo clippy --all-targets --all-features --target aarch64-pc-windows-msvc -- -D warnings

      - name: Run tests
        run: cargo test --all --target aarch64-pc-windows-msvc

      - name: Cache node_modules
        uses: actions/cache@v4
        with:
          path: desktop/node_modules
          key: windows-arm64-node-modules-${{ hashFiles('desktop/**/package-lock.json') }}
          restore-keys: |
            windows-arm64-node-modules-

      - name: Install frontend dependencies
        run: npm ci

      - name: Lint frontend code
        run: npm run lint

      - name: Type check
        run: ./node_modules/.bin/tsc --noEmit

      - name: Run frontend tests
        run: npm run test -- --watch=false

```

## High-Level Overview

This is a .yml file containing 117 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.580195
- Generator: World's Best Repo Book Generator v1.0.0
