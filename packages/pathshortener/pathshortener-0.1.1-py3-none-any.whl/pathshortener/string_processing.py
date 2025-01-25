import os
import sys
from collections import defaultdict

def boundary_check(path, match_start, match_end):
    """
    Checks that 'match_start..match_end' is at a path boundary:
      - preceding char is [os.sep or ':']
      - following char is [os.sep or ';' or end-of-string]
    On Windows, typically os.sep='\\' and pathsep=';'.
    """
    if match_start < 0 or match_end > len(path):
        return False

    prev_char = path[match_start - 1] if match_start > 0 else os.sep
    next_char = os.sep
    if match_end < len(path):
        next_char = path[match_end]

    if prev_char in [os.sep, ':'] and next_char in [os.sep, ';']:
        return True
    return False

def is_entire_env_reference(s):
    """
    True if 's' is exactly an environment-variable reference with no extra text.
    E.g., '%FOO%' on Windows.
    """
    if sys.platform.startswith('win'):
        # e.g., '%PROGRAMFILES%'
        return (len(s) >= 3 
                and s.startswith('%') 
                and s.endswith('%') 
                and s.count('%') == 2)
    else:
        # Not applicable as script is Windows-only now
        return False

def find_common_substrings(paths, min_length=5):
    """
    Finds all candidate substrings (length >= min_length) that appear
    in multiple path entries, with boundary checks. Excludes any substring
    that is just an environment variable reference by itself (e.g., '%FOO%').

    Returns: { substring -> list of (path_idx, start, end) }
    """
    substring_locations = defaultdict(list)
    for pidx, pstr in enumerate(paths):
        components = pstr.split(os.sep)
        for i in range(len(components)):
            for j in range(i+1, len(components)+1):
                subpath = os.sep.join(components[i:j])
                if len(subpath) < min_length:
                    continue
                # skip if purely an env ref
                if is_entire_env_reference(subpath):
                    continue

                pos = 0
                while True:
                    idx = pstr.find(subpath, pos)
                    if idx == -1:
                        break
                    epos = idx + len(subpath)
                    if boundary_check(pstr, idx, epos):
                        substring_locations[subpath].append((pidx, idx, epos))
                    pos = idx + 1
    return substring_locations

def calculate_savings(substring, occurrences, var_ref_length):
    """
    net_savings = (#unique_paths) * (len(substring) - var_ref_length)
    Must appear in >=2 distinct path entries to be beneficial.
    """
    unique_idx = set(x[0] for x in occurrences)
    if len(unique_idx) < 2:
        return 0
    diff = len(substring) - var_ref_length
    if diff <= 0:
        return 0
    total_savings = diff * len(unique_idx)
    # Optional penalty for short substrings
    if len(substring) < 10:
        total_savings *= 0.8
    return total_savings

def apply_substitution(paths, substring, locations, var_ref):
    """
    Replaces all occurrences of 'substring' at the specified locations
    with 'var_ref'. Sort in descending order to avoid messing up indexes.
    """
    new_paths = list(paths)
    sorted_locs = sorted(locations, key=lambda x: (x[0], x[1]), reverse=True)
    for (path_idx, st, ed) in sorted_locs:
        seg = new_paths[path_idx]
        new_paths[path_idx] = seg[:st] + var_ref + seg[ed:]
    return new_paths 