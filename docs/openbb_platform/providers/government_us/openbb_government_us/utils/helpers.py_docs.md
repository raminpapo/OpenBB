# Documentation: openbb_platform/providers/government_us/openbb_government_us/utils/helpers.py

## File Metadata
- **Path**: `openbb_platform/providers/government_us/openbb_government_us/utils/helpers.py`
- **Size**: 296 characters, 11 lines
- **Words**: 27
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Government US Helpers."""

from random_user_agent.user_agent import UserAgent


def get_random_agent() -> str:
    """Generate a random user agent for a request."""
    user_agent_rotator = UserAgent(limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent

```

## High-Level Overview

Government US Helpers.

from random_user_agent.user_agent import UserAgent


def get_random_agent() -> str:
Generate a random user agent for a request.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`get_random_agent`

**Imports** (2):
`random_user_agent.user_agent`, `UserAgent`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `random_user_agent.user_agent`

## Notes
- Generated: 2025-11-18T07:54:39.908224
- Generator: World's Best Repo Book Generator v1.0.0
