# Documentation: ruff.toml

## File Metadata
- **Path**: `ruff.toml`
- **Size**: 1,123 characters, 59 lines
- **Words**: 131
- **Extension**: .toml
- **Classification**: Text file

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

## High-Level Overview

This is a .toml file containing 59 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:43.864382
- Generator: World's Best Repo Book Generator v1.0.0
