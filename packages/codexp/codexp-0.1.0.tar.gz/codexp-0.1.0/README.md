# CodeXP (Code Explorer) 

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/codexp.svg)](https://badge.fury.io/py/codexp)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A CLI tool to analyze Python packages and visualize their structure and dependencies in the terminal.

## Features

- **Package Structure Analysis** 📦
  - Identifies entry points
  - Lists all modules in the package
  - Shows top-level symbols and their definitions

- **Dependency Analysis** 🔍
  - Maps internal imports between package modules
  - Tracks external package dependencies
  - Shows import locations with source code context

- **Symbol Usage Tracking** 🎯
  - Traces both internal and external symbol usage
  - Shows where symbols are defined and used
  - Provides source code context for each usage

- **Flexible Output** 📊
  - Rich terminal visualization with syntax highlighting
  - JSON output for programmatic analysis

## Installation

```bash
pip install codexp
```

## Usage

```bash
codexp <source_directory> [options]

Arguments:
  source_directory    Directory containing source code to analyze

Options:
  --no-line-info, -n    Hide file and line information
  --json, -j           Output results in JSON format
  --help               Show help message and exit
```

## Examples

```bash
# Analyze current directory with visual output
codexp .

# Analyze without line information
codexp ./my_package --no-line-info

# Get JSON output for programmatic use
codexp ./my_package --json > analysis.json
```

The default output provides a rich terminal visualization with syntax highlighting and tree-style formatting. For programmatic analysis, use the `--json` flag to get structured data output.

## License

MIT License - see the [LICENSE](LICENSE) file for details.
