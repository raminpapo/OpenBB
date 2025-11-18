# Documentation: openbb_platform/providers/nasdaq/tests/test_nasdaq_app.py

## File Metadata
- **Path**: `openbb_platform/providers/nasdaq/tests/test_nasdaq_app.py`
- **Size**: 2,040 characters, 64 lines
- **Words**: 198
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

App tests for Nasdaq provider.

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
Fixture to serve FastAPI app instance.
Load expected apps.json data.
current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
with open(current_dir / "record" / "expected_apps.json", encoding="utf-8") as f:

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (7):
`nasdaq_app`, `expected_apps`, `expected_widgets`, `test_app_is_fastapi_instance`, `test_app_has_routes`, `test_apps_json`, `test_widgets_json`

**Imports** (11):
`json`, `os`, `pathlib`, `Path`, `pytest`, `fastapi`, `FastAPI`, `openbb_nasdaq.app`, `main`, `openbb_platform_api.utils.widgets`, `build_json`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `json`
- `os`
- `pathlib`
- `pytest`
- `fastapi`
- `openbb_nasdaq.app`
- `openbb_platform_api.utils.widgets`

## Notes
- Generated: 2025-11-18T07:54:40.432813
- Generator: World's Best Repo Book Generator v1.0.0
