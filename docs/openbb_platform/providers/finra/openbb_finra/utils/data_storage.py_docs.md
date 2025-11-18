# Documentation: openbb_platform/providers/finra/openbb_finra/utils/data_storage.py

## File Metadata
- **Path**: `openbb_platform/providers/finra/openbb_finra/utils/data_storage.py`
- **Size**: 2,668 characters, 83 lines
- **Words**: 274
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Utility for FINRA data storage.

This was created as a way to handle short interest data from the FINRA.
The files do not change, so there is no need to download them every time.
"""

from openbb_core.app.utils import get_user_cache_directory
from openbb_finra.utils.helpers import get_short_interest_dates


def get_db_path():
    """Return the path to the database."""
    # pylint: disable=import-outside-toplevel
    from pathlib import Path

    DB_PATH = Path(get_user_cache_directory()) / "caches/finra_short_volume.db"
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    return DB_PATH


def get_cached_dates() -> list:
    """Return the dates that are cached in the DB file."""
    # pylint: disable=import-outside-toplevel
    import sqlite3  # noqa

    DB_PATH = get_db_path()
    cnx = sqlite3.connect(DB_PATH)
    cursor = cnx.cursor()

    # Check if the table exists
    cursor.execute(
        "SELECT * FROM sqlite_master WHERE type='table' AND name='short_interest'"
    )
    if cursor.fetchone() is None:
        # The table does not exist
        return []

    # If the table exists, fetch the data
    cursor.execute("SELECT distinct settlementDate FROM short_interest")
    result = cursor.fetchall()
    return [row[0] for row in result]


def get_data_from_date_and_store(date):
    """Get data from a specific date and place it in the cache."""
    # pylint: disable=import-outside-toplevel
    import random  # noqa
    import sqlite3  # noqa
    from io import StringIO  # noqa
    from openbb_core.provider.utils.helpers import make_request  # noqa
    from pandas import read_csv  # noqa

    DB_PATH = get_db_path()
    url = f"https://cdn.finra.org/equity/otcmarket/biweekly/shrt{date}.csv"
    # add a random string to user agent to avoid getting blocked
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        + str(random.randint(0, 9))  # noqa: S311
    }
    req = make_request(url, headers=headers, timeout=1)
    if req.status_code != 200:
        return
    data = read_csv(StringIO(req.text), delimiter="|")
    data = data.drop(
        columns=[
            "accountingYearMonthNumber",
            "issuerServicesGroupExchangeCode",
            "stockSplitFlag",
            "revisionFlag",
        ]
    )
    data.to_sql("short_interest", sqlite3.connect(DB_PATH), if_exists="append")


def prepare_data():
    """Prepare the data."""
    date_list = get_short_interest_dates()
    cached_urls = get_cached_dates()
    for date in date_list:
        if f"{date[:4]}-{date[4:6]}-{date[6:]}" not in cached_urls:
            get_data_from_date_and_store(date)

```

## High-Level Overview

Utility for FINRA data storage.

This was created as a way to handle short interest data from the FINRA.
The files do not change, so there is no need to download them every time.

Return the path to the database.
# pylint: disable=import-outside-toplevel
from pathlib import Path

DB_PATH = Path(get_user_cache_directory()) / "caches/finra_short_volume.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

return DB_PATH


def get_cached_dates() -> list:
Return the dates that are cached in the DB file.
pylint: disable=import-outside-toplevel
Check if the table exists
The table does not exist

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (4):
`get_db_path`, `get_cached_dates`, `get_data_from_date_and_store`, `prepare_data`

**Imports** (17):
`the`, `openbb_core.app.utils`, `get_user_cache_directory`, `openbb_finra.utils.helpers`, `get_short_interest_dates`, `pathlib`, `Path`, `sqlite3`, `a`, `random`, `sqlite3`, `io`, `StringIO`, `openbb_core.provider.utils.helpers`, `make_request`, `pandas`, `read_csv`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.utils`
- `openbb_finra.utils.helpers`
- `pathlib`
- `sqlite3`
- `random`
- `sqlite3`
- `io`
- `openbb_core.provider.utils.helpers`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:38.618880
- Generator: World's Best Repo Book Generator v1.0.0
