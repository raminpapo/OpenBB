# Documentation: .github/workflows/gh-pr-labels.yml

## File Metadata
- **Path**: `.github/workflows/gh-pr-labels.yml`
- **Size**: 789 characters, 29 lines
- **Words**: 84
- **Extension**: .yml
- **Classification**: Text file

## Original Source

```yaml
name: 🏷️ Pull Request Labels

on:
  pull_request:
    types: [opened, reopened, labeled, unlabeled, synchronize]

jobs:
  label:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      # - uses: mheap/github-action-required-labels@v1
      #   with:
      #     mode: minimum
      #     count: 1
      #     labels: "guides, bug, build, docker, docs, feat XS, feat S, feat M, feat L, feat XL, help wanted, refactor, tests, dependencies, release"
      - uses: mheap/github-action-required-labels@v1
        with:
          mode: exactly
          count: 0
          labels: "do not merge"

      - name: 🏷️ Label OpenBB Platform PRs
        uses: srvaroa/labeler@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```

## High-Level Overview

This is a .yml file containing 29 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.574539
- Generator: World's Best Repo Book Generator v1.0.0
