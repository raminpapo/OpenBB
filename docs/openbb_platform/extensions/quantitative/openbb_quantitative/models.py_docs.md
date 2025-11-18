# Documentation: openbb_platform/extensions/quantitative/openbb_quantitative/models.py

## File Metadata
- **Path**: `openbb_platform/extensions/quantitative/openbb_quantitative/models.py`
- **Size**: 1,152 characters, 71 lines
- **Words**: 102
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Pydantic models for Quantitative Analysis.

from pydantic import BaseModel


class TestModel(BaseModel):
Base model for QA tests.
Normality model.

kurtosis: TestModel
skewness: TestModel
jarque_bera: TestModel
shapiro_wilk: TestModel
kolmogorov_smirnov: TestModel


class ADFTestModel(TestModel):
Augmented Dickey-Fuller test model.
Kwiatkowski–Phillips–Schmidt–Shin test model.


## Detailed Structure

### Python File Structure

**Classes** (8):
`TestModel`, `NormalityModel`, `ADFTestModel`, `KPSSTestModel`, `UnitRootModel`, `OmegaModel`, `SummaryModel`, `CAPMModel`

**Functions** (0):
None

**Imports** (2):
`pydantic`, `BaseModel`


## Key Components

**Class `TestModel`**: Base model for QA tests.

**Class `NormalityModel`**: Normality model.

**Class `ADFTestModel`**: Augmented Dickey-Fuller test model.

**Class `KPSSTestModel`**: Kwiatkowski–Phillips–Schmidt–Shin test model.

**Class `UnitRootModel`**: Unit root model.

**Class `OmegaModel`**: Omega model.

**Class `SummaryModel`**: Summary model.

**Class `CAPMModel`**: CAPM model.

## Usage & Examples

See source code for usage details.

## Related Files

- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:36.313825
- Generator: World's Best Repo Book Generator v1.0.0
