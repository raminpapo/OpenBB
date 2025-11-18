# Documentation: cli/integration/test_commands.py

## File Metadata
- **Path**: `cli/integration/test_commands.py`
- **Size**: 975 characters, 30 lines
- **Words**: 82
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
import io

import pytest
from openbb_cli.cli import main


@pytest.mark.parametrize(
    "input_values",
    [
        "/equity/price/historical --symbol aapl --provider fmp",
        "/equity/price/historical --symbol msft --provider yfinance",
        "/equity/price/historical --symbol goog --provider polygon",
        "/crypto/price/historical --symbol btc --provider fmp",
        "/currency/price/historical --symbol eur --provider fmp",
        "/derivatives/futures/historical --symbol cl --provider fmp",
        "/etf/price/historical --symbol spy --provider fmp",
        "/economy",
    ],
)
@pytest.mark.integration
def test_launch_with_cli_input(monkeypatch, input_values):
    """Test launching the CLI and providing input via stdin with multiple parameters."""
    stdin = io.StringIO(input_values)
    monkeypatch.setattr("sys.stdin", stdin)

    try:
        main()
    except Exception as e:
        pytest.fail(f"Main function raised an exception: {e}")

```

## High-Level Overview

Test launching the CLI and providing input via stdin with multiple parameters.
stdin = io.StringIO(input_values)
monkeypatch.setattr("sys.stdin", stdin)

try:
main()
except Exception as e:
pytest.fail(f"Main function raised an exception: {e}")


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`test_launch_with_cli_input`

**Imports** (4):
`io`, `pytest`, `openbb_cli.cli`, `main`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `io`
- `pytest`
- `openbb_cli.cli`

## Notes
- Generated: 2025-11-18T07:54:34.607232
- Generator: World's Best Repo Book Generator v1.0.0
