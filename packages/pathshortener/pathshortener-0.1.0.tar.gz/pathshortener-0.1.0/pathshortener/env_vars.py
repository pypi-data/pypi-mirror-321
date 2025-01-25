import os
from collections import defaultdict

from .registry import set_user_env_var, broadcast_settings_change
from .string_processing import (
    boundary_check,
    is_entire_env_reference,
    find_common_substrings,
    calculate_savings,
    apply_substitution
)

def get_next_var_index(prefix="P_"):
    """
    Finds the next available index for environment variables with the given prefix.
    Ensures that existing P_X variables are not overwritten.
    """
    existing_vars = [var for var in os.environ if var.startswith(prefix)]
    indices = []
    for var in existing_vars:
        suffix = var[len(prefix):]
        if suffix.isdigit():
            indices.append(int(suffix))
    if indices:
        return max(indices) + 1
    else:
        return 0

def split_env_var(env_var_value, max_length=2048):
    """
    Splits the environment variable into chunks, each not exceeding max_length.
    Splitting is done at path separators to ensure valid entries.

    Returns a list of chunk strings.
    """
    path_sep = os.pathsep
    entries = env_var_value.split(path_sep)
    chunks = []
    current_chunk = ""

    for entry in entries:
        # Determine if adding this entry would exceed the max_length
        if current_chunk:
            tentative_length = len(current_chunk) + len(path_sep) + len(entry)
        else:
            tentative_length = len(entry)
        
        if tentative_length > max_length:
            if not current_chunk:
                # Single entry exceeds max_length, need to split the entry itself
                # This is a rare case; we split the entry into smaller parts
                for i in range(0, len(entry), max_length):
                    chunks.append(entry[i:i+max_length])
            else:
                # Finalize the current chunk and start a new one
                chunks.append(current_chunk)
                current_chunk = entry
        else:
            if current_chunk:
                current_chunk += path_sep + entry
            else:
                current_chunk = entry

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def create_chunk_vars(chunks, prefix="P_", dry_run=False):
    """
    Creates new environment variables for each chunk without overwriting existing P_X vars.
    
    Returns a dictionary mapping new variable names to their chunk values.
    """
    env_map = {}
    start_index = get_next_var_index(prefix=prefix)
    for i, chunk in enumerate(chunks):
        var_name = f"{prefix}{start_index + i}"
        env_map[var_name] = chunk
    return env_map

def apply_known_envvars_to_path(entries_with_owner, min_length=5):
    """
    entries_with_owner: a list of (owner_var_name, index_in_that_var, string_value).
    We try to replace any literal occurrence of each existing env var's value 
    with a reference (e.g., '%VAR%' on Windows), as long as it's not self-substitution 
    (owner_var_name != that env var).

    Additionally, we **skip** replacing any entry that is **exactly equal** to 
    any existing environment variable's value to prevent cyclical dependencies.

    Returns a new list of the same shape, with updated string_value.
    """
    def make_ref(vn):
        return f"%{vn}%"

    # Gather all existing environment variable values
    all_envvar_values = set(v for _, v in os.environ.items() if v)

    # Gather existing environment variables for substitution
    existing_vars = []
    for var_name, var_value in os.environ.items():
        if var_value and len(var_value) >= min_length:
            existing_vars.append((var_name, var_value))

    # Sort by length of var_value descending
    existing_vars.sort(key=lambda x: len(x[1]), reverse=True)

    new_entries = list(entries_with_owner)

    for envvar_name, envvar_value in existing_vars:
        ref_str = make_ref(envvar_name)
        for i in range(len(new_entries)):
            (owner_var, idx_in_owner, val_str) = new_entries[i]
            # Avoid self-substitution
            if owner_var == envvar_name:
                continue
            # Skip replacement if the entire entry matches any env var's value
            if val_str in all_envvar_values:
                continue

            # Find boundary matches in descending order
            positions = []
            start_idx = 0
            while True:
                found = val_str.find(envvar_value, start_idx)
                if found == -1:
                    break
                end_pos = found + len(envvar_value)
                if boundary_check(val_str, found, end_pos):
                    positions.append((found, end_pos))
                start_idx = found + 1

            positions.sort(key=lambda x: x[0], reverse=True)
            for (spos, epos) in positions:
                val_str = val_str[:spos] + ref_str + val_str[epos:]

            new_entries[i] = (owner_var, idx_in_owner, val_str)

    return new_entries

