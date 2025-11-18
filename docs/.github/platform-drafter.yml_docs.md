# Documentation: .github/platform-drafter.yml

## File Metadata
- **Path**: `.github/platform-drafter.yml`
- **Size**: 1,425 characters, 49 lines
- **Words**: 154
- **Extension**: .yml
- **Classification**: Text file

## Original Source

```yaml
name-template: 'OpenBB Platform v$NEXT_MINOR_VERSION'
tag-template: 'v$NEXT_MINOR_VERSION'
categories:
  - title: 🦋 OpenBB Platform Enhancements
    labels:
      - 'platform'
      - 'v4'
  - title: 🐛 OpenBB Platform Bug Fixes
    labels:
      - 'bug'
  - title: 📚 OpenBB Documentation Changes
    labels:
      - 'docs'
include-labels:
  - 'platform'
  - 'v4'
change-template: '- $TITLE @$AUTHOR (#$NUMBER)'
change-title-escapes: '\<*_&'
exclude-contributors:
  - 'jmaslek'
  - 'DidierRLopes'
  - 'deeleeramone'
  - 'hjoaquim'
  - 'jose-donato'
  - 'luqmanbello'
  - 'montezdesousa'
  - 'tehcoderer'
  - 'colin99d'
  - 'piiq'
  - 'andrewkenreich'
  - 'IgorWounds'
  - 'minhhoang1023'

template: |
  ## Thank you and welcome to our new contributors 🔥
  $CONTRIBUTORS

  ## What's new 🎉

  ## What's changed 🚀
  $CHANGES

  We are proud of our community contributors and staunch supporters of open-source ecosystems.
  Help us promote our community by tagging `@openbb_finance` on X with a link to your pull request,
  and join our Discord server to chat about your contribution! We want to hear about your experience!

  ### Links 🦋
  [Website](https://openbb.co/), [Twitter](https://twitter.com/openbb_finance), [Linkedin](https://www.linkedin.com/company/openbb-finance), [Instagram](https://www.instagram.com/openbb.finance/), [Reddit](https://www.reddit.com/r/openbb/), [Discord](https://discord.com/invite/xPHTuHCmuV)

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
- Generated: 2025-11-18T07:54:34.556713
- Generator: World's Best Repo Book Generator v1.0.0
