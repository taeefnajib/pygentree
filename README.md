# PyGenTree

A Python package to generate ASCII tree representation of directory structures.

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
- Save output to file
- Handle permission errors gracefully
- Cross-platform compatibility

## License

MIT License