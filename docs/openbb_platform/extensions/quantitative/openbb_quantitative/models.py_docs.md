# File Documentation: models.py

## Metadata
- **Path**: `openbb_platform/extensions/quantitative/openbb_quantitative/models.py`
- **Size**: 1,158 bytes
- **Lines**: 71
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Pydantic models for Quantitative Analysis."""

from pydantic import BaseModel


class TestModel(BaseModel):
    """Base model for QA tests."""

    statistic: float
    p_value: float


class NormalityModel(BaseModel):
    """Normality model."""

    kurtosis: TestModel
    skewness: TestModel
    jarque_bera: TestModel
    shapiro_wilk: TestModel
    kolmogorov_smirnov: TestModel


class ADFTestModel(TestModel):
    """Augmented Dickey-Fuller test model."""

    nlags: int
    nobs: int
    icbest: float


class KPSSTestModel(TestModel):
    """Kwiatkowski–Phillips–Schmidt–Shin test model."""

    nlags: int


class UnitRootModel(BaseModel):
    """Unit root model."""

    adf: ADFTestModel
    kpss: KPSSTestModel


class OmegaModel(BaseModel):
    """Omega model."""

    threshold: float
    omega: float


class SummaryModel(BaseModel):
    """Summary model."""

    count: int
    mean: float
    std: float
    var: float
    min: float
    max: float
    p_25: float
    p_50: float
    p_75: float


class CAPMModel(BaseModel):
    """CAPM model."""

    market_risk: float
    systematic_risk: float
    idiosyncratic_risk: float

```



---

## High-Level Overview

This is a **python** file named `models.py`.

**Python Module**

- **Classes** (8): TestModel, NormalityModel, ADFTestModel, KPSSTestModel, UnitRootModel, OmegaModel, SummaryModel, CAPMModel
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TestModel`**(BaseModel)
- **`NormalityModel`**(BaseModel)
- **`ADFTestModel`**(TestModel)
- **`KPSSTestModel`**(TestModel)
- **`UnitRootModel`**(BaseModel)
- **`OmegaModel`**(BaseModel)
- **`SummaryModel`**(BaseModel)
- **`CAPMModel`**(BaseModel)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.256455Z
**Generator**: World's Best Repo Book Generator v1.0
