# Documentation: .github/workflows/test-unit-platform.yml

## File Metadata
- **Path**: `.github/workflows/test-unit-platform.yml`
- **Size**: 1,285 characters, 49 lines
- **Words**: 111
- **Extension**: .yml
- **Classification**: Text file

## Original Source

```yaml
name: 🚉 Unit test Platform

on:
  pull_request:
    branches:
      - develop
    paths:
      - 'openbb_platform/**'

concurrency:
    group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.sha }}
    cancel-in-progress: true

jobs:
  unit_tests:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    strategy:
        fail-fast: false

        matrix:
          python_version:
            ["3.10", "3.11", "3.12", "3.13"]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - name: Install Python ${{ matrix.python_version }}
        uses: actions/setup-python@v5
        with:
            python-version: ${{ matrix.python_version }}
            allow-prereleases: true
            cache: "pip"

      - name: Cache pip packages
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ matrix.python_version }}-${{ hashFiles('openbb_platform/poetry.lock') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Run tests
        run: |
          pip install nox
          nox -f .github/scripts/noxfile.py -s unit_test_platform --python ${{ matrix.python_version }}

```

## High-Level Overview

This is a .yml file containing 49 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.581147
- Generator: World's Best Repo Book Generator v1.0.0
