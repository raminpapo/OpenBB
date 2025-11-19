# File Documentation: oss-gg-hack-submission.yml

## Metadata
- **Path**: `.github/ISSUE_TEMPLATE/oss-gg-hack-submission.yml`
- **Size**: 1,000 bytes
- **Lines**: 34
- **Category**: config
- **Extension**: .yml

---

## Original Source

```yaml
name: oss.gg hack submission 🕹️
description: "Submit your contribution for the for the oss.gg hackathon"
title: "[🕹️]"
labels: 🕹️ oss.gg, player submission, hacktoberfest
assignees: []
body:
  - type: textarea
    id: contribution-name
    attributes:
      label: What side quest or challenge are you solving?
      description: Add the name of the side quest or challenge.
    validations:
      required: true
  - type: textarea
    id: points
    attributes:
      label: Points
      description: How many points are assigned to this contribution?
    validations:
      required: true
  - type: textarea
    id: description
    attributes:
      label: Description
      description: What's the task your performed?
    validations:
  - type: textarea
    id: proof
    attributes:
      label: Provide proof that you've completed the task
      description: Screenshots, loom recordings, links to the content you shared or interacted with.
    validations:
      required: true

```



---

## High-Level Overview

This is a **config** file named `oss-gg-hack-submission.yml`.

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

**Generated**: 2025-11-19T02:15:18.729064Z
**Generator**: World's Best Repo Book Generator v1.0
