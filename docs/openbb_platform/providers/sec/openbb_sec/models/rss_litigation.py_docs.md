# File Documentation: rss_litigation.py

## Metadata
- **Path**: `openbb_platform/providers/sec/openbb_sec/models/rss_litigation.py`
- **Size**: 3,361 bytes
- **Lines**: 99
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""SEC Litigation RSS Feed Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_sec.utils.definitions import HEADERS
from pydantic import Field


class SecRssLitigationQueryParams(QueryParams):
    """SEC Litigation RSS Feed Query.

    Source: https://sec.gov/
    """


class SecRssLitigationData(Data):
    """SEC Litigation RSS Feed Data."""

    __alias_dict__ = {
        "published": "date",
    }

    published: datetime = Field(description="The date of publication.")
    title: str = Field(description="The title of the release.")
    summary: str = Field(description="Short summary of the release.")
    id: str = Field(description="The identifier associated with the release.")
    link: str = Field(description="URL to the release.")


class SecRssLitigationFetcher(
    Fetcher[SecRssLitigationQueryParams, list[SecRssLitigationData]]
):
    """SEC RSS Litigration Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> SecRssLitigationQueryParams:
        """Transform the query."""
        return SecRssLitigationQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SecRssLitigationQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the SEC endpoint."""
        # pylint: disable=import-outside-toplevel
        import re  # noqa
        import xmltodict
        from openbb_core.provider.utils.helpers import make_request
        from pandas import DataFrame, to_datetime

        results: list = []
        url = "https://www.sec.gov/enforcement-litigation/litigation-releases/rss"
        r = make_request(url, headers=HEADERS)

        if r.status_code != 200:
            raise OpenBBError(f"Status code {r.status_code} returned.")

        def clean_xml(xml_content):
            """Clean the XML content before parsing."""
            xml_content = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;)", "&amp;", xml_content)
            return xml_content

        cleaned_content = clean_xml(r.text)
        data = xmltodict.parse(cleaned_content)
        cols = ["title", "link", "summary", "date", "id"]
        feed = DataFrame.from_records(data["rss"]["channel"]["item"])[
            ["title", "link", "description", "pubDate", "dc:creator"]
        ]
        feed.columns = cols
        feed["date"] = to_datetime(feed["date"], format="mixed")
        feed = feed.set_index("date")
        # Remove special characters
        for column in ["title", "summary"]:
            feed[column] = (
                feed[column]
                .replace(r"[^\w\s]|_", "", regex=True)
                .replace(r"\n", "", regex=True)
            )

        results = feed.reset_index().to_dict(orient="records")

        return results

    @staticmethod
    def transform_data(
        query: SecRssLitigationQueryParams, data: list[dict], **kwargs: Any
    ) -> list[SecRssLitigationData]:
        """Transform the data to the standard format."""
        return [SecRssLitigationData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `rss_litigation.py`.

**Python Module**

- **Classes** (3): SecRssLitigationQueryParams, SecRssLitigationData, SecRssLitigationFetcher
- **Functions** (4): transform_query, extract_data, clean_xml, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SecRssLitigationQueryParams`**(QueryParams)
- **`SecRssLitigationData`**(Data)
- **`SecRssLitigationFetcher`**(
    Fetcher[SecRssLitigationQueryParams, list[SecRssLitigationData]]
)

#### Functions

- **`clean_xml(xml_content)`**

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Data`
- `DataFrame`
- `Fetcher`
- `Field`
- `HEADERS`
- `OpenBBError`
- `QueryParams`
- `datetime`
- `make_request`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.helpers`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:52.003846Z
**Generator**: World's Best Repo Book Generator v1.0
