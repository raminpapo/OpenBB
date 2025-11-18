# Documentation: cli/tests/test_controllers_script_parser.py

## File Metadata
- **Path**: `cli/tests/test_controllers_script_parser.py`
- **Size**: 3,284 characters, 103 lines
- **Words**: 311
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test Script parser."""

from datetime import datetime, timedelta

import pytest
from openbb_cli.controllers.script_parser import (
    match_and_return_openbb_keyword_date,
    parse_openbb_script,
)

# pylint: disable=import-outside-toplevel, unused-variable, line-too-long


@pytest.mark.parametrize(
    "command, expected",
    [
        ("reset", True),
        ("r", True),
        ("r\n", True),
        ("restart", False),
    ],
)
def test_is_reset(command, expected):
    """Test the is_reset function."""
    from openbb_cli.controllers.script_parser import is_reset

    assert is_reset(command) == expected


def test_match_and_return_openbb_keyword_date():
    """Test the match_and_return_openbb_keyword_date function."""
    keyword = "$LASTFRIDAY"
    result = match_and_return_openbb_keyword_date(keyword)
    expected = ""
    if keyword == "$LASTFRIDAY":
        today = datetime.now()
        expected = today - timedelta(days=(today.weekday() + 3) % 7)
        if expected >= today:
            expected -= timedelta(days=7)
        expected = expected.strftime("%Y-%m-%d")
    assert result == expected


def test_parse_openbb_script_basic():
    """Test the parse_openbb_script function."""
    raw_lines = ["echo 'Hello World'"]
    error, script = parse_openbb_script(raw_lines)
    assert error == ""
    assert script == "/echo 'Hello World'"


def test_parse_openbb_script_with_variable():
    """Test the parse_openbb_script function."""
    raw_lines = ["$VAR = 2022-01-01", "echo $VAR"]
    error, script = parse_openbb_script(raw_lines)
    assert error == ""
    assert script == "/echo 2022-01-01"


def test_parse_openbb_script_with_foreach_loop():
    """Test the parse_openbb_script function."""
    raw_lines = ["foreach $$DATE in 2022-01-01,2022-01-02", "echo $$DATE", "end"]
    error, script = parse_openbb_script(raw_lines)
    assert error == ""
    assert script == "/echo 2022-01-01/echo 2022-01-02"


def test_parse_openbb_script_with_error():
    """Test the parse_openbb_script function."""
    raw_lines = ["$VAR = ", "echo $VAR"]
    error, script = parse_openbb_script(raw_lines)
    assert "Variable $VAR not given" in error


@pytest.mark.parametrize(
    "line, expected",
    [
        (
            "foreach $$VAR in 2022-01-01",
            "[red]The script has a foreach loop that doesn't terminate. Add the keyword 'end' to explicitly terminate loop[/red]",  # noqa: E501
        ),
        ("echo Hello World", ""),
        (
            "end",
            "[red]The script has a foreach loop that terminates before it gets started. Add the keyword 'foreach' to explicitly start loop[/red]",  # noqa: E501
        ),
    ],
)
def test_parse_openbb_script_foreach_errors(line, expected):
    """Test the parse_openbb_script function."""
    error, script = parse_openbb_script([line])
    assert error == expected


def test_date_keyword_last_friday():
    """Test the match_and_return_openbb_keyword_date function."""
    today = datetime.now()
    last_friday = today - timedelta(days=(today.weekday() - 4 + 7) % 7)
    if last_friday >= today:
        last_friday -= timedelta(days=7)
    expected_date = last_friday.strftime("%Y-%m-%d")
    assert match_and_return_openbb_keyword_date("$LASTFRIDAY") == expected_date

```

## High-Level Overview

Test Script parser.

from datetime import datetime, timedelta

import pytest
from openbb_cli.controllers.script_parser import (
match_and_return_openbb_keyword_date,
parse_openbb_script,
)

# pylint: disable=import-outside-toplevel, unused-variable, line-too-long


@pytest.mark.parametrize(
"command, expected",
[
("reset", True),
("r", True),
("r\n", True),
("restart", False),

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (8):
`test_is_reset`, `test_match_and_return_openbb_keyword_date`, `test_parse_openbb_script_basic`, `test_parse_openbb_script_with_variable`, `test_parse_openbb_script_with_foreach_loop`, `test_parse_openbb_script_with_error`, `test_parse_openbb_script_foreach_errors`, `test_date_keyword_last_friday`

**Imports** (6):
`datetime`, `datetime`, `pytest`, `openbb_cli.controllers.script_parser`, `openbb_cli.controllers.script_parser`, `is_reset`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_cli.controllers.script_parser`
- `openbb_cli.controllers.script_parser`

## Notes
- Generated: 2025-11-18T07:54:34.724831
- Generator: World's Best Repo Book Generator v1.0.0
