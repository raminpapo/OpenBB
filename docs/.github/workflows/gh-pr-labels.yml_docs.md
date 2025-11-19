# File Documentation: gh-pr-labels.yml

## Metadata
- **Path**: `.github/workflows/gh-pr-labels.yml`
- **Size**: 799 bytes
- **Lines**: 29
- **Category**: config
- **Extension**: .yml

---

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



---

## High-Level Overview

This is a **config** file named `gh-pr-labels.yml`.

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

**Generated**: 2025-11-19T02:15:18.749331Z
**Generator**: World's Best Repo Book Generator v1.0
