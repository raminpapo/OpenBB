# File Documentation: README.md

## Metadata
- **Path**: `openbb_platform/providers/tests/README.md`
- **Size**: 827 bytes
- **Lines**: 16
- **Category**: documentation
- **Extension**: .md

---

## Original Source

```markdown
# Providers unit tests

In order to automatically generate unit tests for the providers you can run the following command:

```bash
python openbb_platform/providers/tests/utils/unit_test_generator.py
```

> Note that you should be running this file from the root of the repository.

The automatic unit test generation will add unit tests for all the fetchers available in a given provider.
Each provider will have one auto generated unit test file, and inside that file there will be one unit test for each fetcher.
If the fetcher was added at a later stage compared with the generation of the test file, one can run the script again and new fetchers only will be added.

> Note that sometimes manual intervention can be needed, for example, adjusting out-of-top level imports or adding specific arguments for a given fetcher.

```



---

## High-Level Overview

This is a **documentation** file named `README.md`.

**Documentation File**

- **Sections**: 1
- **Main Topics**: Providers unit tests


---

## Detailed Analysis

### Documentation Structure

**Table of Contents**:

- Providers unit tests


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:52.979186Z
**Generator**: World's Best Repo Book Generator v1.0
