# PyGenTree

[![PyPI version](https://img.shields.io/pypi/v/pygentree.svg?style=for-the-badge)](https://pypi.org/project/pygentree/)
[![License](https://img.shields.io/pypi/l/pygentree.svg?style=for-the-badge)](https://github.com/taeefnajib/pygentree/blob/main/LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/pygentree.svg?style=for-the-badge)](https://pypi.org/project/pygentree/)

A Python package to generate ASCII tree representation of directory structures.

## Requirements

- Python 3.6 or higher

## Installation

```bash
pip install pygentree
```

## Usage

```bash
# Basic usage (current directory)
pygentree

# Specify a directory
pygentree /path/to/directory

# Limit depth level
pygentree -l 2

# Sort files and folders
pygentree -s asc   # ascending order
pygentree -s desc  # descending order
pygentree -s standard  # default: folders first, then files

# Show only directories
pygentree -d

# Ignore hidden files and directories, e.g. .git, .env, etc.
pygentree --ignore-hidden

# Exclude specific files or directories (comma-separated)
pygentree -e "node_modules,venv,dist"

# Save output to file
pygentree -o tree.txt

# Show version
pygentree -v

# Show help
pygentree -h
```

## Features

- Generate ASCII tree representation of directory structures
- Customize maximum depth level
- Multiple sorting options
- Option to show only directories
- Option to ignore hidden files and directories
- Exclude specific files and directories
- Save output to file
- Handle permission errors gracefully
- Cross-platform compatibility

## Supported Python Versions

- Python 3.6
- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

## License

MIT License
