# File Documentation: test_extension.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/model/test_extension.py`
- **Size**: 4,033 bytes
- **Lines**: 122
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test Extension model and its functionalities."""

import sys
import types
from types import SimpleNamespace

import pytest
from openbb_core.app.model.extension import CachedAccessor, Extension


def test_init_raises_if_invalid_configuration():
    # on_command_output False but other flags set -> should raise
    with pytest.raises(ValueError):
        Extension(
            name="bad",
            on_command_output=False,
            command_output_paths=["/some/path"],
        )

    with pytest.raises(ValueError):
        Extension(name="bad2", on_command_output=False, results_only=True)

    with pytest.raises(ValueError):
        Extension(name="bad3", on_command_output=False, immutable=False)


def test_register_accessor_registers_and_warns_on_override():
    class Dummy:
        accessors = set()

    def accessor_factory(obj):
        return SimpleNamespace(called_with=obj)

    # Register new accessor
    decorator = Extension.register_accessor("foo", Dummy)
    returned = decorator(accessor_factory)
    assert returned is accessor_factory  # decorator returns the original accessor
    assert hasattr(Dummy, "foo")
    assert "foo" in Dummy.accessors
    # descriptor instance is stored in the class __dict__; accessing via the
    # class returns the result of descriptor.__get__, so inspect __dict__
    assert isinstance(Dummy.__dict__["foo"], CachedAccessor)

    # If attribute already exists, registration should warn
    Dummy.existing = "I exist"  #  type: ignore
    with pytest.warns(UserWarning):
        Extension.register_accessor("existing", Dummy)(accessor_factory)

    # Clean up
    if "foo" in Dummy.accessors:
        Dummy.accessors.remove("foo")
    if hasattr(Dummy, "foo"):
        delattr(Dummy, "foo")
    if hasattr(Dummy, "existing"):
        delattr(Dummy, "existing")


def test_cached_accessor_descriptor_behavior_and_caching():
    class Dummy:
        accessors = set()

        def __init__(self, name="n"):
            self.name = name

    def make_accessor(obj):
        # returns an object instance to be cached on the target instance
        return SimpleNamespace(result=f"accessed-{obj.name}")

    Extension.register_accessor("myext", Dummy)(make_accessor)

    inst = Dummy("alice")
    # Accessing on instance should call accessor and cache the result on instance
    returned = inst.myext  # type: ignore  # pylint: disable=E1101
    assert isinstance(returned, SimpleNamespace)
    assert returned.result == "accessed-alice"
    # The attribute should now exist on the instance (cached)
    assert getattr(inst, "myext") is returned

    # The descriptor object itself lives in the class __dict__
    cls_attr = Dummy.__dict__["myext"]
    assert isinstance(cls_attr, CachedAccessor)

    # Clean up
    Dummy.accessors.discard("myext")
    if hasattr(Dummy, "myext"):
        delattr(Dummy, "myext")


def test_obbject_accessor_registers_on_mocked_obbject_module(monkeypatch):
    # Create a fake module to be imported in the property
    mod_name = "openbb_core.app.model.obbject"
    fake_mod = types.ModuleType(mod_name)

    class FakeOBBject:
        accessors = set()

    fake_mod.OBBject = FakeOBBject  # type: ignore

    # Install fake module into sys.modules so import inside property picks it up
    monkeypatch.setitem(sys.modules, mod_name, fake_mod)

    ext = Extension(name="ext_name")
    decorator = (
        ext.obbject_accessor
    )  # should return the register decorator for FakeOBBject

    def sample_accessor(obj):
        return SimpleNamespace(tag=f"ext-{getattr(obj,'_marker',None)}")

    decorator(sample_accessor)

    assert "ext_name" in FakeOBBject.accessors
    assert hasattr(FakeOBBject, "ext_name")
    # descriptor instance must be in the class __dict__
    assert isinstance(FakeOBBject.__dict__["ext_name"], CachedAccessor)

    # cleanup
    FakeOBBject.accessors.discard("ext_name")
    if hasattr(FakeOBBject, "ext_name"):
        delattr(FakeOBBject, "ext_name")
    monkeypatch.delitem(sys.modules, mod_name)

```



---

## High-Level Overview

This is a **python** file named `test_extension.py`.

**Python Module**

- **Classes** (7): Dummy, __dict__, returns, Dummy, __dict__, FakeOBBject, __dict__
- **Functions** (8): test_init_raises_if_invalid_configuration, test_register_accessor_registers_and_warns_on_override, accessor_factory, test_cached_accessor_descriptor_behavior_and_caching, __init__, make_accessor, test_obbject_accessor_registers_on_mocked_obbject_module, sample_accessor
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Dummy`**
- **`Dummy`**
- **`FakeOBBject`**

#### Functions

- **`test_init_raises_if_invalid_configuration()`**
- **`test_register_accessor_registers_and_warns_on_override()`**
- **`accessor_factory(obj)`**
- **`test_cached_accessor_descriptor_behavior_and_caching()`**
- **`__init__(self, name="n")`**
- **`make_accessor(obj)`**
- **`test_obbject_accessor_registers_on_mocked_obbject_module(monkeypatch)`**
- **`sample_accessor(obj)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `CachedAccessor`
- `SimpleNamespace`
- `inside`
- `openbb_core.app.model.extension`
- `pytest`
- `sys`
- `types`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.669248Z
**Generator**: World's Best Repo Book Generator v1.0
