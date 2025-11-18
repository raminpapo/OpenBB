# Documentation: cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/ruff.toml

## File Metadata
- **Path**: `cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/ruff.toml`
- **Size**: 804 characters, 49 lines
- **Words**: 103
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
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

This is a .toml file containing 49 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.748032
- Generator: World's Best Repo Book Generator v1.0.0
