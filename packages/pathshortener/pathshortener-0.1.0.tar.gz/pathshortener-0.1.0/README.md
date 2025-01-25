# PathShortener

A Python library for shortening Windows environment variables and paths by finding and replacing repeated patterns with environment variable references.

## Features

- Shorten environment variables by replacing repeated substrings with references
- Compress environment variables by finding common patterns
- Automatically split long environment variables into chunks
- Handle Windows registry operations for environment variables
- Support for both temporary and permanent environment variable changes
- Command-line interface for quick access to functionality

## Installation

```bash
pip install pathshortener
```

## Usage

### As a Library

```python
from pathshortener import shorten_string, compress_single_variable, compress_all_variables

# Shorten a single string
shortened_string, env_map = shorten_string(
    input_string="C:\\Program Files\\Common Files\\System\\Some\\Long\\Path",
    max_vars=10,
    min_length=5,
    dry_run=True
)

# Compress a single environment variable
old_len, new_len, env_map, final_val = compress_single_variable(
    env_var_name="PATH",
    dry_run=True,
    max_vars=10,
    min_length=5,
    permanent=False,
    max_length=2048  # Values exceeding this will be split into chunks
)

# Compress all environment variables
old_total, new_total, env_map, var_to_newval = compress_all_variables(
    dry_run=True,
    max_vars=10,
    min_length=5,
    permanent=False
)
```

### Command Line Interface

```bash
# Shorten a string
pathshortener --string "C:\\Program Files\\Common Files\\System\\Some\\Long\\Path" --dry-run

# Compress a single environment variable
pathshortener --env-var PATH --dry-run --max-length 2048

# Compress all environment variables
pathshortener --env-var ALL --dry-run

# Make permanent changes (writes to Windows registry)
pathshortener --env-var PATH --permanent
```

## Options

- `--dry-run`: Show what would happen without making changes
- `--max-vars`: Maximum number of new environment variables to create (default: 10)
- `--min-length`: Minimum length of substrings to consider for substitution (default: 5)
- `--max-length`: Maximum length for environment variable values (default: 2048). Values exceeding this will be split into chunks.
- `--env-var`: Environment variable to process (default: PATH), or 'ALL' for global synergy
- `--string`: An arbitrary string to shorten
- `--permanent`: Write changes to Windows registry (HKEY_CURRENT_USER\Environment)

## How It Works

1. First, the tool tries to shorten environment variables by:
   - Finding and replacing repeated substrings with environment variable references
   - Using existing environment variables where possible
   - Creating new environment variables for common patterns

2. If the resulting value exceeds the maximum length (default: 2048 characters):
   - The value is split into chunks at path separators
   - Each chunk is stored in a new environment variable
   - The original variable is updated to reference these chunks

This two-step process ensures that environment variables are both shortened and kept within Windows' length limits.

## Requirements

- Windows operating system
- Python 3.6 or higher

## License

MIT License 