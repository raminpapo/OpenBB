# Documentation: .github/workflows/test-unit-desktop-osx64.yml

## File Metadata
- **Path**: `.github/workflows/test-unit-desktop-osx64.yml`
- **Size**: 2,056 characters, 84 lines
- **Words**: 183
- **Extension**: .yml
- **Classification**: Text file

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

## High-Level Overview

This is a .yml file containing 84 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.577493
- Generator: World's Best Repo Book Generator v1.0.0
