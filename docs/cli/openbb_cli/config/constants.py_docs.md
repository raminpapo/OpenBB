# File Documentation: constants.py

## Metadata
- **Path**: `cli/openbb_cli/config/constants.py`
- **Size**: 1,811 bytes
- **Lines**: 81
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `constants.py`.

**Python Module**

- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Path`
- `pathlib`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:15:18.849520Z
**Generator**: World's Best Repo Book Generator v1.0
