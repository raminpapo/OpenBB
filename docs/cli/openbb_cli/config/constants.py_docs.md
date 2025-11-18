# Documentation: cli/openbb_cli/config/constants.py

## File Metadata
- **Path**: `cli/openbb_cli/config/constants.py`
- **Size**: 1,760 characters, 81 lines
- **Words**: 155
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Constants module."""

from pathlib import Path

# Paths
HOME_DIRECTORY = Path.home()
REPOSITORY_DIRECTORY = Path(__file__).parent.parent.parent.parent
SRC_DIRECTORY = Path(__file__).parent.parent
SETTINGS_DIRECTORY = HOME_DIRECTORY / ".openbb_platform"
ASSETS_DIRECTORY = SRC_DIRECTORY / "assets"
STYLES_DIRECTORY = ASSETS_DIRECTORY / "styles"
ENV_FILE_SETTINGS = SETTINGS_DIRECTORY / ".cli.env"
HIST_FILE_PROMPT = SETTINGS_DIRECTORY / ".cli.his"


DEFAULT_ROUTINES_URL = "https://openbb-cms.directus.app/items/Routines"
TIMEOUT = 30
CONNECTION_ERROR_MSG = "[red]Connection error.[/red]"
CONNECTION_TIMEOUT_MSG = "[red]Connection timeout.[/red]"
SCRIPT_TAGS = [
    "stocks",
    "crypto",
    "etf",
    "economy",
    "forex",
    "fixed income",
    "alternative",
    "funds",
    "bonds",
    "macro",
    "mutual funds",
    "equities",
    "options",
    "dark pool",
    "shorts",
    "insider",
    "behavioral analysis",
    "fundamental analysis",
    "technical analysis",
    "quantitative analysis",
    "forecasting",
    "government",
    "comparison",
    "nft",
    "on chain",
    "off chain",
    "screener",
    "report",
    "overview",
    "rates",
    "econometrics",
    "portfolio",
    "real estate",
]
AVAILABLE_FLAIRS = {
    ":openbb": "(🦋)",
    ":bug": "(🐛)",
    ":rocket": "(🚀)",
    ":diamond": "(💎)",
    ":stars": "(✨)",
    ":baseball": "(⚾)",
    ":boat": "(⛵)",
    ":phone": "(☎)",
    ":mercury": "(☿)",
    ":hidden": "",
    ":sun": "(☼)",
    ":moon": "(🌕)",
    ":nuke": "(☢)",
    ":hazard": "(☣)",
    ":tunder": "(☈)",
    ":king": "(♔)",
    ":queen": "(♕)",
    ":knight": "(♘)",
    ":recycle": "(♻)",
    ":scales": "(⚖)",
    ":ball": "(⚽)",
    ":golf": "(⛳)",
    ":peace": "(☮)",
    ":yy": "(☯)",
}

```

## High-Level Overview

Constants module.

from pathlib import Path

# Paths
HOME_DIRECTORY = Path.home()
REPOSITORY_DIRECTORY = Path(__file__).parent.parent.parent.parent
SRC_DIRECTORY = Path(__file__).parent.parent
SETTINGS_DIRECTORY = HOME_DIRECTORY / ".openbb_platform"
ASSETS_DIRECTORY = SRC_DIRECTORY / "assets"
STYLES_DIRECTORY = ASSETS_DIRECTORY / "styles"
ENV_FILE_SETTINGS = SETTINGS_DIRECTORY / ".cli.env"
HIST_FILE_PROMPT = SETTINGS_DIRECTORY / ".cli.his"


DEFAULT_ROUTINES_URL = "https://openbb-cms.directus.app/items/Routines"
TIMEOUT = 30
CONNECTION_ERROR_MSG = "[red]Connection error.[/red]"
CONNECTION_TIMEOUT_MSG = "[red]Connection timeout.[/red]"
SCRIPT_TAGS = [

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (2):
`pathlib`, `Path`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pathlib`

## Notes
- Generated: 2025-11-18T07:54:34.638122
- Generator: World's Best Repo Book Generator v1.0.0
