# Documentation: openbb_platform/core/tests/app/model/abstract/test_singleton.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/model/abstract/test_singleton.py`
- **Size**: 1,016 characters, 41 lines
- **Words**: 98
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tests for the SingletonMeta metaclass."""

from openbb_core.app.model.abstract.singleton import SingletonMeta


class MyClass(metaclass=SingletonMeta):
    """A simple class."""

    def __init__(self, value):
        """Initialize the class."""
        self.value = value


def test_singleton_instance_creation():
    """Test the SingletonMeta metaclass with instance creation."""
    # Arrange
    instance1 = MyClass(42)
    instance2 = MyClass(100)

    # Act & Assert
    assert instance1 is instance2
    assert instance1.value == instance2.value
    assert instance1.value == 42


def test_singleton_multiple_classes():
    """Test the SingletonMeta metaclass with multiple classes."""

    # Arrange
    class AnotherClass(metaclass=SingletonMeta):
        def __init__(self, data):
            self.data = data

    instance1 = MyClass(42)
    instance2 = AnotherClass("test")

    # Act & Assert
    assert instance1 is not instance2
    assert instance1.value == 42
    assert instance2.data == "test"

```

## High-Level Overview

Tests for the SingletonMeta metaclass.

from openbb_core.app.model.abstract.singleton import SingletonMeta


class MyClass(metaclass=SingletonMeta):
A simple class.
Initialize the class.
self.value = value


def test_singleton_instance_creation():
Test the SingletonMeta metaclass with instance creation.
Arrange
Act & Assert
Test the SingletonMeta metaclass with multiple classes.

# Arrange
class AnotherClass(metaclass=SingletonMeta):
def __init__(self, data):

## Detailed Structure

### Python File Structure

**Classes** (4):
`MyClass`, `with`, `with`, `AnotherClass`

**Functions** (4):
`__init__`, `test_singleton_instance_creation`, `test_singleton_multiple_classes`, `__init__`

**Imports** (2):
`openbb_core.app.model.abstract.singleton`, `SingletonMeta`


## Key Components

**Class `MyClass`**: A simple class.

**Class `with`**: Test the SingletonMeta metaclass with multiple classes.

**Class `AnotherClass`**: No documentation

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.abstract.singleton`

## Notes
- Generated: 2025-11-18T07:54:35.824943
- Generator: World's Best Repo Book Generator v1.0.0
