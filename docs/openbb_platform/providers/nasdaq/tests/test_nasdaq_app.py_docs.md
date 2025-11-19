# File Documentation: test_nasdaq_app.py

## Metadata
- **Path**: `openbb_platform/providers/nasdaq/tests/test_nasdaq_app.py`
- **Size**: 2,040 bytes
- **Lines**: 64
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""App tests for Nasdaq provider."""

# flake8: noqa:E501
# pylint: disable=redefined-outer-name, unused-argument, line-too-long
import json
import os
from pathlib import Path

import pytest
from fastapi import FastAPI
from openbb_nasdaq.app import main
from openbb_platform_api.utils.widgets import build_json


@pytest.fixture(scope="module")
def nasdaq_app():
    """Fixture to serve FastAPI app instance."""
    app = main()
    yield app


@pytest.fixture(scope="module")
def expected_apps():
    """Load expected apps.json data."""
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    with open(current_dir / "record" / "expected_apps.json", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="module")
def expected_widgets():
    """Load expected widgets.json data."""
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    with open(current_dir / "record" / "expected_widgets.json", encoding="utf-8") as f:
        return json.load(f)


def test_app_is_fastapi_instance(nasdaq_app):
    """Test that the factory function returns a FastAPI instance."""
    assert isinstance(nasdaq_app, FastAPI)


def test_app_has_routes(nasdaq_app):
    """Test that the app has at least one route."""
    assert len(nasdaq_app.routes) > 0


@pytest.mark.asyncio
async def test_apps_json(nasdaq_app, expected_apps):
    """Test the /apps.json endpoint. This looks for changes and verifies the endpoint works."""
    route = [d for d in nasdaq_app.routes if d.path == "/apps.json"][0]
    response = await route.endpoint()
    assert isinstance(response, dict)
    assert response == expected_apps


def test_widgets_json(nasdaq_app, expected_widgets):
    """Test the /widgets.json endpoint. This looks for changes and verifies that the widgets are being generated correctly."""
    openapi_json: dict = nasdaq_app.openapi()
    assert isinstance(openapi_json, dict)
    response = build_json(openapi_json, [])
    assert isinstance(response, dict)
    assert response == expected_widgets

```



---

## High-Level Overview

This is a **python** file named `test_nasdaq_app.py`.

**Python Module**

- **Functions** (7): nasdaq_app, expected_apps, expected_widgets, test_app_is_fastapi_instance, test_app_has_routes, test_apps_json, test_widgets_json
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`nasdaq_app()`**
- **`expected_apps()`**
- **`expected_widgets()`**
- **`test_app_is_fastapi_instance(nasdaq_app)`**
- **`test_app_has_routes(nasdaq_app)`**
- **`test_apps_json(nasdaq_app, expected_apps)`**
- **`test_widgets_json(nasdaq_app, expected_widgets)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `FastAPI`
- `Path`
- `build_json`
- `fastapi`
- `json`
- `main`
- `openbb_nasdaq.app`
- `openbb_platform_api.utils.widgets`
- `os`
- `pathlib`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.662824Z
**Generator**: World's Best Repo Book Generator v1.0
