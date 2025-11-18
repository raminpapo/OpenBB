# Documentation: .github/PULL_REQUEST_TEMPLATE/platform_pull_request_template.md

## File Metadata
- **Path**: `.github/PULL_REQUEST_TEMPLATE/platform_pull_request_template.md`
- **Size**: 2,137 characters, 41 lines
- **Words**: 322
- **Extension**: .md
- **Classification**: Text file

## Original Source

```markdown
# Pull Request the OpenBB Platform

## Description

- [ ] Summary of the change/ bug fix.
- [ ] Link # issue, if applicable.
- [ ] Screenshot of the feature or the bug before/after fix, if applicable.
- [ ] Relevant motivation and context.
- [ ] List any dependencies that are required for this change.

## How has this been tested?

- Please describe the tests that you ran to verify your changes.
- Please provide instructions so we can reproduce.
- Please also list any relevant details for your test configuration.

- [ ] Ensure all unit and integration tests pass.
- If you modified/added command(s):
  - [ ] Ensure the command(s) execute with the expected output.
    - [ ] API.
    - [ ] Python Interface.
  - [ ] If applicable, please add new tests for the command (see [CONTRIBUTING.md](/openbb_platform/CONTRIBUTING.md) to leverage semi-automated testing).
- If a new provider was introduced or a new fetcher was added to an existing provider:
  - [ ] Ensure the existing tests pass.
  - [ ] Ensure the new provider and/or fetcher is stable and usable.
  - [ ] If applicable, please add new tests for the provider and/or fetcher (see [CONTRIBUTING.md](/openbb_platform/CONTRIBUTING.md) to leverage semi-automated testing).
- If a new provider or extension was added:
  - [ ] Update the list of [Extensions](/openbb_platform/EXTENSIONS.md).
  - [ ] Update the list of [Providers](/openbb_platform/PROVIDERS.md).
  - [ ] If it's a community extension or provider, update the [integration tests GitHub Action workflow](/.github/workflows/platform-api-integration-test.yml).

## Checklist

- [ ] I have performed a self-review of my own code.
- [ ] I have commented my code, particularly in hard-to-understand areas.
- [ ] I have adhered to the GitFlow naming convention and my branch name is in the format of `feature/feature-name` or `hotfix/hotfix-name`.
- [ ] I ensure that I am following the [CONTRIBUTING guidelines](https://github.com/OpenBB-finance/OpenBB/blob/main/CONTRIBUTING.md).
  - [ ] (If applicable) I have updated tests following [these guidelines](/openbb_platform/CONTRIBUTING.md#qa-your-extension).

</details>

```

## High-Level Overview

This is a .md file containing 41 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.554129
- Generator: World's Best Repo Book Generator v1.0.0
