# Documentation: openbb_platform/core/openbb_core/app/deprecation.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/deprecation.py`
- **Size**: 2,521 characters, 64 lines
- **Words**: 285
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""
OpenBB-specific deprecation warnings.

This implementation was inspired from Pydantic's specific warnings and modified to suit OpenBB's needs.
"""

from openbb_core.app.version import VERSION, get_major_minor


class DeprecationSummary(str):
    """A string subclass that can be used to store deprecation metadata."""

    def __new__(cls, value: str, metadata: DeprecationWarning):
        """Create a new instance of the class."""
        obj = str.__new__(cls, value)
        setattr(obj, "metadata", metadata)
        return obj


class OpenBBDeprecationWarning(DeprecationWarning):
    """
    A OpenBB specific deprecation warning.

    This warning is raised when using deprecated functionality in OpenBB. It provides information on when the
    deprecation was introduced and the expected version in which the corresponding functionality will be removed.

    Attributes
    ----------
        message: Description of the warning.
        since: Version in what the deprecation was introduced.
        expected_removal: Version in what the corresponding functionality expected to be removed.
    """

    # The choice to use class variables is based on the potential for extending the class in future developments.
    # Example: launching Platform V5 and decide to create a subclimagine we areass named OpenBBDeprecatedSinceV4,
    # which inherits from OpenBBDeprecationWarning. In this subclass, we would set since=4.X and expected_removal=5.0.
    # It's important for these values to be defined at the class level, rather than just at the instance level,
    # to ensure consistency and clarity in our deprecation warnings across the platform.

    message: str
    since: tuple[int, int]
    expected_removal: tuple[int, int]

    def __init__(
        self,
        message: str,
        *args: object,
        since: tuple[int, int] | None = None,
        expected_removal: tuple[int, int] | None = None,
    ) -> None:
        """Initialize the warning."""
        super().__init__(message, *args)
        self.message = message.rstrip(".")
        self.since = since or get_major_minor(VERSION)
        self.expected_removal = expected_removal or (self.since[0] + 1, 0)
        self.long_message = (
            f"{self.message}. Deprecated in OpenBB Platform V{self.since[0]}.{self.since[1]}"
            f" to be removed in V{self.expected_removal[0]}.{self.expected_removal[1]}."
        )

    def __str__(self) -> str:
        """Return the warning message."""
        return self.long_message

```

## High-Level Overview


OpenBB-specific deprecation warnings.

This implementation was inspired from Pydantic's specific warnings and modified to suit OpenBB's needs.

A string subclass that can be used to store deprecation metadata.

def __new__(cls, value: str, metadata: DeprecationWarning):
Create a new instance of the class.

A OpenBB specific deprecation warning.

This warning is raised when using deprecated functionality in OpenBB. It provides information on when the
deprecation was introduced and the expected version in which the corresponding functionality will be removed.

Attributes
----------
message: Description of the warning.
since: Version in what the deprecation was introduced.
expected_removal: Version in what the corresponding functionality expected to be removed.

## Detailed Structure

### Python File Structure

**Classes** (6):
`DeprecationSummary`, `that`, `OpenBBDeprecationWarning`, `variables`, `in`, `level`

**Functions** (3):
`__new__`, `__init__`, `__str__`

**Imports** (4):
`Pydantic`, `openbb_core.app.version`, `VERSION`, `OpenBBDeprecationWarning.`


## Key Components

**Class `DeprecationSummary`**: A string subclass that can be used to store deprecation metadata.

**Class `OpenBBDeprecationWarning`**: A OpenBB specific deprecation warning.

    This warning is raised when using deprecated functionality in OpenBB. It provides information on when the
    deprecation was introduced and the expected ve

**Class `variables`**: No documentation

**Class `level`**: No documentation

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.version`

## Notes
- Generated: 2025-11-18T07:54:35.415875
- Generator: World's Best Repo Book Generator v1.0.0
