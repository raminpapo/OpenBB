# File Documentation: test_metadata.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/model/test_metadata.py`
- **Size**: 4,645 bytes
- **Lines**: 145
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the Metadata model."""

from datetime import datetime

import numpy as np
import pandas as pd
import pytest
from openbb_core.app.model.metadata import Metadata
from openbb_core.provider.abstract.data import Data


def test_Metadata():
    """Run Smoke test."""
    m = Metadata(
        arguments={
            "provider_choices": {},
            "standard_params": {},
            "extra_params": {},
        },
        route="test",
        timestamp=datetime.now(),
        duration=0,
    )
    assert m
    assert isinstance(m, Metadata)


def test_fields():
    """Run Smoke test."""
    fields = Metadata.model_fields.keys()
    assert "arguments" in fields
    assert "duration" in fields
    assert "route" in fields
    assert "timestamp" in fields


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        # Test cases for various input types
        ({"data": Data()}, {"data": {"type": "Data", "columns": []}}),
        (
            {"data": Data(open=123, close=456)},
            {"data": {"type": "Data", "columns": ["open", "close"]}},
        ),
        (
            {"data_list": [Data(open=123, close=456), Data(volume=789)]},
            {
                "data_list": {
                    "type": "List[Data]",
                    "columns": ["open", "volume", "close"],
                }
            },
        ),
        (
            {"data_list": [Data(open=123, close=456), Data(open=321, volume=789)]},
            {
                "data_list": {
                    "type": "List[Data]",
                    "columns": ["open", "close", "volume"],
                }
            },
        ),
        (
            {"data_frame": pd.DataFrame({"A": [1, 2], "B": [3, 4]})},
            {"data_frame": {"type": "DataFrame", "columns": ["A", "B"]}},
        ),
        (
            {
                "data_frame_list": [
                    pd.DataFrame({"A": [1, 2], "B": [3, 4]}),
                    pd.DataFrame({"C": [5, 6]}),
                ],
                "data_series_list": [
                    pd.Series([1, 2], name="X"),
                    pd.Series([3, 4], name="Y"),
                ],
            },
            {
                "data_frame_list": {
                    "type": "List[DataFrame]",
                    "columns": [["A", "B"], ["C"]],
                },
                "data_series_list": {"type": "List[Series]", "columns": ["X", "Y"]},
            },
        ),
        (
            {
                "numpy_array": np.array(
                    [(1, "Alice"), (2, "Bob")], dtype=[("id", int), ("name", "U10")]
                )
            },
            {"numpy_array": {"type": "ndarray", "columns": ["id", "name"]}},
        ),
        # Test case for long string input
        (
            {
                "long_string": "This is a very long string that exceeds 80 characters in length and should be trimmed."
            },
            {
                "long_string": "This is a very long string that exceeds 80 characters in length and should be tr"
            },
        ),
    ],
)
def test_scale_arguments(input_data, expected_output):
    """Test the scale_arguments method."""
    kwargs = {
        "provider_choices": {},
        "standard_params": {},
        "extra_params": input_data,
    }
    m = Metadata(
        arguments=kwargs,
        route="test",
        timestamp=datetime.now(),
        duration=0,
    )
    arguments = m.arguments

    for arg in arguments:  # pylint: disable=E1133
        if "columns" in arguments[arg]:
            # compare the column names disregarding the order with the expected output
            assert sorted(arguments["extra_params"][arg]["columns"]) == sorted(
                expected_output[arg]["columns"]
            )
            assert arguments[arg]["type"] == expected_output[arg]["type"]
        else:
            # assert m.arguments["extra_params"] == expected_output
            keys = list(arguments["extra_params"].keys())
            expected_keys = list(expected_output.keys())
            assert sorted(keys) == sorted(expected_keys)

            for key in keys:
                if "type" in arguments["extra_params"][key]:
                    assert (
                        arguments["extra_params"][key]["type"]
                        == expected_output[key]["type"]
                    )
                    assert sorted(arguments["extra_params"][key]["columns"]) == sorted(
                        expected_output[key]["columns"]
                    )
                else:
                    assert arguments["extra_params"][key] == expected_output[key]

```



---

## High-Level Overview

This is a **python** file named `test_metadata.py`.

**Python Module**

- **Functions** (3): test_Metadata, test_fields, test_scale_arguments
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_Metadata()`**
- **`test_fields()`**
- **`test_scale_arguments(input_data, expected_output)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Metadata`
- `datetime`
- `numpy`
- `openbb_core.app.model.metadata`
- `openbb_core.provider.abstract.data`
- `pandas`
- `pytest`


---

## Performance & Security Notes

### Security Considerations

- ⚠️ Uses `input()` - validate user input


---

**Generated**: 2025-11-19T02:16:46.671032Z
**Generator**: World's Best Repo Book Generator v1.0
