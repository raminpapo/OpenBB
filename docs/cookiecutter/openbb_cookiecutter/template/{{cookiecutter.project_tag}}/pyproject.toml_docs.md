# Documentation: cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/pyproject.toml

## File Metadata
- **Path**: `cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/pyproject.toml`
- **Size**: 1,547 characters, 35 lines
- **Words**: 123
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "{{ cookiecutter.project_tag }}"
version = "0.0.1"
description = "{{ cookiecutter.project_name }}"
authors = ["{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>"]
readme = "README.md"
license = "AGPL-3.0-only"
packages = [{ include = "{{ cookiecutter.package_name }}" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "*"
openbb-platform-api = "*"

[tool.poetry.group.dev.dependencies]
openbb-devtools = { version = "*" }

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."openbb_core_extension"]
{{ cookiecutter.router_name }} = "{{ cookiecutter.package_name }}.routers.{{ cookiecutter.router_name }}:router"

[tool.poetry.plugins."openbb_charting_extension"]
{{ cookiecutter.router_name }} = "{{ cookiecutter.package_name }}.routers.{{ cookiecutter.router_name }}_views:{{cookiecutter.router_name.replace('_', ' ').title().replace(' ', '').replace('"', '')}}Views"

[tool.poetry.plugins."openbb_provider_extension"]
{{ cookiecutter.provider_name }} = "{{ cookiecutter.package_name }}.providers.{{ cookiecutter.provider_name }}:{{ cookiecutter.provider_name }}_provider"

[tool.poetry.plugins."openbb_obbject_extension"]
to_string = "{{ cookiecutter.package_name }}.obbject.{{ cookiecutter.obbject_name }}:ext"
{{ cookiecutter.obbject_name }} = "{{ cookiecutter.package_name }}.obbject.{{ cookiecutter.obbject_name }}:class_ext"
nonblocking_plugin = "{{ cookiecutter.package_name }}.obbject.{{ cookiecutter.obbject_name }}:nonblocking_plugin"

```

## High-Level Overview

This is a .toml file containing 35 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.746051
- Generator: World's Best Repo Book Generator v1.0.0
