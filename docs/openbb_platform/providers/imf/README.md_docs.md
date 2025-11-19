# File Documentation: README.md

## Metadata
- **Path**: `openbb_platform/providers/imf/README.md`
- **Size**: 1,232 bytes
- **Lines**: 42
- **Category**: documentation
- **Extension**: .md

---

## Original Source

```markdown
# OpenBB IMF Provider Extension

This package adds the `openbb-imf` provider extension to the OpenBB Platform.

## Installation

Install from PyPI with:

```sh
pip install openbb-imf
```

## Implementation

The extension utilizes the JSON RESTful Web Service ((https://datahelp.imf.org/knowledgebase/articles/630877-data-services)[https://datahelp.imf.org/knowledgebase/articles/630877-data-services])

No authorization is required to use, but IP addresses are bound by the limitations described in the link above.

## Coverage

- Databases:
  - International Reserves and Foreign Currency Liquidity
  - Direction of Trade Statistics
  - Financial Soundness Indicators
  - Port Watch

Coverage:
  - All IRFCL tables.
  - Individual, or multiple, time series from single or multiple countries.
  - Core and Encouraged Set tables, plus all individual underlying series.
  - Daily Port and Chokepoints data, with charts for metadata and average annual statistics.

### Endpoints

- `obb.economy.available_indicators`
- `obb.economy.indicators`
- `obb.economy.direction_of_trade`
- `obb.economy.shipping.chokepoint_info`
- `obb.economy.shipping.chokepoint_volume`
- `obb.economy.shipping.port_info`
- `obb.economy.shipping.port_volume`

```



---

## High-Level Overview

This is a **documentation** file named `README.md`.

**Documentation File**

- **Sections**: 5
- **Main Topics**: OpenBB IMF Provider Extension, Installation, Implementation, Coverage, Endpoints


---

## Detailed Analysis

### Documentation Structure

**Table of Contents**:

- OpenBB IMF Provider Extension
  - Installation
  - Implementation
  - Coverage
    - Endpoints


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.231719Z
**Generator**: World's Best Repo Book Generator v1.0
