# pepperpy-poetry

A Poetry plugin for shared configuration management across multiple projects in the pepperpy ecosystem.

## Installation

```bash
poetry self add pepperpy-poetry
```

## Usage

1. Create a `shared-config.toml` file in your project root with your shared configurations:

```toml
[tool.ruff]
line-length = 88
target-version = "py312"
extend-exclude = [
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    ".git",
    "__pycache__"
]

[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
```

2. The plugin will automatically merge these configurations into your project's `pyproject.toml` when Poetry runs.

## Features

- Automatically merges shared configurations from `shared-config.toml` into your project's `pyproject.toml`
- Supports any TOML configuration sections
- Provides clear console feedback during the merge process
- Gracefully handles missing configuration files and errors

## Development

To work on the plugin locally:

```bash
git clone https://github.com/felipepimentel/pepperpy-poetry
cd pepperpy-poetry
poetry install
poetry self add .
```
