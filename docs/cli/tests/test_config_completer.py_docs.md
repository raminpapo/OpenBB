# Documentation: cli/tests/test_config_completer.py

## File Metadata
- **Path**: `cli/tests/test_config_completer.py`
- **Size**: 2,690 characters, 79 lines
- **Words**: 227
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Config completer."""

import pytest
from openbb_cli.config.completer import WordCompleter
from prompt_toolkit.completion import CompleteEvent
from prompt_toolkit.document import Document

# pylint: disable=redefined-outer-name, import-outside-toplevel


@pytest.fixture
def word_completer():
    """Return a simple word completer."""
    words = ["test", "example", "demo"]
    return WordCompleter(words, ignore_case=True)


def test_word_completer_simple(word_completer):
    """Test the word completer with a simple word list."""
    doc = Document(text="ex", cursor_position=2)
    completions = list(word_completer.get_completions(doc, CompleteEvent()))
    assert len(completions) == 1
    assert completions[0].text == "example"


def test_word_completer_case_insensitive(word_completer):
    """Test the word completer with case-insensitive matching."""
    doc = Document(text="Ex", cursor_position=2)
    completions = list(word_completer.get_completions(doc, CompleteEvent()))
    assert len(completions) == 1
    assert completions[0].text == "example"


def test_word_completer_no_match(word_completer):
    """Test the word completer with no matches."""
    doc = Document(text="xyz", cursor_position=3)
    completions = list(word_completer.get_completions(doc, CompleteEvent()))
    assert len(completions) == 0


@pytest.fixture
def nested_completer():
    """Return a nested completer."""
    from openbb_cli.config.completer import NestedCompleter

    data = {
        "show": {
            "version": None,
            "interfaces": None,
            "clock": None,
            "ip": {"interface": {"brief": None}},
        },
        "exit": None,
        "enable": None,
    }
    return NestedCompleter.from_nested_dict(data)


def test_nested_completer_root_command(nested_completer):
    """Test the nested completer with a root command."""
    doc = Document(text="sh", cursor_position=2)
    completions = list(nested_completer.get_completions(doc, CompleteEvent()))
    assert "show" in [c.text for c in completions]


def test_nested_completer_sub_command(nested_completer):
    """Test the nested completer with a sub-command."""
    doc = Document(text="show ", cursor_position=5)
    completions = list(nested_completer.get_completions(doc, CompleteEvent()))
    assert "version" in [c.text for c in completions]
    assert "interfaces" in [c.text for c in completions]


def test_nested_completer_no_match(nested_completer):
    """Test the nested completer with no matches."""
    doc = Document(text="random ", cursor_position=7)
    completions = list(nested_completer.get_completions(doc, CompleteEvent()))
    assert len(completions) == 0

```

## High-Level Overview

Test the Config completer.

import pytest
from openbb_cli.config.completer import WordCompleter
from prompt_toolkit.completion import CompleteEvent
from prompt_toolkit.document import Document

# pylint: disable=redefined-outer-name, import-outside-toplevel


@pytest.fixture
def word_completer():
Return a simple word completer.
Test the word completer with a simple word list.
doc = Document(text="ex", cursor_position=2)
completions = list(word_completer.get_completions(doc, CompleteEvent()))
assert len(completions) == 1
assert completions[0].text == "example"



## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (8):
`word_completer`, `test_word_completer_simple`, `test_word_completer_case_insensitive`, `test_word_completer_no_match`, `nested_completer`, `test_nested_completer_root_command`, `test_nested_completer_sub_command`, `test_nested_completer_no_match`

**Imports** (9):
`pytest`, `openbb_cli.config.completer`, `WordCompleter`, `prompt_toolkit.completion`, `CompleteEvent`, `prompt_toolkit.document`, `Document`, `openbb_cli.config.completer`, `NestedCompleter`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_cli.config.completer`
- `prompt_toolkit.completion`
- `prompt_toolkit.document`
- `openbb_cli.config.completer`

## Notes
- Generated: 2025-11-18T07:54:34.710174
- Generator: World's Best Repo Book Generator v1.0.0
