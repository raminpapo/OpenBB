# File Documentation: test_integration_tests_python.py

## Metadata
- **Path**: `openbb_platform/extensions/tests/test_integration_tests_python.py`
- **Size**: 2,671 bytes
- **Lines**: 78
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the integration tests."""

from typing import Literal

import pytest

from .utils.integration_tests_testers import (
    check_missing_integration_test_params,
    check_missing_integration_test_providers,
    check_missing_integration_tests,
    check_outdated_integration_tests,
    check_wrong_integration_test_params,
    get_integration_tests,
    get_module_functions,
)


def run_test(test_type: Literal["api", "python"], check_function) -> None:
    """Run tests helper function."""
    integration_tests = get_integration_tests(test_type=test_type)
    functions = get_module_functions(integration_tests)
    missing_items = check_function(functions)

    assert not missing_items, "\n".join(missing_items)


def test_python_interface_integration_test_providers() -> None:
    """Test if there are any missing providers for integration tests."""
    run_test("python", check_missing_integration_test_providers)


def test_python_interface_integration_test_params() -> None:
    """Test if there are any missing params for integration tests."""
    run_test("python", check_missing_integration_test_params)


def test_python_interface_wrong_integration_test_params() -> None:
    """Test if there are any wrong params for integration tests."""
    run_test("python", check_wrong_integration_test_params)


@pytest.mark.skipif(
    "openbb_charting" not in __import__("sys").modules,
    reason="Charting extension not installed",
)
def test_charting_extension_function_coverage() -> None:
    """Test if all charting extension functions are covered by integration tests."""
    from openbb_charting import Charting  # pylint: disable=import-outside-toplevel

    functions = Charting.functions()

    test_names = [f"test_charting_{func}" for func in functions]
    integration_tests_modules = get_integration_tests(
        test_type="python", filter_charting_ext=False
    )
    charting_module = [
        module for module in integration_tests_modules if "charting" in module.__name__
    ]
    integration_tests_functions = get_module_functions(charting_module)

    missing_items = [
        test for test in test_names if test not in integration_tests_functions
    ]

    assert missing_items == [], "\n".join(missing_items)


def test_missing_python_integration_tests() -> None:
    """Check if there are missing tests."""
    missing = check_missing_integration_tests(test_type="python")
    assert not missing, "\n".join(missing)


def test_outdated_python_integration_tests() -> None:
    """Check if there are outdated tests."""
    outdated = check_outdated_integration_tests(test_type="python")
    assert not outdated, "\n".join(outdated)

```



---

## High-Level Overview

This is a **python** file named `test_integration_tests_python.py`.

**Python Module**

- **Functions** (7): run_test, test_python_interface_integration_test_providers, test_python_interface_integration_test_params, test_python_interface_wrong_integration_test_params, test_charting_extension_function_coverage, test_missing_python_integration_tests, test_outdated_python_integration_tests
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure


#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `.utils.integration_tests_testers`
- `Charting`
- `Literal`
- `openbb_charting`
- `pytest`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.349183Z
**Generator**: World's Best Repo Book Generator v1.0
