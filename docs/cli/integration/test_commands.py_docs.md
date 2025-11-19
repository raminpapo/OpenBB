# File Documentation: test_commands.py

## Metadata
- **Path**: `cli/integration/test_commands.py`
- **Size**: 975 bytes
- **Lines**: 30
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_commands.py`.

**Python Module**

- **Functions** (1): test_launch_with_cli_input
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_launch_with_cli_input(monkeypatch, input_values)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `io`
- `main`
- `openbb_cli.cli`
- `pytest`


---

## Performance & Security Notes

### Security Considerations

- ⚠️ Uses `input()` - validate user input


---

**Generated**: 2025-11-19T02:15:18.806807Z
**Generator**: World's Best Repo Book Generator v1.0
