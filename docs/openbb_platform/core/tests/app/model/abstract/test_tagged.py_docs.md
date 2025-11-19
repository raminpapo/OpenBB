# File Documentation: test_tagged.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/model/abstract/test_tagged.py`
- **Size**: 355 bytes
- **Lines**: 19
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the Tagged model."""

from openbb_core.app.model.abstract.tagged import Tagged


def test_tagged_model():
    """Test the Tagged model."""
    tagged = Tagged()

    assert hasattr(tagged, "id")


def test_fields():
    """Test the Tagged fields."""
    fields = Tagged.model_fields
    fields_keys = fields.keys()

    assert "id" in fields_keys

```



---

## High-Level Overview

This is a **python** file named `test_tagged.py`.

**Python Module**

- **Functions** (2): test_tagged_model, test_fields
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_tagged_model()`**
- **`test_fields()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Tagged`
- `openbb_core.app.model.abstract.tagged`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.682739Z
**Generator**: World's Best Repo Book Generator v1.0