def iterative_substitution(paths, max_vars=10, min_length=5, env_var_prefix="P_", start_index=0):
    """
    Iteratively:
      - Scan current path-entries for repeated substrings
      - Pick the one with the greatest net savings (tie-break on substring length)
      - Replace it with %P_X% ...
      - Repeat until max_vars or no beneficial substring remains

    Returns (env_var_map, final_path_entries, next_var_index).
    """
    var_ref_len = 4  # e.g., %P_0%
    def make_ref(vn):
        return f"%{vn}%"

    env_map = {}
    current = list(paths)
    var_counter = start_index

    for _ in range(max_vars):
        subs_locs = find_common_substrings(current, min_length=min_length)
        best_sub = None
        best_locs = None
        best_savings = 0

        for sub, locs in subs_locs.items():
            s = calculate_savings(sub, locs, var_ref_len)
            if s > best_savings:
                best_sub = sub
                best_locs = locs
                best_savings = s
            elif abs(s - best_savings) < 1e-9 and best_sub and sub:
                # tie-break on substring length
                if len(sub) > len(best_sub):
                    best_sub = sub
                    best_locs = locs

        if not best_sub or best_savings <= 0:
            break

        var_name = f"{env_var_prefix}{var_counter}"
        var_counter += 1
        ref_str = make_ref(var_name)
        updated = apply_substitution(current, best_sub, best_locs, ref_str)
        env_map[var_name] = best_sub
        current = updated

    return env_map, current, var_counter

def update_environment_permanent(var_to_newval_dict, env_var_mapping, dry_run):
    """
    Permanently writes changes to HKEY_CURRENT_USER\Environment on Windows.
    If not on Windows, this function should not be called.
    """
    # Set new environment variables
    for new_var, val in env_var_mapping.items():
        if dry_run:
            print(f"[Dry Run] Would permanently set user env var {new_var} = {val}")
        else:
            set_user_env_var(new_var, val)

    # Update existing environment variables
    for var_name, new_val in var_to_newval_dict.items():
        if dry_run:
            print(f"[Dry Run] Would permanently update user env var {var_name} = {new_val}")
        else:
            set_user_env_var(var_name, new_val)
    
    if not dry_run:
        broadcast_settings_change()

def update_environment_temp(var_to_newval_dict, env_var_mapping, dry_run):
    """
    Just modifies os.environ in this process (ephemeral).
    """
    for new_var, val in env_var_mapping.items():
        if dry_run:
            print(f"[Dry Run] Would set environment variable {new_var} = {val}")
        else:
            os.environ[new_var] = val

    for var_name, new_val in var_to_newval_dict.items():
        if dry_run:
            print(f"[Dry Run] Would update {var_name} to: {new_val}")
        else:
            os.environ[var_name] = new_val

def compress_single_variable(env_var_name, dry_run, max_vars, min_length, permanent=False, max_length=2048):
    """
    Pre-run expansions + iterative new variables for a single specified variable.
    If the result exceeds max_length, it will be split into chunks.
    """
    orig_val = os.environ.get(env_var_name, "")
    split_entries = orig_val.split(os.pathsep) if orig_val else []
    old_len = len(orig_val)

    # Build a list of (owner, idx, val_str)
    entries_with_owner = [(env_var_name, i, v) for i, v in enumerate(split_entries)]

    # Pre-run
    pre_sub = apply_known_envvars_to_path(entries_with_owner, min_length=min_length)
    pre_sub_strings = [t[2] for t in pre_sub]

    # Determine the next available P_X index
    start_index = get_next_var_index()

    # Iterative
    env_map, final_list, _ = iterative_substitution(
        paths=pre_sub_strings,
        max_vars=max_vars,
        min_length=min_length,
        env_var_prefix="P_",
        start_index=start_index
    )
    new_val = os.pathsep.join(final_list)
    new_len = len(new_val)

    # Check if we need to split into chunks
    if new_len > max_length:
        # Split into chunks
        chunks = split_env_var(new_val, max_length=max_length)
        chunk_vars = create_chunk_vars(chunks, prefix="P_", dry_run=dry_run)
        
        # Create references to chunks
        chunk_refs = [f"%{var}%" for var in chunk_vars.keys()]
        final_val = os.pathsep.join(chunk_refs)
        
        # Combine both sets of variables
        combined_vars = {**env_map, **chunk_vars}
        
        # Update environment
        var_to_newval = {env_var_name: final_val}
        if permanent:
            update_environment_permanent(var_to_newval, combined_vars, dry_run)
        else:
            update_environment_temp(var_to_newval, combined_vars, dry_run)
            
        return old_len, len(final_val), combined_vars, final_val
    else:
        # No need to split, proceed with normal update
        var_to_newval = {env_var_name: new_val}
        if permanent:
            update_environment_permanent(var_to_newval, env_map, dry_run)
        else:
            update_environment_temp(var_to_newval, env_map, dry_run)

        return old_len, new_len, env_map, new_val

