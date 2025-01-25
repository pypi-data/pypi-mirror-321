"""Command-line interface for pathshortener."""
import os
import sys
import argparse

from . import (
    compress_single_variable,
    compress_all_variables,
    shorten_string,
    update_environment_after_string_shortening
)

def create_parser():
    """Create the command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Shorten environment variables or an arbitrary string by replacing repeated substrings with new variables."
    )
    parser.add_argument('--dry-run', action='store_true',
                        help="Show what would happen without actually applying changes.")
    parser.add_argument('--max-vars', type=int, default=10,
                        help="Maximum number of new environment variables to define.")
    parser.add_argument('--min-length', type=int, default=5,
                        help="Minimum length of substrings to consider for substitution.")
    parser.add_argument('--max-length', type=int, default=2048,
                        help="Maximum length for environment variable values. Values exceeding this will be split into chunks.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--env-var', default='PATH',
                       help="Single environment var to process (default: PATH), or 'ALL' for global synergy.")
    group.add_argument('--string', type=str,
                       help="An arbitrary string to shorten.")
    parser.add_argument('--permanent', action='store_true',
                        help="On Windows, write changes to user registry (HKEY_CURRENT_USER\\Environment). Applicable only when modifying environment variables.")
    return parser

def handle_string_shortening(args):
    """Handle the string shortening mode."""
    print(f"Shortening the provided string: {args.string}")
    shortened_string, env_map = shorten_string(
        input_string=args.string,
        max_vars=args.max_vars,
        min_length=args.min_length,
        dry_run=args.dry_run
    )
    
    if not args.dry_run and env_map:
        update_environment_after_string_shortening(env_map, dry_run=args.dry_run)
    
    if not args.dry_run:
        print(f"\nShortened String: {shortened_string}")
    else:
        print(f"\n[Dry Run] Shortened String: {shortened_string}")

def handle_all_variables(args):
    """Handle the global synergy mode (all variables)."""
    old_total, new_total, env_map, var_to_newval = compress_all_variables(
        dry_run=args.dry_run,
        max_vars=args.max_vars,
        min_length=args.min_length,
        permanent=args.permanent
    )

    print(f"\nTotal length across all variables reduced from {old_total} to {new_total}.")
    if old_total > 0:
        saved = old_total - new_total
        pct = 100.0 * saved / old_total
        print(f"Total reduction: {saved} characters ({pct:.1f}%)")
    else:
        print("No reduction (all empty?).")

    print("\nEnvironment Variable Mapping (newly created):")
    for var, val in env_map.items():
        if args.dry_run:
            print(f"[Dry Run] {var} = {val}")
        else:
            print(f"{var} = {val}")

    # Optionally show the final state
    if args.dry_run:
        for vn, vv in var_to_newval.items():
            print(f"[Dry Run] {vn} -> {vv}")
    else:
        for vn in var_to_newval:
            print(f"\n{vn} is now: {os.environ[vn]}")

def handle_single_variable(args):
    """Handle single variable compression mode."""
    env_var_name = args.env_var
    old_len, new_len, env_map, final_val = compress_single_variable(
        env_var_name=env_var_name,
        dry_run=args.dry_run,
        max_vars=args.max_vars,
        min_length=args.min_length,
        permanent=args.permanent,
        max_length=args.max_length
    )
    saved = old_len - new_len
    print(f"\n{env_var_name} length reduced from {old_len} to {new_len}.")
    if old_len > 0:
        pct = 100.0 * saved / old_len
        print(f"Total reduction: {saved} characters ({pct:.1f}%)")
    else:
        print("No reduction (empty?).")

    print("\nEnvironment Variable Mapping (newly created):")
    for var, val in env_map.items():
        if args.dry_run:
            print(f"[Dry Run] {var} = {val}")
        else:
            print(f"{var} = {val}")

    if args.dry_run:
        print(f"\n[Dry Run] New {env_var_name} would be: {final_val}")
    else:
        print(f"\nNew {env_var_name}:", os.environ[env_var_name])

def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()

    if not sys.platform.startswith("win"):
        print("Error: This script is designed to run on Windows only.")
        sys.exit(1)

    if args.string:
        handle_string_shortening(args)
    else:
        if args.env_var.upper() == 'ALL':
            handle_all_variables(args)
        else:
            handle_single_variable(args)

if __name__ == "__main__":
    main() 