# File Documentation: test_config_completer.py

## Metadata
- **Path**: `cli/tests/test_config_completer.py`
- **Size**: 2,690 bytes
- **Lines**: 79
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_config_completer.py`.

**Python Module**

- **Functions** (8): word_completer, test_word_completer_simple, test_word_completer_case_insensitive, test_word_completer_no_match, nested_completer, test_nested_completer_root_command, test_nested_completer_sub_command, test_nested_completer_no_match
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`word_completer()`**
- **`test_word_completer_simple(word_completer)`**
- **`test_word_completer_case_insensitive(word_completer)`**
- **`test_word_completer_no_match(word_completer)`**
- **`nested_completer()`**
- **`test_nested_completer_root_command(nested_completer)`**
- **`test_nested_completer_sub_command(nested_completer)`**
- **`test_nested_completer_no_match(nested_completer)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `CompleteEvent`
- `Document`
- `NestedCompleter`
- `WordCompleter`
- `openbb_cli.config.completer`
- `prompt_toolkit.completion`
- `prompt_toolkit.document`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.915560Z
**Generator**: World's Best Repo Book Generator v1.0
