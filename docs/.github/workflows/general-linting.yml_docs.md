# Documentation: .github/workflows/general-linting.yml

## File Metadata
- **Path**: `.github/workflows/general-linting.yml`
- **Size**: 3,455 characters, 103 lines
- **Words**: 333
- **Extension**: .yml
- **Classification**: Text file

## Original Source

```yaml
name: 🧹 General Linting

env:
  PIP_DEFAULT_TIMEOUT: 100

on:
  pull_request:
    types: [opened, synchronize, edited]
  # push:
  #   branches:
  #     - "feature/*"
  #     - "hotfix/*"
  #     - "release/*"
  merge_group:
    types: [checks_requested]

# Cancel previous runs that are not yet completed.
concurrency:
  group: ${{ github.event_name }}-${{ github.repository }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  code-linting:
    name: General Code Linting
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4.1.1 # actions/checkout v3.0.2
        with:
          ref: ${{ github.event.pull_request.head.ref || github.ref }}
          repository: ${{ github.event.pull_request.head.repo.full_name || github.repository }}
          fetch-depth: 20
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Fetch base branch
        run: git fetch --no-tags --depth=20 origin ${{ github.base_ref }}

      - name: Setup Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"
          architecture: x64

      - name: Get changed files in openbb_platform for PR
        if: github.event_name == 'pull_request'
        run: |
          # "Checking PR diff"
          echo "diff_files=$(git diff --diff-filter=d --name-only origin/${{ github.base_ref }}...${{ github.head_ref }} | grep -E '^(openbb_platform|cli)/.*\.py$' | grep -v 'openbb_platform/core/openbb/package' | grep -v 'integration' | grep -v 'tests' | xargs)" >> $GITHUB_ENV
          echo $diff_files

      - uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-linting-${{ hashFiles('**/poetry.lock') }}
          restore-keys: ${{ runner.os }}-linting-${{ hashFiles('**/poetry.lock') }}

      - run: |
          pip install openbb-devtools
          pip install types-pytz types-requests types-termcolor types-tabulate types-PyYAML types-python-dateutil types-setuptools types-six
      - run: bandit -x ./tests -r . || true
      - run: codespell --ignore-words=.codespell.ignore --skip="$(tr '\n' ',' < .codespell.skip | sed 's/,$//')" --quiet-level=2
      - run: |
          # Run linters for openbb_platform | cli
          if [ -n "${{ env.diff_files }}" ]; then
            black --diff --check ${{ env.diff_files }}
            mypy ${{ env.diff_files }}  --ignore-missing-imports  --scripts-are-modules --check-untyped-defs
            pydocstyle ${{ env.diff_files }}
            pylint ${{ env.diff_files }}
            ruff check ${{ env.diff_files }}
          else
            echo "No Python files changed in openbb_platform | cli"
          fi

  markdown-link-check:
    name: Markdown Linting
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4
        name: Check out the code
      - name: Lint Code Base
        uses: docker://avtodev/markdown-lint:v1
        with:
          args: "./*.md ./changelogs/*.md ./openbb_terminal/**/*.md ./discordbot/**/*.md"

  json-yaml-validate:
    name: JSON Check
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4

      - name: json-yaml-validate
        id: json-yaml-validate
        uses: GrantBirki/json-yaml-validate@v2.0.0
        with:
          yaml_exclude_regex: "construct.yaml"
          use_gitignore: false

```

## High-Level Overview

This is a .yml file containing 103 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.572344
- Generator: World's Best Repo Book Generator v1.0.0
