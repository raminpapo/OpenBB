# File Documentation: ruff.toml

## Metadata
- **Path**: `ruff.toml`
- **Size**: 1,123 bytes
- **Lines**: 59
- **Category**: config
- **Extension**: .toml

---

## Original Source

```toml
# This is an introductory addition of ruff. We should look to adding:
# PD: pandas-vet
# All options here: https://github.com/charliermarsh/ruff#supported-rules

exclude = [
    "^openbb_platform/platform/core/openbb_core/app/static/package/.*",
    "^openbb_platform/core/openbb/package/.*",
    "^cookiecutter/*",
]

line-length = 122
target-version = "py310"
fix = true

[lint]
select = [
    "E",
    "W",
    "F",
    "Q",
    "S",
    "UP",
    "I",
    "PLC",
    "PLE",
    "PLR",
    "PLW",
    "SIM",
    "T20",
]
# These ignores should be seen as temporary solutions to problems that will NEED fixed
ignore = ["PLR2004", "PLR0913", "PLR0915", "PLC0415", "E402"]

[lint.per-file-ignores]
"**/tests/*" = ["S101"]
"*init*.py" = ["F401"]
"website/*" = ["T201", "PLR0915"]
"*integration/*" = ["S101"]

[lint.isort]
combine-as-imports = true
force-wrap-aliases = true

[lint.pylint]
max-args = 8
max-branches = 26
max-returns = 9
max-statements = 30

[lint.pydocstyle]
convention = "numpy"

[lint.flake8-import-conventions.aliases]
"matplotlib.pyplot" = "plt"
numpy = "np"
pandas = "pd"
seaborn = "sns"
openbb = "obb"

```



---

## High-Level Overview

This is a **config** file named `ruff.toml`.

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

**Generated**: 2025-11-19T02:15:18.718385Z
**Generator**: World's Best Repo Book Generator v1.0
