# Documentation: openbb_platform/extensions/mcp_server/pyproject.toml

## File Metadata
- **Path**: `openbb_platform/extensions/mcp_server/pyproject.toml`
- **Size**: 620 characters, 24 lines
- **Words**: 60
- **Extension**: .toml
- **Classification**: Text file

## Original Source

```toml
[tool.poetry]
name = "openbb-mcp-server"
version = "1.2.0"
description = "OpenBB Platform MCP Server"
authors = ["OpenBB <hello@openbb.co>"]
license = "AGPL-3.0-only"
readme = "README.md"
homepage = "https://openbb.co"
repository = "https://github.com/openbb-finance/openbb"
documentation = "https://docs.openbb.co"
packages = [{ include = "openbb_mcp_server" }]

[tool.poetry.scripts]
openbb-mcp = "openbb_mcp_server.app.app:main"

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
openbb-core = "^1.5.1"
fastmcp = ">=2.12.3"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

```

## High-Level Overview

This is a .toml file containing 24 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:36.216033
- Generator: World's Best Repo Book Generator v1.0.0