def compress_all_variables(dry_run, max_vars, min_length, permanent=False):
    """
    Combine ALL environment variables (except those starting with 'P_') 
    into a single synergy list, do the same pre-run + iterative logic, 
    then reassemble them. 
    """
    all_vars = sorted(os.environ.items(), key=lambda x: x[0])
    # Skip newly created from prior runs
    filtered_vars = [(k, v) for (k, v) in all_vars if not k.startswith("P_")]

    # Build a big list of (var_name, idx, string_val)
    master_entries = []
    for var_name, var_value in filtered_vars:
        splitted = var_value.split(os.pathsep) if var_value else []
        for idx, entry in enumerate(splitted):
            master_entries.append((var_name, idx, entry))

    old_total = sum(len(v) for (k, v) in filtered_vars)

    # Pre-run
    pre_sub = apply_known_envvars_to_path(master_entries, min_length=min_length)
    pre_sub_strings = [x[2] for x in pre_sub]

    # Determine the next available P_X index
    start_index = get_next_var_index()

    # Iterative synergy
    env_map, final_strings, _ = iterative_substitution(
        paths=pre_sub_strings,
        max_vars=max_vars,
        min_length=min_length,
        env_var_prefix="P_",
        start_index=start_index
    )

    # Rebuild each var
    # final_strings[i] corresponds to master_entries[i]
    var_segments = defaultdict(list)
    for ((var_name, idx_in_var, _), final_str) in zip(master_entries, final_strings):
        var_segments[var_name].append((idx_in_var, final_str))

    var_to_newval = {}
    for var_name, segs in var_segments.items():
        segs.sort(key=lambda x: x[0])
        joined = os.pathsep.join(s[1] for s in segs)
        var_to_newval[var_name] = joined

    new_total = sum(len(v) for v in var_to_newval.values())

    # Update environment
    if permanent:
        update_environment_permanent(var_to_newval, env_map, dry_run)
    else:
        update_environment_temp(var_to_newval, env_map, dry_run)

    return old_total, new_total, env_map, var_to_newval

def shorten_string(input_string, max_vars=10, min_length=5, dry_run=False):
    """
    Shortens an arbitrary input string by replacing repeated substrings with new variables.
    Existing environment variables are considered for replacements.

    Returns the shortened string and the mapping of new variables.
    """
    # Split the input string by path separator if it's a path-like string
    # Otherwise, treat the entire string as a single entry
    if os.pathsep in input_string:
        split_entries = input_string.split(os.pathsep)
    else:
        split_entries = [input_string]
    
    # Build a list of (owner, idx, val_str)
    entries_with_owner = [("INPUT", i, v) for i, v in enumerate(split_entries)]

    # Pre-run
    pre_sub = apply_known_envvars_to_path(entries_with_owner, min_length=min_length)
    pre_sub_strings = [t[2] for t in pre_sub]

    # Determine the next available P_X index
    start_index = get_next_var_index()

    # Iterative substitution
    env_map, final_list, _ = iterative_substitution(
        paths=pre_sub_strings,
        max_vars=max_vars,
        min_length=min_length,
        env_var_prefix="P_",
        start_index=start_index
    )

    # Reassemble the string
    shortened_entries = final_list
    shortened_string = os.pathsep.join(shortened_entries)

    # Output the mapping
    if dry_run:
        print("\n[Dry Run] Environment Variable Mapping (newly created):")
        for var, val in env_map.items():
            print(f"[Dry Run] {var} = {val}")
        print(f"\n[Dry Run] Shortened String: {shortened_string}")
    else:
        print("\nEnvironment Variable Mapping (newly created):")
        for var, val in env_map.items():
            print(f"{var} = {val}")

    return shortened_string, env_map

def update_environment_after_string_shortening(env_map, dry_run):
    """
    Applies the new environment variables created during string shortening.
    Does not modify existing environment variables.
    """
    # Set new environment variables
    for new_var, val in env_map.items():
        if dry_run:
            print(f"[Dry Run] Would set environment variable {new_var} = {val}")
        else:
            set_user_env_var(new_var, val)
    
    if not dry_run:
        broadcast_settings_change() 