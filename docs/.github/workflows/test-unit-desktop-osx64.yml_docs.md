# File Documentation: test-unit-desktop-osx64.yml

## Metadata
- **Path**: `.github/workflows/test-unit-desktop-osx64.yml`
- **Size**: 2,056 bytes
- **Lines**: 84
- **Category**: config
- **Extension**: .yml

---

## Original Source

```yaml
name: Test macOS x64

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
  test-macos-x64:
    runs-on: macos-15-intel
    permissions:
      contents: read
    defaults:
      run:
        working-directory: desktop
    steps:
      - uses: actions/checkout@v4

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

      - name: Cache cargo registry
        uses: actions/cache@v4
        with:
          path: |
            ~/.cargo/registry
            ~/.cargo/git
          key: macos-x64-cargo-registry-${{ hashFiles('desktop/**/Cargo.lock') }}
          restore-keys: |
            macos-x64-cargo-registry-

      - name: Cache cargo build
        uses: actions/cache@v4
        with:
          path: desktop/target
          key: macos-x64-cargo-build-${{ hashFiles('desktop/**/Cargo.lock') }}
          restore-keys: |
            macos-x64-cargo-build-

      - name: Check formatting
        run: cargo fmt --all -- --check

      - name: Run clippy linter
        run: cargo clippy --all-targets --all-features -- -D warnings

      - name: Run tests
        run: cargo test --all

      - name: Cache node_modules
        uses: actions/cache@v4
        with:
          path: desktop/node_modules
          key: macos-x64-node-modules-${{ hashFiles('desktop/**/package-lock.json') }}
          restore-keys: |
            macos-x64-node-modules-

      - name: Install frontend dependencies
        run: npm ci

      - name: Lint frontend code
        run: npm run lint

      - name: Type check
        run: ./node_modules/.bin/tsc --noEmit

      - name: Run frontend tests
        run: npm run test -- --watch=false

```



---

## High-Level Overview

This is a **config** file named `test-unit-desktop-osx64.yml`.

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

**Generated**: 2025-11-19T02:15:18.752802Z
**Generator**: World's Best Repo Book Generator v1.0
