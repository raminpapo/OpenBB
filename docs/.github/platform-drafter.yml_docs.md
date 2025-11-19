# File Documentation: platform-drafter.yml

## Metadata
- **Path**: `.github/platform-drafter.yml`
- **Size**: 1,446 bytes
- **Lines**: 49
- **Category**: config
- **Extension**: .yml

---

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



---

## High-Level Overview

This is a **config** file named `platform-drafter.yml`.

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

**Generated**: 2025-11-19T02:15:18.723224Z
**Generator**: World's Best Repo Book Generator v1.0
