# File Documentation: bill_text.py

## Metadata
- **Path**: `openbb_platform/providers/congress_gov/openbb_congress_gov/models/bill_text.py`
- **Size**: 4,736 bytes
- **Lines**: 145
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Congress Gov Bills Text Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class CongressBillTextQueryParams(QueryParams):
    """Congress Gov Bills Text Query."""

    __json_schema_extra__ = {
        "urls": {
            "multiple_items_allowed": True,
        }
    }
    # This field is typed this way to allow the Python interface and API
    # to easily accept the parameter.
    # In the API, the body can be a string, a list of URLs or a dictionary with a "urls" key.
    # Workspace will send the body as a dictionary with a "urls" key.
    urls: str | list[str] | dict[str, list[str]] = Field(
        description="List of direct bill URLs to download.",
        kw_only=True,
    )


class CongressBillTextData(Data):
    """Congress Gov Bills Text Data."""

    error_type: str | None = Field(
        default=None,
        description="Error type if any error occurs during the download.",
    )
    content: str = Field(
        description="Base64-encoded PDF document.",
    )
    filename: str | None = Field(
        default=None,
        description="The filename of the downloaded PDF.",
    )
    data_format: dict[str, str] | None = Field(
        default=None,
        description="Data format information, including data type and filename.",
    )


class CongressBillTextFetcher(
    Fetcher[CongressBillTextQueryParams, list[CongressBillTextData]]
):
    """Congress Gov Bills Text Fetcher."""

    require_credentials = False

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> CongressBillTextQueryParams:
        """Transform the query parameters."""

        return CongressBillTextQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: CongressBillTextQueryParams,
        credentials: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> list:
        """Extract data from the query."""
        # pylint: disable=import-outside-toplevel
        import base64  # noqa
        from io import BytesIO
        from openbb_core.provider.utils.helpers import make_request

        urls = (
            query.urls.get("urls", [])
            if isinstance(query.urls, dict)
            else (query.urls if isinstance(query.urls, list) else query.urls.split(","))
        )
        results: list = []

        for url in urls:
            filename = url.split("/")[-1]

            if "congress.gov" not in url.strip():
                results.append(
                    {
                        "error_type": "invalid_url",
                        "content": f"Invalid URL: {url}. Must be a valid Congress.gov API URL.",
                        "filename": filename,
                    }
                )
                continue
            try:
                response = make_request(url)
                response.raise_for_status()
                datatype = filename.split(".")[-1].lower()

                if datatype == "pdf":
                    pdf_content = base64.b64encode(
                        BytesIO(response.content).read()
                    ).decode("utf-8")
                    results.append(
                        {
                            "content": pdf_content,
                            "data_format": {
                                "data_type": "pdf",
                                "filename": url.split("/")[-1],
                            },
                        }
                    )
                else:
                    results.append(
                        {
                            "content": response.text,
                            "data_format": {
                                "data_type": "text",
                                "filename": filename,
                            },
                        }
                    )
            except Exception as exc:  # pylint: disable=broad-except
                results.append(
                    {
                        "error_type": "download_error",
                        "content": f"{exc.__class__.__name__}: {exc.args[0]}",
                        "filename": url.split("/")[-1],
                    }
                )
                continue

        return results

    @staticmethod
    def transform_data(
        query: CongressBillTextQueryParams,
        data: list,
        **kwargs: Any,
    ) -> list[CongressBillTextData]:
        """Transform the extracted data into the desired format."""
        return [CongressBillTextData(**item) for item in data]

```



---

## High-Level Overview

This is a **python** file named `bill_text.py`.

**Python Module**

- **Classes** (3): CongressBillTextQueryParams, CongressBillTextData, CongressBillTextFetcher
- **Functions** (3): transform_query, aextract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CongressBillTextQueryParams`**(QueryParams)
- **`CongressBillTextData`**(Data)
- **`CongressBillTextFetcher`**(
    Fetcher[CongressBillTextQueryParams, list[CongressBillTextData]]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `BytesIO`
- `Data`
- `Fetcher`
- `Field`
- `QueryParams`
- `base64`
- `io`
- `make_request`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.helpers`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.692606Z
**Generator**: World's Best Repo Book Generator v1.0
