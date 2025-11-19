# Comprehensive Repository Book

**Repository**: OpenBB
**Commit**: `f3344c910576ef0bc793b4759f74e27a7c1ae35c`
**Generated**: 2025-11-19T02:18:22.251996Z

---

## Introduction

This is a comprehensive book generated from the entire repository. It combines all folder documentation into a single narrative document.

---

## Table of Contents

- [Root](#root)
  - [.github](#github)
  - [assets](#assets)
  - [cli](#cli)
  - [cookiecutter](#cookiecutter)
  - [desktop](#desktop)
  - [examples](#examples)
  - [frontend-components](#frontend-components)
  - [images](#images)
  - [openbb_platform](#openbb_platform)
    - [.github/ISSUE_TEMPLATE](#github/issue_template)
    - [.github/PULL_REQUEST_TEMPLATE](#github/pull_request_template)
    - [.github/scripts](#github/scripts)
    - [.github/workflows](#github/workflows)
    - [assets/extensions](#assets/extensions)
    - [assets/scripts](#assets/scripts)
    - [cli/integration](#cli/integration)
    - [cli/openbb_cli](#cli/openbb_cli)
    - [cli/tests](#cli/tests)
    - [cookiecutter/openbb_cookiecutter](#cookiecutter/openbb_cookiecutter)
    - [desktop/public](#desktop/public)
    - [desktop/src](#desktop/src)
    - [desktop/src-tauri](#desktop/src-tauri)
    - [examples/openbb-apachebeam](#examples/openbb-apachebeam)
    - [examples/streamlit](#examples/streamlit)
    - [frontend-components/fonts](#frontend-components/fonts)
    - [frontend-components/plotly](#frontend-components/plotly)
    - [frontend-components/tables](#frontend-components/tables)
    - [images/legacy](#images/legacy)
    - [openbb_platform/core](#openbb_platform/core)
    - [openbb_platform/extensions](#openbb_platform/extensions)
    - [openbb_platform/obbject_extensions](#openbb_platform/obbject_extensions)
    - [openbb_platform/providers](#openbb_platform/providers)
    - [openbb_platform/tests](#openbb_platform/tests)
      - [cli/openbb_cli/argparse_translator](#cli/openbb_cli/argparse_translator)
      - [cli/openbb_cli/assets](#cli/openbb_cli/assets)
      - [cli/openbb_cli/config](#cli/openbb_cli/config)
      - [cli/openbb_cli/controllers](#cli/openbb_cli/controllers)
      - [cli/openbb_cli/models](#cli/openbb_cli/models)
      - [cli/openbb_cli/utils](#cli/openbb_cli/utils)
      - [cookiecutter/openbb_cookiecutter/template](#cookiecutter/openbb_cookiecutter/template)
      - [desktop/public/assets](#desktop/public/assets)
      - [desktop/src-tauri/capabilities](#desktop/src-tauri/capabilities)
      - [desktop/src-tauri/frameworks](#desktop/src-tauri/frameworks)
      - [desktop/src-tauri/gen](#desktop/src-tauri/gen)
      - [desktop/src-tauri/icons](#desktop/src-tauri/icons)
      - [desktop/src-tauri/permissions](#desktop/src-tauri/permissions)
      - [desktop/src-tauri/scripts](#desktop/src-tauri/scripts)
      - [desktop/src-tauri/src](#desktop/src-tauri/src)
      - [desktop/src/components](#desktop/src/components)
      - [desktop/src/contexts](#desktop/src/contexts)
      - [desktop/src/routes](#desktop/src/routes)
      - [desktop/src/styles](#desktop/src/styles)
      - [desktop/src/tests](#desktop/src/tests)
      - [desktop/src/utils](#desktop/src/utils)
      - [examples/openbb-apachebeam/tests](#examples/openbb-apachebeam/tests)
      - [frontend-components/plotly/src](#frontend-components/plotly/src)
      - [frontend-components/tables/src](#frontend-components/tables/src)
      - [openbb_platform/core/integration](#openbb_platform/core/integration)
      - [openbb_platform/core/openbb](#openbb_platform/core/openbb)
      - [openbb_platform/core/openbb_core](#openbb_platform/core/openbb_core)
      - [openbb_platform/core/tests](#openbb_platform/core/tests)
      - [openbb_platform/extensions/commodity](#openbb_platform/extensions/commodity)
      - [openbb_platform/extensions/crypto](#openbb_platform/extensions/crypto)
      - [openbb_platform/extensions/currency](#openbb_platform/extensions/currency)
      - [openbb_platform/extensions/derivatives](#openbb_platform/extensions/derivatives)
      - [openbb_platform/extensions/devtools](#openbb_platform/extensions/devtools)
      - [openbb_platform/extensions/econometrics](#openbb_platform/extensions/econometrics)
      - [openbb_platform/extensions/economy](#openbb_platform/extensions/economy)
      - [openbb_platform/extensions/equity](#openbb_platform/extensions/equity)
      - [openbb_platform/extensions/etf](#openbb_platform/extensions/etf)
      - [openbb_platform/extensions/famafrench](#openbb_platform/extensions/famafrench)
      - [openbb_platform/extensions/fixedincome](#openbb_platform/extensions/fixedincome)
      - [openbb_platform/extensions/index](#openbb_platform/extensions/index)
      - [openbb_platform/extensions/mcp_server](#openbb_platform/extensions/mcp_server)
      - [openbb_platform/extensions/news](#openbb_platform/extensions/news)
      - [openbb_platform/extensions/platform_api](#openbb_platform/extensions/platform_api)
      - [openbb_platform/extensions/quantitative](#openbb_platform/extensions/quantitative)
      - [openbb_platform/extensions/regulators](#openbb_platform/extensions/regulators)
      - [openbb_platform/extensions/technical](#openbb_platform/extensions/technical)
      - [openbb_platform/extensions/tests](#openbb_platform/extensions/tests)
      - [openbb_platform/extensions/uscongress](#openbb_platform/extensions/uscongress)
      - [openbb_platform/obbject_extensions/charting](#openbb_platform/obbject_extensions/charting)
      - [openbb_platform/providers/alpha_vantage](#openbb_platform/providers/alpha_vantage)
      - [openbb_platform/providers/benzinga](#openbb_platform/providers/benzinga)
      - [openbb_platform/providers/biztoc](#openbb_platform/providers/biztoc)
      - [openbb_platform/providers/bls](#openbb_platform/providers/bls)
      - [openbb_platform/providers/cboe](#openbb_platform/providers/cboe)
      - [openbb_platform/providers/cftc](#openbb_platform/providers/cftc)
      - [openbb_platform/providers/congress_gov](#openbb_platform/providers/congress_gov)
      - [openbb_platform/providers/deribit](#openbb_platform/providers/deribit)
      - [openbb_platform/providers/ecb](#openbb_platform/providers/ecb)
      - [openbb_platform/providers/econdb](#openbb_platform/providers/econdb)
      - [openbb_platform/providers/eia](#openbb_platform/providers/eia)
      - [openbb_platform/providers/famafrench](#openbb_platform/providers/famafrench)
      - [openbb_platform/providers/federal_reserve](#openbb_platform/providers/federal_reserve)
      - [openbb_platform/providers/finra](#openbb_platform/providers/finra)
      - [openbb_platform/providers/finviz](#openbb_platform/providers/finviz)
      - [openbb_platform/providers/fmp](#openbb_platform/providers/fmp)
      - [openbb_platform/providers/fred](#openbb_platform/providers/fred)

---



## Chapter: Root


**Path**: `.`

---

## Purpose & Role

This is the **root directory** of the project. It contains top-level configuration files, documentation, and entry points.


---

## Contents Summary

This folder contains **16 files** across **4 categories**:

- **Config**: 4 files (4.5 KB)
- **Documentation**: 3 files (16.3 KB)
- **Python**: 1 files (9.3 KB)
- **Text**: 8 files (53.9 KB)

**Subdirectories**: 8


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Configuration**: Contains configuration management
- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.500919Z


---



## Chapter: .github


**Path**: `.github`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `.github`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Config**: 3 files (3.3 KB)
- **Documentation**: 1 files (332.0 B)

**Subdirectories**: 4


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.508352Z


---



## Chapter: assets


**Path**: `assets`

---

## Purpose & Role

This folder contains **static assets and resources** used by the project.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Documentation**: 1 files (248.0 B)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.524362Z


---



## Chapter: cli


**Path**: `cli`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `cli`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (766.0 B)
- **Documentation**: 1 files (1.9 KB)
- **Text**: 1 files (525.6 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.531392Z


---



## Chapter: cookiecutter


**Path**: `cookiecutter`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `cookiecutter`.


---

## Contents Summary

This folder contains **4 files** across **3 categories**:

- **Config**: 2 files (989.0 B)
- **Documentation**: 1 files (2.2 KB)
- **Text**: 1 files (195.0 B)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.572473Z


---



## Chapter: desktop


**Path**: `desktop`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `desktop`.


---

## Contents Summary

This folder contains **15 files** across **5 categories**:

- **Config**: 5 files (401.9 KB)
- **Documentation**: 1 files (3.7 KB)
- **Javascript**: 4 files (2.2 KB)
- **Text**: 4 files (284.5 KB)
- **Web**: 1 files (390.0 B)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Configuration**: Contains configuration management


---

**Generated**: 2025-11-19T02:17:16.603415Z


---



## Chapter: examples


**Path**: `examples`

---

## Purpose & Role

This folder contains **examples and demonstrations** of how to use the project.


---

## Contents Summary

This folder contains **25 files** across **4 categories**:

- **Binary**: 5 files (113.3 KB)
- **Config**: 1 files (3.3 KB)
- **Documentation**: 1 files (3.3 KB)
- **Text**: 18 files (7.0 MB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities


---

**Generated**: 2025-11-19T02:17:16.672346Z


---



## Chapter: frontend-components


**Path**: `frontend-components`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `frontend-components`.


---

## Contents Summary

This folder contains **0 files** across **0 categories**:


**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.691665Z


---



## Chapter: images


**Path**: `images`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `images`.


---

## Contents Summary

This folder contains **16 files** across **1 categories**:

- **Binary**: 16 files (37.0 MB)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.735997Z


---



## Chapter: openbb_platform


**Path**: `openbb_platform`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_platform`.


---

## Contents Summary

This folder contains **6 files** across **4 categories**:

- **Config**: 1 files (3.5 KB)
- **Documentation**: 2 files (48.8 KB)
- **Python**: 2 files (10.1 KB)
- **Text**: 1 files (509.9 KB)

**Subdirectories**: 4


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.738508Z


---



## Chapter: .github/ISSUE_TEMPLATE


**Path**: `.github/ISSUE_TEMPLATE`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `issue_template`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Config**: 1 files (1000.0 B)
- **Documentation**: 3 files (2.0 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.510824Z


---



## Chapter: .github/PULL_REQUEST_TEMPLATE


**Path**: `.github/PULL_REQUEST_TEMPLATE`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `pull_request_template`.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Documentation**: 3 files (5.0 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.513244Z


---



## Chapter: .github/scripts


**Path**: `.github/scripts`

---

## Purpose & Role

This folder contains **utility scripts and tools** for development and maintenance.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Python**: 3 files (9.7 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:16.515582Z


---



## Chapter: .github/workflows


**Path**: `.github/workflows`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `workflows`.


---

## Contents Summary

This folder contains **16 files** across **2 categories**:

- **Config**: 15 files (51.3 KB)
- **Documentation**: 1 files (6.0 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities


---

**Generated**: 2025-11-19T02:17:16.517880Z


---



## Chapter: assets/extensions


**Path**: `assets/extensions`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `extensions`.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Config**: 3 files (22.5 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.525958Z


---



## Chapter: assets/scripts


**Path**: `assets/scripts`

---

## Purpose & Role

This folder contains **utility scripts and tools** for development and maintenance.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (4.2 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.528960Z


---



## Chapter: cli/integration


**Path**: `cli/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **5 files** across **1 categories**:

- **Python**: 5 files (8.8 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 5 Python source files


---

**Generated**: 2025-11-19T02:17:16.534192Z


---



## Chapter: cli/openbb_cli


**Path**: `cli/openbb_cli`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_cli`.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Python**: 3 files (3.9 KB)

**Subdirectories**: 5


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:16.537185Z


---



## Chapter: cli/tests


**Path**: `cli/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.

Contains a substantial Python codebase with 19 Python files.


---

## Contents Summary

This folder contains **19 files** across **1 categories**:

- **Python**: 19 files (59.2 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Models**: Contains data models or model definitions
- **Utilities**: Contains utility and helper functions
- **Configuration**: Contains configuration management
- **Python Modules**: 19 Python source files


---

**Generated**: 2025-11-19T02:17:16.565431Z


---



## Chapter: cookiecutter/openbb_cookiecutter


**Path**: `cookiecutter/openbb_cookiecutter`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_cookiecutter`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (2.2 KB)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.574664Z


---



## Chapter: desktop/public


**Path**: `desktop/public`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `public`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.609950Z


---



## Chapter: desktop/src


**Path**: `desktop/src`

---

## Purpose & Role

This folder contains the **source code** for the project.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Javascript**: 3 files (7.6 KB)
- **Web**: 1 files (13.9 KB)

**Subdirectories**: 6


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.614423Z


---



## Chapter: desktop/src-tauri


**Path**: `desktop/src-tauri`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `src-tauri`.


---

## Contents Summary

This folder contains **13 files** across **3 categories**:

- **Binary**: 2 files (8.3 MB)
- **Config**: 5 files (6.0 KB)
- **Text**: 6 files (4.1 MB)

**Subdirectories**: 7


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.617216Z


---



## Chapter: examples/openbb-apachebeam


**Path**: `examples/openbb-apachebeam`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb-apachebeam`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Documentation**: 2 files (644.0 B)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.685928Z


---



## Chapter: examples/streamlit


**Path**: `examples/streamlit`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `streamlit`.


---

## Contents Summary

This folder contains **2 files** across **2 categories**:

- **Documentation**: 1 files (30.0 B)
- **Python**: 1 files (18.4 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.689739Z


---



## Chapter: frontend-components/fonts


**Path**: `frontend-components/fonts`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `fonts`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Binary**: 2 files (562.4 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.693058Z


---



## Chapter: frontend-components/plotly


**Path**: `frontend-components/plotly`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `plotly`.


---

## Contents Summary

This folder contains **10 files** across **5 categories**:

- **Config**: 4 files (235.4 KB)
- **Documentation**: 1 files (3.3 KB)
- **Javascript**: 1 files (530.0 B)
- **Text**: 3 files (1.1 KB)
- **Web**: 1 files (1.4 KB)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Configuration**: Contains configuration management


---

**Generated**: 2025-11-19T02:17:16.694428Z


---



## Chapter: frontend-components/tables


**Path**: `frontend-components/tables`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `tables`.


---

## Contents Summary

This folder contains **9 files** across **4 categories**:

- **Config**: 4 files (276.0 KB)
- **Javascript**: 1 files (534.0 B)
- **Text**: 3 files (1.1 KB)
- **Web**: 1 files (1.4 KB)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Configuration**: Contains configuration management


---

**Generated**: 2025-11-19T02:17:16.714925Z


---



## Chapter: images/legacy


**Path**: `images/legacy`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `legacy`.


---

## Contents Summary

This folder contains **12 files** across **1 categories**:

- **Binary**: 12 files (2.0 MB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.737179Z


---



## Chapter: openbb_platform/core


**Path**: `openbb_platform/core`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `core`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (821.0 B)
- **Documentation**: 1 files (2.2 KB)
- **Python**: 1 files (26.0 B)
- **Text**: 1 files (206.1 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.743303Z


---



## Chapter: openbb_platform/extensions


**Path**: `openbb_platform/extensions`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `extensions`.


---

## Contents Summary

This folder contains **2 files** across **2 categories**:

- **Documentation**: 1 files (103.0 B)
- **Python**: 1 files (34.0 B)

**Subdirectories**: 19


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.938297Z


---



## Chapter: openbb_platform/obbject_extensions


**Path**: `openbb_platform/obbject_extensions`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `obbject_extensions`.


---

## Contents Summary

This folder contains **0 files** across **0 categories**:


**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.199118Z


---



## Chapter: openbb_platform/providers


**Path**: `openbb_platform/providers`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `providers`.


---

## Contents Summary

This folder contains **2 files** across **2 categories**:

- **Documentation**: 1 files (848.0 B)
- **Python**: 1 files (33.0 B)

**Subdirectories**: 34


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.243447Z


---



## Chapter: openbb_platform/tests


**Path**: `openbb_platform/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Python**: 3 files (6.7 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:18.093560Z


---



## Chapter: cli/openbb_cli/argparse_translator


**Path**: `cli/openbb_cli/argparse_translator`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `argparse_translator`.


---

## Contents Summary

This folder contains **7 files** across **1 categories**:

- **Python**: 7 files (39.6 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Utilities**: Contains utility and helper functions
- **Python Modules**: 7 Python source files


---

**Generated**: 2025-11-19T02:17:16.539349Z


---



## Chapter: cli/openbb_cli/assets


**Path**: `cli/openbb_cli/assets`

---

## Purpose & Role

This folder contains **static assets and resources** used by the project.


---

## Contents Summary

This folder contains **0 files** across **0 categories**:


**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.542708Z


---



## Chapter: cli/openbb_cli/config


**Path**: `cli/openbb_cli/config`

---

## Purpose & Role

This folder contains **configuration files** for the project.


---

## Contents Summary

This folder contains **7 files** across **1 categories**:

- **Python**: 7 files (31.2 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 7 Python source files


---

**Generated**: 2025-11-19T02:17:16.554059Z


---



## Chapter: cli/openbb_cli/controllers


**Path**: `cli/openbb_cli/controllers`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `controllers`.


---

## Contents Summary

This folder contains **8 files** across **1 categories**:

- **Python**: 8 files (149.1 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Utilities**: Contains utility and helper functions
- **Python Modules**: 8 Python source files


---

**Generated**: 2025-11-19T02:17:16.557489Z


---



## Chapter: cli/openbb_cli/models


**Path**: `cli/openbb_cli/models`

---

## Purpose & Role

This folder contains **data models and schemas** for the project.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (5.3 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.562162Z


---



## Chapter: cli/openbb_cli/utils


**Path**: `cli/openbb_cli/utils`

---

## Purpose & Role

This folder contains **utility functions and helper code** used throughout the project.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (1.0 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Utilities**: Contains utility and helper functions
- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.563765Z


---



## Chapter: cookiecutter/openbb_cookiecutter/template


**Path**: `cookiecutter/openbb_cookiecutter/template`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `template`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Config**: 1 files (335.0 B)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.576478Z


---



## Chapter: desktop/public/assets


**Path**: `desktop/public/assets`

---

## Purpose & Role

This folder contains **static assets and resources** used by the project.


---

## Contents Summary

This folder contains **0 files** across **0 categories**:


**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.611425Z


---



## Chapter: desktop/src-tauri/capabilities


**Path**: `desktop/src-tauri/capabilities`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `capabilities`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Config**: 2 files (2.1 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.623808Z


---



## Chapter: desktop/src-tauri/frameworks


**Path**: `desktop/src-tauri/frameworks`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `frameworks`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Binary**: 2 files (11.8 MB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.625813Z


---



## Chapter: desktop/src-tauri/gen


**Path**: `desktop/src-tauri/gen`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `gen`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.627138Z


---



## Chapter: desktop/src-tauri/icons


**Path**: `desktop/src-tauri/icons`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `icons`.


---

## Contents Summary

This folder contains **19 files** across **1 categories**:

- **Binary**: 19 files (404.5 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.628579Z


---



## Chapter: desktop/src-tauri/permissions


**Path**: `desktop/src-tauri/permissions`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `permissions`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.629884Z


---



## Chapter: desktop/src-tauri/scripts


**Path**: `desktop/src-tauri/scripts`

---

## Purpose & Role

This folder contains **utility scripts and tools** for development and maintenance.


---

## Contents Summary

This folder contains **2 files** across **2 categories**:

- **Shell**: 1 files (2.1 KB)
- **Text**: 1 files (1.1 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.631211Z


---



## Chapter: desktop/src-tauri/src


**Path**: `desktop/src-tauri/src`

---

## Purpose & Role

This folder contains the **source code** for the project.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Text**: 2 files (64.3 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.633109Z


---



## Chapter: desktop/src/components


**Path**: `desktop/src/components`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `components`.


---

## Contents Summary

This folder contains **10 files** across **1 categories**:

- **Javascript**: 10 files (340.1 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.646697Z


---



## Chapter: desktop/src/contexts


**Path**: `desktop/src/contexts`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `contexts`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Javascript**: 1 files (1.0 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.651147Z


---



## Chapter: desktop/src/routes


**Path**: `desktop/src/routes`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `routes`.


---

## Contents Summary

This folder contains **10 files** across **1 categories**:

- **Javascript**: 10 files (324.7 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **API**: Contains API-related code


---

**Generated**: 2025-11-19T02:17:16.653012Z


---



## Chapter: desktop/src/styles


**Path**: `desktop/src/styles`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `styles`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Web**: 1 files (1.8 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.658339Z


---



## Chapter: desktop/src/tests


**Path**: `desktop/src/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Javascript**: 2 files (1017.0 B)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Utilities**: Contains utility and helper functions


---

**Generated**: 2025-11-19T02:17:16.660060Z


---



## Chapter: desktop/src/utils


**Path**: `desktop/src/utils`

---

## Purpose & Role

This folder contains **utility functions and helper code** used throughout the project.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Javascript**: 1 files (184.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.670440Z


---



## Chapter: examples/openbb-apachebeam/tests


**Path**: `examples/openbb-apachebeam/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (1.8 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.687853Z


---



## Chapter: frontend-components/plotly/src


**Path**: `frontend-components/plotly/src`

---

## Purpose & Role

This folder contains the **source code** for the project.


---

## Contents Summary

This folder contains **3 files** across **2 categories**:

- **Javascript**: 2 files (4.0 KB)
- **Web**: 1 files (11.0 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.698633Z


---



## Chapter: frontend-components/tables/src


**Path**: `frontend-components/tables/src`

---

## Purpose & Role

This folder contains the **source code** for the project.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Javascript**: 3 files (3.1 KB)
- **Web**: 1 files (4.4 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.719272Z


---



## Chapter: openbb_platform/core/integration


**Path**: `openbb_platform/core/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (2.5 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.746075Z


---



## Chapter: openbb_platform/core/openbb


**Path**: `openbb_platform/core/openbb`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb`.


---

## Contents Summary

This folder contains **2 files** across **2 categories**:

- **Python**: 1 files (1.4 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.747995Z


---



## Chapter: openbb_platform/core/openbb_core


**Path**: `openbb_platform/core/openbb_core`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_core`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Python**: 3 files (7.9 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:16.753556Z


---



## Chapter: openbb_platform/core/tests


**Path**: `openbb_platform/core/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **0 files** across **0 categories**:


**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.878533Z


---



## Chapter: openbb_platform/extensions/commodity


**Path**: `openbb_platform/extensions/commodity`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `commodity`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (504.0 B)
- **Documentation**: 1 files (336.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.940355Z


---



## Chapter: openbb_platform/extensions/crypto


**Path**: `openbb_platform/extensions/crypto`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `crypto`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (587.0 B)
- **Documentation**: 1 files (334.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.949301Z


---



## Chapter: openbb_platform/extensions/currency


**Path**: `openbb_platform/extensions/currency`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `currency`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (607.0 B)
- **Documentation**: 1 files (331.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.959835Z


---



## Chapter: openbb_platform/extensions/derivatives


**Path**: `openbb_platform/extensions/derivatives`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `derivatives`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (637.0 B)
- **Documentation**: 1 files (289.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.970862Z


---



## Chapter: openbb_platform/extensions/devtools


**Path**: `openbb_platform/extensions/devtools`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `devtools`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (844.0 B)
- **Documentation**: 1 files (604.0 B)
- **Text**: 1 files (349.5 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.984754Z


---



## Chapter: openbb_platform/extensions/econometrics


**Path**: `openbb_platform/extensions/econometrics`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `econometrics`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (747.0 B)
- **Documentation**: 1 files (325.0 B)
- **Text**: 1 files (278.2 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.991371Z


---



## Chapter: openbb_platform/extensions/economy


**Path**: `openbb_platform/extensions/economy`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `economy`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (597.0 B)
- **Documentation**: 1 files (338.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.001837Z


---



## Chapter: openbb_platform/extensions/equity


**Path**: `openbb_platform/extensions/equity`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `equity`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (587.0 B)
- **Documentation**: 1 files (815.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.018677Z


---



## Chapter: openbb_platform/extensions/etf


**Path**: `openbb_platform/extensions/etf`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `etf`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (557.0 B)
- **Documentation**: 1 files (225.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.048807Z


---



## Chapter: openbb_platform/extensions/famafrench


**Path**: `openbb_platform/extensions/famafrench`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `famafrench`.


---

## Contents Summary

This folder contains **0 files** across **0 categories**:


**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.060699Z


---



## Chapter: openbb_platform/extensions/fixedincome


**Path**: `openbb_platform/extensions/fixedincome`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `fixedincome`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (638.0 B)
- **Documentation**: 1 files (429.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.064794Z


---



## Chapter: openbb_platform/extensions/index


**Path**: `openbb_platform/extensions/index`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `index`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (577.0 B)
- **Documentation**: 1 files (337.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.083211Z


---



## Chapter: openbb_platform/extensions/mcp_server


**Path**: `openbb_platform/extensions/mcp_server`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `mcp_server`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (620.0 B)
- **Documentation**: 1 files (26.2 KB)
- **Text**: 1 files (299.7 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.093669Z


---



## Chapter: openbb_platform/extensions/news


**Path**: `openbb_platform/extensions/news`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `news`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (474.0 B)
- **Documentation**: 1 files (297.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.121758Z


---



## Chapter: openbb_platform/extensions/platform_api


**Path**: `openbb_platform/extensions/platform_api`

---

## Purpose & Role

This folder contains **API-related code**, including endpoints, handlers, and API utilities.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (712.0 B)
- **Documentation**: 1 files (23.3 KB)
- **Text**: 1 files (209.1 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.130483Z


---



## Chapter: openbb_platform/extensions/quantitative


**Path**: `openbb_platform/extensions/quantitative`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `quantitative`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (560.0 B)
- **Documentation**: 1 files (481.0 B)
- **Text**: 1 files (228.6 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.147926Z


---



## Chapter: openbb_platform/extensions/regulators


**Path**: `openbb_platform/extensions/regulators`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `regulators`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (529.0 B)
- **Documentation**: 1 files (347.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.164423Z


---



## Chapter: openbb_platform/extensions/technical


**Path**: `openbb_platform/extensions/technical`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `technical`.


---

## Contents Summary

This folder contains **3 files** across **3 categories**:

- **Config**: 1 files (679.0 B)
- **Documentation**: 1 files (482.0 B)
- **Text**: 1 files (235.8 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.175240Z


---



## Chapter: openbb_platform/extensions/tests


**Path**: `openbb_platform/extensions/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **6 files** across **1 categories**:

- **Python**: 6 files (8.8 KB)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 6 Python source files


---

**Generated**: 2025-11-19T02:17:17.187827Z


---



## Chapter: openbb_platform/extensions/uscongress


**Path**: `openbb_platform/extensions/uscongress`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `uscongress`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (55.0 B)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.194901Z


---



## Chapter: openbb_platform/obbject_extensions/charting


**Path**: `openbb_platform/obbject_extensions/charting`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `charting`.


---

## Contents Summary

This folder contains **7 files** across **3 categories**:

- **Config**: 1 files (684.0 B)
- **Documentation**: 5 files (32.5 KB)
- **Text**: 1 files (270.5 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.200701Z


---



## Chapter: openbb_platform/providers/alpha_vantage


**Path**: `openbb_platform/providers/alpha_vantage`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `alpha_vantage`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (527.0 B)
- **Documentation**: 1 files (334.0 B)
- **Python**: 1 files (30.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.245737Z


---



## Chapter: openbb_platform/providers/benzinga


**Path**: `openbb_platform/providers/benzinga`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `benzinga`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (497.0 B)
- **Documentation**: 1 files (316.0 B)
- **Python**: 1 files (25.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.264219Z


---



## Chapter: openbb_platform/providers/biztoc


**Path**: `openbb_platform/providers/biztoc`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `biztoc`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (493.0 B)
- **Documentation**: 1 files (323.0 B)
- **Python**: 1 files (23.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.282998Z


---



## Chapter: openbb_platform/providers/bls


**Path**: `openbb_platform/providers/bls`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `bls`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (762.0 B)
- **Documentation**: 1 files (397.0 B)
- **Python**: 1 files (30.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.298315Z


---



## Chapter: openbb_platform/providers/cboe


**Path**: `openbb_platform/providers/cboe`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `cboe`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (528.0 B)
- **Documentation**: 1 files (300.0 B)
- **Python**: 1 files (21.0 B)
- **Text**: 1 files (209.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.328051Z


---



## Chapter: openbb_platform/providers/cftc


**Path**: `openbb_platform/providers/cftc`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `cftc`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (622.0 B)
- **Documentation**: 1 files (731.0 B)
- **Python**: 1 files (31.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.357129Z


---



## Chapter: openbb_platform/providers/congress_gov


**Path**: `openbb_platform/providers/congress_gov`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `congress_gov`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (633.0 B)
- **Documentation**: 1 files (2.8 KB)
- **Python**: 1 files (33.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.374655Z


---



## Chapter: openbb_platform/providers/deribit


**Path**: `openbb_platform/providers/deribit`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `deribit`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (532.0 B)
- **Documentation**: 1 files (924.0 B)
- **Python**: 1 files (38.0 B)
- **Text**: 1 files (207.4 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.395848Z


---



## Chapter: openbb_platform/providers/ecb


**Path**: `openbb_platform/providers/ecb`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `ecb`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (489.0 B)
- **Documentation**: 1 files (303.0 B)
- **Python**: 1 files (24.0 B)
- **Text**: 1 files (207.4 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.414637Z


---



## Chapter: openbb_platform/providers/econdb


**Path**: `openbb_platform/providers/econdb`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `econdb`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (540.0 B)
- **Documentation**: 1 files (304.0 B)
- **Python**: 1 files (24.0 B)
- **Text**: 1 files (209.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.434041Z


---



## Chapter: openbb_platform/providers/eia


**Path**: `openbb_platform/providers/eia`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `eia`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (748.0 B)
- **Documentation**: 1 files (3.8 KB)
- **Python**: 1 files (37.0 B)
- **Text**: 1 files (208.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.460755Z


---



## Chapter: openbb_platform/providers/famafrench


**Path**: `openbb_platform/providers/famafrench`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `famafrench`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (656.0 B)
- **Documentation**: 1 files (1.6 KB)
- **Python**: 1 files (26.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.479987Z


---



## Chapter: openbb_platform/providers/federal_reserve


**Path**: `openbb_platform/providers/federal_reserve`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `federal_reserve`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (569.0 B)
- **Documentation**: 1 files (351.0 B)
- **Python**: 1 files (52.0 B)
- **Text**: 1 files (208.0 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.502584Z


---



## Chapter: openbb_platform/providers/finra


**Path**: `openbb_platform/providers/finra`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `finra`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (479.0 B)
- **Documentation**: 1 files (300.0 B)
- **Python**: 1 files (42.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.529401Z


---



## Chapter: openbb_platform/providers/finviz


**Path**: `openbb_platform/providers/finviz`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `finviz`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (511.0 B)
- **Documentation**: 1 files (3.0 KB)
- **Python**: 1 files (23.0 B)
- **Text**: 1 files (229.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.545232Z


---



## Chapter: openbb_platform/providers/fmp


**Path**: `openbb_platform/providers/fmp`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `fmp`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (467.0 B)
- **Documentation**: 1 files (355.0 B)
- **Python**: 1 files (20.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.577430Z


---



## Chapter: openbb_platform/providers/fred


**Path**: `openbb_platform/providers/fred`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `fred`.


---

## Contents Summary

This folder contains **5 files** across **4 categories**:

- **Config**: 1 files (473.0 B)
- **Documentation**: 1 files (321.0 B)
- **Python**: 1 files (25.0 B)
- **Text**: 2 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.650888Z


---



## Chapter: openbb_platform/providers/government_us


**Path**: `openbb_platform/providers/government_us`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `government_us`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (556.0 B)
- **Documentation**: 1 files (322.0 B)
- **Python**: 1 files (30.0 B)
- **Text**: 1 files (207.4 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.699709Z


---



## Chapter: openbb_platform/providers/imf


**Path**: `openbb_platform/providers/imf`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `imf`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (518.0 B)
- **Documentation**: 1 files (1.2 KB)
- **Python**: 1 files (31.0 B)
- **Text**: 1 files (207.4 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.715749Z


---



## Chapter: openbb_platform/providers/intrinio


**Path**: `openbb_platform/providers/intrinio`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `intrinio`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (523.0 B)
- **Documentation**: 1 files (312.0 B)
- **Python**: 1 files (25.0 B)
- **Text**: 1 files (210.4 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.743344Z


---



## Chapter: openbb_platform/providers/multpl


**Path**: `openbb_platform/providers/multpl`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `multpl`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (473.0 B)
- **Documentation**: 1 files (218.0 B)
- **Python**: 1 files (33.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.787533Z


---



## Chapter: openbb_platform/providers/nasdaq


**Path**: `openbb_platform/providers/nasdaq`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `nasdaq`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (594.0 B)
- **Documentation**: 1 files (2.3 KB)
- **Python**: 1 files (23.0 B)
- **Text**: 1 files (212.2 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.802039Z


---



## Chapter: openbb_platform/providers/oecd


**Path**: `openbb_platform/providers/oecd`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `oecd`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (519.0 B)
- **Documentation**: 1 files (301.0 B)
- **Python**: 1 files (41.0 B)
- **Text**: 1 files (207.4 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.828365Z


---



## Chapter: openbb_platform/providers/polygon


**Path**: `openbb_platform/providers/polygon`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `polygon`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (491.0 B)
- **Documentation**: 1 files (307.0 B)
- **Python**: 1 files (29.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.848967Z


---



## Chapter: openbb_platform/providers/sec


**Path**: `openbb_platform/providers/sec`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `sec`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (628.0 B)
- **Documentation**: 1 files (301.0 B)
- **Python**: 1 files (20.0 B)
- **Text**: 1 files (256.7 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.874149Z


---



## Chapter: openbb_platform/providers/seeking_alpha


**Path**: `openbb_platform/providers/seeking_alpha`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `seeking_alpha`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (527.0 B)
- **Documentation**: 1 files (330.0 B)
- **Python**: 1 files (30.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.913483Z


---



## Chapter: openbb_platform/providers/stockgrid


**Path**: `openbb_platform/providers/stockgrid`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `stockgrid`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (531.0 B)
- **Documentation**: 1 files (315.0 B)
- **Python**: 1 files (26.0 B)
- **Text**: 1 files (217.1 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.931307Z


---



## Chapter: openbb_platform/providers/tests


**Path**: `openbb_platform/providers/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Documentation**: 1 files (827.0 B)
- **Python**: 3 files (9.6 KB)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.943849Z


---



## Chapter: openbb_platform/providers/tiingo


**Path**: `openbb_platform/providers/tiingo`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `tiingo`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (485.0 B)
- **Documentation**: 1 files (308.0 B)
- **Python**: 1 files (23.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.949155Z


---



## Chapter: openbb_platform/providers/tmx


**Path**: `openbb_platform/providers/tmx`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `tmx`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (670.0 B)
- **Documentation**: 1 files (2.6 KB)
- **Python**: 1 files (20.0 B)
- **Text**: 1 files (212.4 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.969056Z


---



## Chapter: openbb_platform/providers/tradier


**Path**: `openbb_platform/providers/tradier`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `tradier`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (508.0 B)
- **Documentation**: 1 files (562.0 B)
- **Python**: 1 files (24.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:18.011969Z


---



## Chapter: openbb_platform/providers/tradingeconomics


**Path**: `openbb_platform/providers/tradingeconomics`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `tradingeconomics`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (546.0 B)
- **Documentation**: 1 files (346.0 B)
- **Python**: 1 files (41.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:18.031033Z


---



## Chapter: openbb_platform/providers/wsj


**Path**: `openbb_platform/providers/wsj`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `wsj`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (467.0 B)
- **Documentation**: 1 files (304.0 B)
- **Python**: 1 files (20.0 B)
- **Text**: 1 files (206.9 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:18.046116Z


---



## Chapter: openbb_platform/providers/yfinance


**Path**: `openbb_platform/providers/yfinance`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `yfinance`.


---

## Contents Summary

This folder contains **4 files** across **4 categories**:

- **Config**: 1 files (542.0 B)
- **Documentation**: 1 files (327.0 B)
- **Python**: 1 files (25.0 B)
- **Text**: 1 files (263.4 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:18.060159Z


---



## Chapter: cli/openbb_cli/assets/routines


**Path**: `cli/openbb_cli/assets/routines`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `routines`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (439.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.544210Z


---



## Chapter: cli/openbb_cli/assets/styles


**Path**: `cli/openbb_cli/assets/styles`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `styles`.


---

## Contents Summary

This folder contains **0 files** across **0 categories**:


**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.546054Z


---



## Chapter: cookiecutter/openbb_cookiecutter/template/hooks


**Path**: `cookiecutter/openbb_cookiecutter/template/hooks`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `hooks`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (2.0 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.578002Z


---



## Chapter: cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}


**Path**: `cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `{{cookiecutter.project_tag}}`.


---

## Contents Summary

This folder contains **6 files** across **3 categories**:

- **Config**: 3 files (2.5 KB)
- **Documentation**: 1 files (1.1 KB)
- **Text**: 2 files (6.4 KB)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities


---

**Generated**: 2025-11-19T02:17:16.580010Z


---



## Chapter: desktop/public/assets/icons


**Path**: `desktop/public/assets/icons`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `icons`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Binary**: 1 files (19.8 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.612766Z


---



## Chapter: desktop/src-tauri/src/tauri_handlers


**Path**: `desktop/src-tauri/src/tauri_handlers`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `tauri_handlers`.


---

## Contents Summary

This folder contains **7 files** across **1 categories**:

- **Text**: 7 files (406.3 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Utilities**: Contains utility and helper functions


---

**Generated**: 2025-11-19T02:17:16.635622Z


---



## Chapter: desktop/src-tauri/src/utils


**Path**: `desktop/src-tauri/src/utils`

---

## Purpose & Role

This folder contains **utility functions and helper code** used throughout the project.


---

## Contents Summary

This folder contains **5 files** across **1 categories**:

- **Text**: 5 files (74.5 KB)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.640581Z


---



## Chapter: desktop/src/tests/components


**Path**: `desktop/src/tests/components`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `components`.


---

## Contents Summary

This folder contains **6 files** across **1 categories**:

- **Javascript**: 6 files (34.0 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities


---

**Generated**: 2025-11-19T02:17:16.661891Z


---



## Chapter: desktop/src/tests/routes


**Path**: `desktop/src/tests/routes`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `routes`.


---

## Contents Summary

This folder contains **11 files** across **1 categories**:

- **Javascript**: 11 files (93.6 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code


---

**Generated**: 2025-11-19T02:17:16.665442Z


---



## Chapter: frontend-components/plotly/src/components


**Path**: `frontend-components/plotly/src/components`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `components`.


---

## Contents Summary

This folder contains **6 files** across **1 categories**:

- **Javascript**: 6 files (68.2 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Configuration**: Contains configuration management


---

**Generated**: 2025-11-19T02:17:16.700920Z


---



## Chapter: frontend-components/plotly/src/data


**Path**: `frontend-components/plotly/src/data`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `data`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Javascript**: 1 files (294.8 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.711074Z


---



## Chapter: frontend-components/plotly/src/utils


**Path**: `frontend-components/plotly/src/utils`

---

## Purpose & Role

This folder contains **utility functions and helper code** used throughout the project.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Javascript**: 3 files (11.3 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Utilities**: Contains utility and helper functions


---

**Generated**: 2025-11-19T02:17:16.712766Z


---



## Chapter: frontend-components/tables/src/components


**Path**: `frontend-components/tables/src/components`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `components`.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Javascript**: 3 files (9.7 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.721744Z


---



## Chapter: frontend-components/tables/src/data


**Path**: `frontend-components/tables/src/data`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `data`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Javascript**: 1 files (269.8 KB)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.731252Z


---



## Chapter: frontend-components/tables/src/utils


**Path**: `frontend-components/tables/src/utils`

---

## Purpose & Role

This folder contains **utility functions and helper code** used throughout the project.


---

## Contents Summary

This folder contains **4 files** across **1 categories**:

- **Javascript**: 4 files (10.2 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Utilities**: Contains utility and helper functions


---

**Generated**: 2025-11-19T02:17:16.733417Z


---



## Chapter: openbb_platform/core/openbb/assets


**Path**: `openbb_platform/core/openbb/assets`

---

## Purpose & Role

This folder contains **static assets and resources** used by the project.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Config**: 1 files (389.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.750107Z


---



## Chapter: openbb_platform/core/openbb/package


**Path**: `openbb_platform/core/openbb/package`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `package`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (86.0 B)


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.751854Z


---



## Chapter: openbb_platform/core/openbb_core/api


**Path**: `openbb_platform/core/openbb_core/api`

---

## Purpose & Role

This folder contains **API-related code**, including endpoints, handlers, and API utilities.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Python**: 3 files (10.0 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **API**: Contains API-related code
- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:16.756092Z


---



## Chapter: openbb_platform/core/openbb_core/app


**Path**: `openbb_platform/core/openbb_core/app`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `app`.


---

## Contents Summary

This folder contains **10 files** across **1 categories**:

- **Python**: 10 files (84.1 KB)

**Subdirectories**: 4


---

## Key Concepts

Key concepts and components in this folder:

- **Utilities**: Contains utility and helper functions
- **Python Modules**: 10 Python source files


---

**Generated**: 2025-11-19T02:17:16.768697Z


---



## Chapter: openbb_platform/core/openbb_core/provider


**Path**: `openbb_platform/core/openbb_core/provider`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `provider`.


---

## Contents Summary

This folder contains **5 files** across **2 categories**:

- **Python**: 4 files (13.4 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 4 Python source files


---

**Generated**: 2025-11-19T02:17:16.809777Z


---



## Chapter: openbb_platform/core/tests/api


**Path**: `openbb_platform/core/tests/api`

---

## Purpose & Role

This folder contains **API-related code**, including endpoints, handlers, and API utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (155.0 B)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.880096Z


---



## Chapter: openbb_platform/core/tests/app


**Path**: `openbb_platform/core/tests/app`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `app`.


---

## Contents Summary

This folder contains **8 files** across **1 categories**:

- **Python**: 8 files (39.0 KB)

**Subdirectories**: 5


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Utilities**: Contains utility and helper functions
- **Python Modules**: 8 Python source files


---

**Generated**: 2025-11-19T02:17:16.888975Z


---



## Chapter: openbb_platform/core/tests/provider


**Path**: `openbb_platform/core/tests/provider`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `provider`.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Python**: 3 files (6.4 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:16.927421Z


---



## Chapter: openbb_platform/extensions/commodity/integration


**Path**: `openbb_platform/extensions/commodity/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (5.8 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.943068Z


---



## Chapter: openbb_platform/extensions/commodity/openbb_commodity


**Path**: `openbb_platform/extensions/commodity/openbb_commodity`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_commodity`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (2.3 KB)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.945165Z


---



## Chapter: openbb_platform/extensions/crypto/integration


**Path**: `openbb_platform/extensions/crypto/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (6.4 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.951669Z


---



## Chapter: openbb_platform/extensions/crypto/openbb_crypto


**Path**: `openbb_platform/extensions/crypto/openbb_crypto`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_crypto`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Python**: 3 files (1.6 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:16.953731Z


---



## Chapter: openbb_platform/extensions/crypto/tests


**Path**: `openbb_platform/extensions/crypto/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.958273Z


---



## Chapter: openbb_platform/extensions/currency/integration


**Path**: `openbb_platform/extensions/currency/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (9.7 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.962380Z


---



## Chapter: openbb_platform/extensions/currency/openbb_currency


**Path**: `openbb_platform/extensions/currency/openbb_currency`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_currency`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Python**: 3 files (4.1 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:16.964698Z


---



## Chapter: openbb_platform/extensions/currency/tests


**Path**: `openbb_platform/extensions/currency/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.969220Z


---



## Chapter: openbb_platform/extensions/derivatives/integration


**Path**: `openbb_platform/extensions/derivatives/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (14.6 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.973431Z


---



## Chapter: openbb_platform/extensions/derivatives/openbb_derivatives


**Path**: `openbb_platform/extensions/derivatives/openbb_derivatives`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_derivatives`.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Python**: 3 files (12.2 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:16.975545Z


---



## Chapter: openbb_platform/extensions/derivatives/tests


**Path**: `openbb_platform/extensions/derivatives/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.982984Z


---



## Chapter: openbb_platform/extensions/devtools/integration


**Path**: `openbb_platform/extensions/devtools/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:16.987808Z


---



## Chapter: openbb_platform/extensions/devtools/openbb_devtools


**Path**: `openbb_platform/extensions/devtools/openbb_devtools`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_devtools`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (39.0 B)


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.989469Z


---



## Chapter: openbb_platform/extensions/econometrics/integration


**Path**: `openbb_platform/extensions/econometrics/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (18.8 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:16.994162Z


---



## Chapter: openbb_platform/extensions/econometrics/openbb_econometrics


**Path**: `openbb_platform/extensions/econometrics/openbb_econometrics`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_econometrics`.


---

## Contents Summary

This folder contains **5 files** across **2 categories**:

- **Python**: 4 files (38.9 KB)
- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:

- **Utilities**: Contains utility and helper functions
- **Python Modules**: 4 Python source files


---

**Generated**: 2025-11-19T02:17:16.996515Z


---



## Chapter: openbb_platform/extensions/econometrics/tests


**Path**: `openbb_platform/extensions/econometrics/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (710.0 B)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Utilities**: Contains utility and helper functions
- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:16.999832Z


---



## Chapter: openbb_platform/extensions/economy/integration


**Path**: `openbb_platform/extensions/economy/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (69.1 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.004443Z


---



## Chapter: openbb_platform/extensions/economy/openbb_economy


**Path**: `openbb_platform/extensions/economy/openbb_economy`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_economy`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Python**: 3 files (48.5 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.006984Z


---



## Chapter: openbb_platform/extensions/economy/tests


**Path**: `openbb_platform/extensions/economy/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.016597Z


---



## Chapter: openbb_platform/extensions/equity/integration


**Path**: `openbb_platform/extensions/equity/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (126.4 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.021214Z


---



## Chapter: openbb_platform/extensions/equity/openbb_equity


**Path**: `openbb_platform/extensions/equity/openbb_equity`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_equity`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Python**: 3 files (6.5 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 9


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.023978Z


---



## Chapter: openbb_platform/extensions/equity/tests


**Path**: `openbb_platform/extensions/equity/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.047071Z


---



## Chapter: openbb_platform/extensions/etf/integration


**Path**: `openbb_platform/extensions/etf/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (24.9 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.051433Z


---



## Chapter: openbb_platform/extensions/etf/openbb_etf


**Path**: `openbb_platform/extensions/etf/openbb_etf`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_etf`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Python**: 3 files (9.3 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.054251Z


---



## Chapter: openbb_platform/extensions/etf/tests


**Path**: `openbb_platform/extensions/etf/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.058952Z


---



## Chapter: openbb_platform/extensions/famafrench/integration


**Path**: `openbb_platform/extensions/famafrench/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Python**: 3 files (12.2 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.062070Z


---



## Chapter: openbb_platform/extensions/fixedincome/integration


**Path**: `openbb_platform/extensions/fixedincome/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (36.9 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.067362Z


---



## Chapter: openbb_platform/extensions/fixedincome/openbb_fixedincome


**Path**: `openbb_platform/extensions/fixedincome/openbb_fixedincome`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_fixedincome`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Python**: 3 files (10.9 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 4


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.069714Z


---



## Chapter: openbb_platform/extensions/fixedincome/tests


**Path**: `openbb_platform/extensions/fixedincome/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.081439Z


---



## Chapter: openbb_platform/extensions/index/integration


**Path**: `openbb_platform/extensions/index/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (11.6 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.085582Z


---



## Chapter: openbb_platform/extensions/index/openbb_index


**Path**: `openbb_platform/extensions/index/openbb_index`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_index`.


---

## Contents Summary

This folder contains **4 files** across **2 categories**:

- **Python**: 3 files (3.9 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 1


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.087595Z


---



## Chapter: openbb_platform/extensions/index/tests


**Path**: `openbb_platform/extensions/index/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.092098Z


---



## Chapter: openbb_platform/extensions/mcp_server/integration


**Path**: `openbb_platform/extensions/mcp_server/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.096296Z


---



## Chapter: openbb_platform/extensions/mcp_server/openbb_mcp_server


**Path**: `openbb_platform/extensions/mcp_server/openbb_mcp_server`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_mcp_server`.


---

## Contents Summary

This folder contains **2 files** across **2 categories**:

- **Python**: 1 files (33.0 B)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 4


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.097865Z


---



## Chapter: openbb_platform/extensions/mcp_server/tests


**Path**: `openbb_platform/extensions/mcp_server/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **0 files** across **0 categories**:


**Subdirectories**: 4


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.110581Z


---



## Chapter: openbb_platform/extensions/news/integration


**Path**: `openbb_platform/extensions/news/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (11.4 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.124472Z


---



## Chapter: openbb_platform/extensions/news/openbb_news


**Path**: `openbb_platform/extensions/news/openbb_news`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_news`.


---

## Contents Summary

This folder contains **3 files** across **2 categories**:

- **Python**: 2 files (3.2 KB)
- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.126610Z


---



## Chapter: openbb_platform/extensions/news/tests


**Path**: `openbb_platform/extensions/news/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.128778Z


---



## Chapter: openbb_platform/extensions/platform_api/integration


**Path**: `openbb_platform/extensions/platform_api/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:



---

**Generated**: 2025-11-19T02:17:17.133372Z


---



## Chapter: openbb_platform/extensions/platform_api/openbb_platform_api


**Path**: `openbb_platform/extensions/platform_api/openbb_platform_api`

---

## Purpose & Role

This folder contains **API-related code**, including endpoints, handlers, and API utilities.


---

## Contents Summary

This folder contains **4 files** across **1 categories**:

- **Python**: 4 files (20.1 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Models**: Contains data models or model definitions
- **Python Modules**: 4 Python source files


---

**Generated**: 2025-11-19T02:17:17.135226Z


---



## Chapter: openbb_platform/extensions/platform_api/tests


**Path**: `openbb_platform/extensions/platform_api/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **5 files** across **2 categories**:

- **Config**: 2 files (329.4 KB)
- **Python**: 3 files (44.2 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Utilities**: Contains utility and helper functions
- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.144142Z


---



## Chapter: openbb_platform/extensions/quantitative/integration


**Path**: `openbb_platform/extensions/quantitative/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (30.6 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.150350Z


---



## Chapter: openbb_platform/extensions/quantitative/openbb_quantitative


**Path**: `openbb_platform/extensions/quantitative/openbb_quantitative`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_quantitative`.


---

## Contents Summary

This folder contains **6 files** across **2 categories**:

- **Python**: 5 files (15.3 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **Models**: Contains data models or model definitions
- **Utilities**: Contains utility and helper functions
- **Python Modules**: 5 Python source files


---

**Generated**: 2025-11-19T02:17:17.152646Z


---



## Chapter: openbb_platform/extensions/quantitative/tests


**Path**: `openbb_platform/extensions/quantitative/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (1.1 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Utilities**: Contains utility and helper functions
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.162430Z


---



## Chapter: openbb_platform/extensions/regulators/integration


**Path**: `openbb_platform/extensions/regulators/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (12.4 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.166825Z


---



## Chapter: openbb_platform/extensions/regulators/openbb_regulators


**Path**: `openbb_platform/extensions/regulators/openbb_regulators`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_regulators`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (453.0 B)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.168966Z


---



## Chapter: openbb_platform/extensions/technical/integration


**Path**: `openbb_platform/extensions/technical/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (50.0 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.178461Z


---



## Chapter: openbb_platform/extensions/technical/openbb_technical


**Path**: `openbb_platform/extensions/technical/openbb_technical`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_technical`.


---

## Contents Summary

This folder contains **6 files** across **2 categories**:

- **Python**: 5 files (119.5 KB)
- **Text**: 1 files (0.0 B)


---

## Key Concepts

Key concepts and components in this folder:

- **Utilities**: Contains utility and helper functions
- **Python Modules**: 5 Python source files


---

**Generated**: 2025-11-19T02:17:17.181267Z


---



## Chapter: openbb_platform/extensions/technical/tests


**Path**: `openbb_platform/extensions/technical/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (2.7 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Utilities**: Contains utility and helper functions
- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.185967Z


---



## Chapter: openbb_platform/extensions/tests/utils


**Path**: `openbb_platform/extensions/tests/utils`

---

## Purpose & Role

This folder contains **utility functions and helper code** used throughout the project.


---

## Contents Summary

This folder contains **6 files** across **1 categories**:

- **Python**: 6 files (48.4 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Utilities**: Contains utility and helper functions
- **Python Modules**: 6 Python source files


---

**Generated**: 2025-11-19T02:17:17.191090Z


---



## Chapter: openbb_platform/extensions/uscongress/integration


**Path**: `openbb_platform/extensions/uscongress/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (6.6 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.196777Z


---



## Chapter: openbb_platform/obbject_extensions/charting/integration


**Path**: `openbb_platform/obbject_extensions/charting/integration`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `integration`.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (47.6 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **API**: Contains API-related code
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.205148Z


---



## Chapter: openbb_platform/obbject_extensions/charting/openbb_charting


**Path**: `openbb_platform/obbject_extensions/charting/openbb_charting`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_charting`.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Python**: 3 files (56.2 KB)

**Subdirectories**: 3


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.207619Z


---



## Chapter: openbb_platform/obbject_extensions/charting/tests


**Path**: `openbb_platform/obbject_extensions/charting/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **3 files** across **1 categories**:

- **Python**: 3 files (5.2 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Utilities**: Contains utility and helper functions
- **Python Modules**: 3 Python source files


---

**Generated**: 2025-11-19T02:17:17.240398Z


---



## Chapter: openbb_platform/providers/alpha_vantage/openbb_alpha_vantage


**Path**: `openbb_platform/providers/alpha_vantage/openbb_alpha_vantage`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_alpha_vantage`.


---

## Contents Summary

This folder contains **2 files** across **2 categories**:

- **Python**: 1 files (1.5 KB)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.248807Z


---



## Chapter: openbb_platform/providers/alpha_vantage/tests


**Path**: `openbb_platform/providers/alpha_vantage/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (1.4 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.256075Z


---



## Chapter: openbb_platform/providers/benzinga/openbb_benzinga


**Path**: `openbb_platform/providers/benzinga/openbb_benzinga`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_benzinga`.


---

## Contents Summary

This folder contains **2 files** across **2 categories**:

- **Python**: 1 files (898.0 B)
- **Text**: 1 files (0.0 B)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.267216Z


---



## Chapter: openbb_platform/providers/benzinga/tests


**Path**: `openbb_platform/providers/benzinga/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (1.9 KB)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.275016Z


---



## Chapter: openbb_platform/providers/biztoc/openbb_biztoc


**Path**: `openbb_platform/providers/biztoc/openbb_biztoc`

---

## Purpose & Role

This folder is part of the project structure and contains code/resources for `openbb_biztoc`.


---

## Contents Summary

This folder contains **1 files** across **1 categories**:

- **Python**: 1 files (1.5 KB)

**Subdirectories**: 2


---

## Key Concepts

Key concepts and components in this folder:

- **Python Modules**: 1 Python source files


---

**Generated**: 2025-11-19T02:17:17.286256Z


---



## Chapter: openbb_platform/providers/biztoc/tests


**Path**: `openbb_platform/providers/biztoc/tests`

---

## Purpose & Role

This folder contains **test files** for the project. It includes unit tests, integration tests, and test utilities.


---

## Contents Summary

This folder contains **2 files** across **1 categories**:

- **Python**: 2 files (905.0 B)


---

## Key Concepts

Key concepts and components in this folder:

- **Testing**: Contains test files and testing utilities
- **Python Modules**: 2 Python source files


---

**Generated**: 2025-11-19T02:17:17.292192Z


---



---

## Conclusion

This comprehensive book covered 200 major sections of the repository.

For more detailed information:
- See individual file documentation (`*_docs.md` files)
- Browse the [keyword index](./keywords.md)
- Explore the [folder structure](./index.md)

**End of Book**

---

**Generated by**: World's Best Repo Book Generator v1.0.0
