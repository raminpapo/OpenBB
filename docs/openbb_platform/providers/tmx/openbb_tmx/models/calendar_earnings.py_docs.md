# File Documentation: calendar_earnings.py

## Metadata
- **Path**: `openbb_platform/providers/tmx/openbb_tmx/models/calendar_earnings.py`
- **Size**: 5,347 bytes
- **Lines**: 148
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""TMX Earnings Calendar Model."""

# pylint: disable=unused-argument

from datetime import datetime
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.calendar_earnings import (
    CalendarEarningsData,
    CalendarEarningsQueryParams,
)
from pydantic import Field, field_validator


class TmxCalendarEarningsQueryParams(CalendarEarningsQueryParams):
    """TMX Calendar Earnings Query."""


class TmxCalendarEarningsData(CalendarEarningsData):
    """TMX Calendar Earnings Data."""

    __alias_dict__ = {
        "eps_actual": "actualEps",
        "reporting_time": "announceTime",
        "eps_consensus": "estimatedEps",
        "eps_surprise": "epsSurpriseDollar",
        "surprise_percent": "epsSurprisePercent",
        "name": "companyName",
    }

    name: str = Field(description="The company's name.")
    eps_consensus: float | None = Field(
        default=None, description="The consensus estimated EPS in dollars."
    )
    eps_actual: float | None = Field(
        default=None, description="The actual EPS in dollars."
    )
    eps_surprise: float | None = Field(
        default=None, description="The EPS surprise in dollars."
    )
    surprise_percent: float | None = Field(
        default=None,
        description="The EPS surprise as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    reporting_time: str | None = Field(
        default=None,
        description="The time of the report - i.e., before or after market.",
    )

    @field_validator("surprise_percent", mode="before", check_fields=False)
    @classmethod
    def percent_validate(cls, v):  # pylint: disable=E0213
        """Return the percent as a normalized value."""
        return float(v) / 100 if v else None


class TmxCalendarEarningsFetcher(
    Fetcher[TmxCalendarEarningsQueryParams, list[TmxCalendarEarningsData]]
):
    """Transform the query, extract and transform the data from the TMX endpoints."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> TmxCalendarEarningsQueryParams:
        """Transform the query."""
        # pylint: disable=import-outside-toplevel
        from datetime import timedelta

        transformed_params = params.copy()
        if transformed_params.get("start_date") is None:
            transformed_params["start_date"] = (
                datetime.now().date().strftime("%Y-%m-%d")
            )
        if transformed_params.get("end_date") is None:
            transformed_params["end_date"] = (
                (datetime.now() + timedelta(days=5)).date().strftime("%Y-%m-%d")
            )
        return TmxCalendarEarningsQueryParams(**transformed_params)

    @staticmethod
    async def aextract_data(
        query: TmxCalendarEarningsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the TMX endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        import json  # noqa
        from openbb_tmx.utils import gql  # noqa
        from openbb_tmx.utils.helpers import get_data_from_gql, get_random_agent  # noqa
        from pandas import date_range  # noqa

        results: list[dict] = []
        user_agent = get_random_agent()
        dates = date_range(query.start_date, end=query.end_date)

        async def create_task(date, results):
            """Create a task for a single date in the range."""
            data = []
            date = date.strftime("%Y-%m-%d")
            payload = gql.get_earnings_date_payload.copy()
            payload["variables"]["date"] = date
            url = "https://app-money.tmx.com/graphql"
            r = await get_data_from_gql(
                method="POST",
                url=url,
                data=json.dumps(payload),
                headers={
                    "Host": "app-money.tmx.com",
                    "Referer": "https://money.tmx.com/",
                    "locale": "en",
                    "Content-Type": "application/json",
                    "User-Agent": user_agent,
                    "Accept": "*/*",
                },
                timeout=3,
            )
            try:
                if (
                    "data" in r
                    and r["data"].get("getEnhancedEarningsForDate") is not None
                ):
                    data = r["data"].get("getEnhancedEarningsForDate")
                    data = [{"report_date": date, **d} for d in data]
            except Exception as e:
                raise RuntimeError(e) from e
            if len(data) > 0:
                results.extend(data)
            return results

        tasks = [create_task(date, results) for date in dates if date.weekday() < 5]

        await asyncio.gather(*tasks)

        return sorted(results, key=lambda x: x["report_date"])

    @staticmethod
    def transform_data(
        query: TmxCalendarEarningsQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[TmxCalendarEarningsData]:
        """Return the transformed data."""
        results = [{k: (None if v == "N/A" else v) for k, v in d.items()} for d in data]
        return [TmxCalendarEarningsData.model_validate(d) for d in results]

```



---

## High-Level Overview

This is a **python** file named `calendar_earnings.py`.

**Python Module**

- **Classes** (3): TmxCalendarEarningsQueryParams, TmxCalendarEarningsData, TmxCalendarEarningsFetcher
- **Functions** (5): percent_validate, transform_query, aextract_data, create_task, transform_data
- **Import Statements**: 8


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TmxCalendarEarningsQueryParams`**(CalendarEarningsQueryParams)
- **`TmxCalendarEarningsData`**(CalendarEarningsData)
- **`TmxCalendarEarningsFetcher`**(
    Fetcher[TmxCalendarEarningsQueryParams, list[TmxCalendarEarningsData]]
)

#### Functions

- **`percent_validate(cls, v)`**
- **`create_task(date, results)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Field`
- `asyncio`
- `date_range`
- `datetime`
- `get_data_from_gql`
- `gql`
- `json`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.calendar_earnings`
- `openbb_tmx.utils`
- `openbb_tmx.utils.helpers`
- `pandas`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:53.067097Z
**Generator**: World's Best Repo Book Generator v1.0
