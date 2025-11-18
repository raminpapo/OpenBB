# Documentation: openbb_platform/providers/imf/openbb_imf/utils/dot_helpers.py

## File Metadata
- **Path**: `openbb_platform/providers/imf/openbb_imf/utils/dot_helpers.py`
- **Size**: 2,811 characters, 88 lines
- **Words**: 247
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Direction Of Trade Utilities."""

from openbb_core.app.model.abstract.error import OpenBBError


def load_country_map() -> dict:
    """Load IMF IRFCL country map."""
    # pylint: disable=import-outside-toplevel
    import json  # noqa
    from json.decoder import JSONDecodeError
    from pathlib import Path

    try:
        country_map_file = (
            Path(__file__).parents[1].joinpath("assets", "imf_country_map.json")
        )
        with country_map_file.open(encoding="utf-8") as file:
            country_map_dict = json.load(file)
    except (FileNotFoundError, JSONDecodeError) as e:
        raise OpenBBError(f"Failed to load IMF DOT country map: {e}") from e

    return country_map_dict


def load_country_to_code_map() -> dict:
    """Load a map of lowercase country name to 2-letter ISO symbol."""
    # pylint: disable=import-outside-toplevel
    from warnings import warn  # noqa

    try:
        return {
            (
                "euro_area"
                if k == "U2"
                else v.lower()
                .replace(".", "")
                .replace(",", "")
                .replace(":", "")
                .split("(")[0]
                .strip()
                .replace(" ", "_")
            ): k
            for k, v in load_country_map().items()
            if not k.startswith("1C_ALL")
            and "Report" not in v
            and k not in ("GW", "_X")
        }
    except OpenBBError:
        warn(f"Failed to load country to code map. -> {OpenBBError}")
        return {}


def validate_countries(countries: list[str]) -> str:
    """Validate the list of countries."""
    # pylint: disable=import-outside-toplevel
    from warnings import warn

    try:
        country_to_code_map = load_country_to_code_map()
    except OpenBBError as e:
        raise OpenBBError(f"Failed to load country to code map: {e}") from e
    if not country_to_code_map:
        raise OpenBBError("Failed to load country to code map.")

    new_countries: list = []

    for country in countries:
        if country == "all":
            return country
        if country in country_to_code_map:
            new_countries.append(country_to_code_map.get(country))
        elif country.upper() in country_to_code_map.values():
            new_countries.append(country.upper())
        elif country.lower() == "eu":
            new_countries.append(country_to_code_map.get("european_union"))
        elif country.lower() == "ea":
            new_countries.append(country_to_code_map.get("euro_area"))
        else:
            warn(f"Invalid country {country}")
            continue

    if not new_countries:
        raise OpenBBError(
            f"No valid countries found. Please choose from {list(country_to_code_map)}"
        )

    return "+".join(new_countries)

```

## High-Level Overview

Direction Of Trade Utilities.

from openbb_core.app.model.abstract.error import OpenBBError


def load_country_map() -> dict:
Load IMF IRFCL country map.
pylint: disable=import-outside-toplevel
Load a map of lowercase country name to 2-letter ISO symbol.
# pylint: disable=import-outside-toplevel
from warnings import warn  # noqa

try:
return {
(
"euro_area"
if k == "U2"
else v.lower()
.replace(".", "")
.replace(",", "")

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`load_country_map`, `load_country_to_code_map`, `validate_countries`

**Imports** (13):
`openbb_core.app.model.abstract.error`, `OpenBBError`, `json`, `json.decoder`, `JSONDecodeError`, `pathlib`, `Path`, `e`, `warnings`, `warn`, `warnings`, `warn`, `e`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.abstract.error`
- `json`
- `json.decoder`
- `pathlib`
- `warnings`
- `warnings`

## Notes
- Generated: 2025-11-18T07:54:40.020212
- Generator: World's Best Repo Book Generator v1.0.0
