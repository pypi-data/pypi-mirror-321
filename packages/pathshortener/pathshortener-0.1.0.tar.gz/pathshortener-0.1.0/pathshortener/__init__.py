"""
pathshortener - A library for shortening Windows environment variables and paths.

This library provides functionality to:
1. Shorten environment variables by replacing repeated substrings with references
2. Compress environment variables by finding common patterns
3. Handle Windows registry operations for environment variables
"""

from .env_vars import (
    compress_single_variable,
    compress_all_variables,
    shorten_string,
    update_environment_after_string_shortening
)

from .registry import (
    set_user_env_var,
    broadcast_settings_change
)

from .string_processing import (
    boundary_check,
    is_entire_env_reference,
    find_common_substrings,
    calculate_savings,
    apply_substitution
)

__version__ = "0.1.0"
__all__ = [
    'compress_single_variable',
    'compress_all_variables',
    'shorten_string',
    'update_environment_after_string_shortening',
    'set_user_env_var',
    'broadcast_settings_change',
    'boundary_check',
    'is_entire_env_reference',
    'find_common_substrings',
    'calculate_savings',
    'apply_substitution'
] 