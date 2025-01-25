"""
This module contains the functions necessary to read, write, and build AdataDict objects from adata in memory or on disk.
"""

import os
import json
import itertools
from collections import Counter

import pandas as pd
import anndata as ad
import scanpy as sc


from .adata_dict import AdataDict, to_nested_tuple
from .adata_dict_fapply import adata_dict_fapply


def write_adata_dict(adata_dict, directory, file_prefix=""):
    """
    Saves each AnnData object from an AdataDict into separate .h5ad files,
    creating a directory structure that reflects the hierarchy of the AdataDict,
    using key values as directory names. The hierarchy is saved in a file
    'adata_dict.hierarchy' in the top-level directory.

    Parameters:
    - adata_dict: An instance of AdataDict.
    - directory: String, base directory where .h5ad files will be saved.
    - file_prefix: String, optional prefix for the filenames.

    The directory structure uses key values as directory names, and the full key tuple
    as the filename of the h5ad file.

    Example:
    If the hierarchy is ('species', 'tissue', 'cell_type') and keys are ('human', 'brain', 'neuron'),
    the files will be saved in 'directory/human/brain/neuron/' with filenames like 'human_brain_neuron.h5ad'.

    Additionally, a file named 'adata_dict.hierarchy' is saved in the top-level directory,
    containing the hierarchy information.
    """

    # Create the base directory, throwing error if it exists already (to avoid overwriting)
    os.makedirs(directory, exist_ok=False)

    # Save the hierarchy to a file in the top-level directory
    hierarchy_file_path = os.path.join(directory, "adata_dict.hierarchy")
    with open(hierarchy_file_path, "w") as f:
        # Save the hierarchy using JSON for easy reconstruction
        json.dump(adata_dict._hierarchy, f)

    # Flatten the AdataDict to get all AnnData objects with their keys
    flat_dict = adata_dict.flatten()

    # Iterate over the flattened dictionary and save each AnnData object
    for key, adata in flat_dict.items():
        # Build the path according to the key values (without hierarchy names)
        path_parts = [directory] + [str(k) for k in key]
        # Create the directory path
        dir_path = os.path.join(*path_parts)
        os.makedirs(dir_path, exist_ok=True)
        # Construct the filename using the full key tuple
        filename = f"{file_prefix}{'_'.join(map(str, key))}.h5ad"
        file_path = os.path.join(dir_path, filename)
        # Save the AnnData object
        sc.write(file_path, adata)


def read(directory_list, keys=None):
    """
    Takes a list of strings, which can be directories or file paths.
    For each directory, if a .hierarchy file is found in the directory, it processes that directory with read_adata_dict.
    Otherwise, processes the highest-level directory with read_adata_dict_from_h5ad.
    The directories that contain .hierarchy files and the subdirectories of a directory that contains .hierarchy files are not processed with read_adata_dict_from_h5ad.

    Parameters:
    - directory_list: List of strings, paths to directories or .h5ad files.
    - keys: a list of strings that will be the keys for the dictionary

    Returns:
    - A combined dictionary of AnnData objects.
    """
    adata_dict = {}

    # Set to keep track of directories that have been processed with read_adata_dict
    hierarchy_dirs = set()

    # List to collect .h5ad files to process
    h5ad_files = []

    # Function to find all directories containing adata_dict.hierarchy files
    def find_hierarchy_dirs(dir_path):
        for root, dirs, files in os.walk(dir_path):
            if "adata_dict.hierarchy" in files:
                hierarchy_dirs.add(root)
                # Do not traverse subdirectories of directories with hierarchy files
                dirs[:] = []
            else:
                # Continue traversing subdirectories
                pass

    # First, process the input paths to find hierarchy directories and collect .h5ad files
    for path in directory_list:
        if os.path.isfile(path):
            if path.endswith(".h5ad"):
                h5ad_files.append(path)
        elif os.path.isdir(path):
            # Find hierarchy directories
            find_hierarchy_dirs(path)
        else:
            raise ValueError(f"Path {path} is neither a file nor a directory.")

    # Process directories with hierarchy files using read_adata_dict
    for h_dir in hierarchy_dirs:
        adata_dict.update(read_adata_dict(h_dir))

    # Build a set of directories to exclude (hierarchy_dirs and their subdirectories)
    exclude_dirs = set()
    for h_dir in hierarchy_dirs:
        for root, dirs, files in os.walk(h_dir):
            exclude_dirs.add(root)

    # Function to collect .h5ad files not under exclude_dirs
    def collect_h5ad_files(dir_path):
        for root, dirs, files in os.walk(dir_path):
            # Skip directories under exclude_dirs
            if any(
                os.path.commonpath([root, excl_dir]) == excl_dir
                for excl_dir in exclude_dirs
            ):
                dirs[:] = []
                continue
            for file in files:
                if file.endswith(".h5ad"):
                    h5ad_files.append(os.path.join(root, file))

    # Collect .h5ad files from directories not containing hierarchy files
    for path in directory_list:
        if os.path.isdir(path):
            collect_h5ad_files(path)

    # Process the collected .h5ad files using read_adata_dict_from_h5ad
    if h5ad_files:
        adata_dict.update(read_adata_dict_from_h5ad(h5ad_files, keys=keys))

    return adata_dict


def read_adata_dict(directory):
    """
    Reads the AdataDict from the specified directory, reconstructing
    the hierarchy and loading all AnnData objects. Returns an instance
    of AdataDict with the hierarchy attribute set.

    Parameters:
    - directory: String, base directory where the .h5ad files and hierarchy file are located.

    Returns:
    - An instance of AdataDict reconstructed from the saved files.
    """

    # Read the hierarchy from the file
    hierarchy_file_path = os.path.join(directory, "adata_dict.hierarchy")
    with open(hierarchy_file_path, "r") as f:
        # tuples will be converted to lists on write, so need to convert back to tuple on load
        hierarchy = to_nested_tuple(json.load(f))

    # Initialize an empty AdataDict with the hierarchy
    adata_dict = AdataDict(hierarchy=hierarchy)

    # Function to recursively rebuild the nested AdataDict
    def add_to_adata_dict(current_dict, key_tuple, adata):
        """
        Recursively adds the AnnData object to the appropriate place in the nested AdataDict.

        Parameters:
        - current_dict: The current level of AdataDict.
        - key_tuple: Tuple of key elements indicating the path.
        - adata: The AnnData object to add.
        """
        if len(key_tuple) == 1:
            current_dict[key_tuple[0]] = adata
        else:
            key = key_tuple[0]
            if key not in current_dict:
                current_dict[key] = AdataDict(hierarchy=hierarchy[1:])
            add_to_adata_dict(current_dict[key], key_tuple[1:], adata)

    # Walk through the directory structure
    for root, dirs, files in os.walk(directory):
        # Skip the top-level directory where the hierarchy file is located
        relative_path = os.path.relpath(root, directory)
        if relative_path == ".":
            continue
        for file in files:
            if file.endswith(".h5ad"):
                # Reconstruct the key from the directory path
                path_parts = relative_path.split(os.sep)
                key_elements = path_parts
                # Remove empty strings (if any)
                key_elements = [k for k in key_elements if k]
                key = tuple(key_elements)
                # Read the AnnData object
                file_path = os.path.join(root, file)
                adata = sc.read(file_path)
                # Add to the AdataDict
                add_to_adata_dict(adata_dict, key, adata)
    return adata_dict


def read_adata_dict_from_h5ad(paths, keys=None):
    """
    Reads .h5ad files from a list of paths and returns them in a dictionary.
    For each element in the provided list of paths, if the element is a directory,
    it reads all .h5ad files in that directory. If the element is an .h5ad file,
    it reads the file directly.

    For auto-generated keys, if there are duplicate filenames, the function will
    include parent directory names from right to left until keys are unique.
    For example, 'dat/heart/fibroblast.h5ad' would generate the key ('heart', 'fibroblast')
    if disambiguation is needed.

    Parameters:
    paths (list): A list of paths to directories or .h5ad files.
    keys (list, optional): A list of strings to use as keys for the adata_dict.
                          If provided, must be equal in length to the number of .h5ad files read.

    Returns:
    dict: A dictionary with tuple keys and AnnData objects as values.
    """

    adata_dict = {}
    file_paths = []

    # First, collect all file paths
    for path in paths:
        if os.path.isdir(path):
            for file in os.listdir(path):
                if file.endswith(".h5ad"):
                    file_paths.append(os.path.join(path, file))
        elif path.endswith(".h5ad"):
            file_paths.append(path)

    # Check if provided keys match the number of files
    if keys is not None:
        if len(keys) != len(file_paths):
            raise ValueError(
                f"Number of provided keys ({len(keys)}) does not match the number of .h5ad files ({len(file_paths)})"
            )
        # Check for uniqueness in provided keys
        key_counts = Counter(keys)
        duplicates = [k for k, v in key_counts.items() if v > 1]
        if duplicates:
            raise ValueError(f"Duplicate keys found: {duplicates}")
        # Convert provided keys to tuples
        tuple_keys = [tuple(k) if isinstance(k, (list, tuple)) else (k,) for k in keys]
    else:
        # Generate keys from paths
        base_names = [os.path.splitext(os.path.basename(fp))[0] for fp in file_paths]

        # Start with just the base names
        tuple_keys = [(name,) for name in base_names]

        # Keep extending paths to the left until all keys are unique
        while len(set(tuple_keys)) != len(tuple_keys):
            new_tuple_keys = []
            for i, file_path in enumerate(file_paths):
                path_parts = os.path.normpath(file_path).split(os.sep)
                # Find the current key's elements in the path
                current_key = tuple_keys[i]
                current_idx = (
                    len(path_parts) - 1 - len(current_key)
                )  # -1 for zero-based index
                # Add one more path element to the left if possible
                if current_idx > 0:
                    new_key = (path_parts[current_idx - 1],) + current_key
                else:
                    new_key = current_key
                new_tuple_keys.append(new_key)
            tuple_keys = new_tuple_keys

            # Safety check - if we've used all path components and still have duplicates
            if all(
                len(key) == len(os.path.normpath(fp).split(os.sep))
                for key, fp in zip(tuple_keys, file_paths)
            ):
                raise ValueError("Unable to create unique keys even using full paths")

    # Process the files with the finalized tuple keys
    for i, file_path in enumerate(file_paths):
        adata_dict[tuple_keys[i]] = ad.read_h5ad(file_path)

    return adata_dict


def build_adata_dict(adata, strata_keys, desired_strata=None):
    """
    Build a dictionary of AnnData objects split by desired strata values.

    Parameters:
    adata (AnnData): Annotated data matrix.
    strata_keys (list of str): List of column names in `adata.obs` to use for stratification.
    desired_strata (list or dict, optional): List of desired strata tuples or a dictionary where keys are strata keys and values are lists of desired strata values. If None (Default), all combinations of categories in adata.obs[strata_keys] will be used.

    Returns:
    dict: Dictionary where keys are strata tuples and values are corresponding AnnData subsets.

    Raises:
    ValueError: If `desired_strata` is neither a list nor a dictionary of lists.
    """
    if desired_strata is None:
        # Generate all combinations of categories in adata.obs[strata_keys]
        all_categories = [adata.obs[key].cat.categories.tolist() for key in strata_keys]
        all_combinations = list(itertools.product(*all_categories))
        desired_strata = all_combinations
        return build_adata_dict_main(
            adata, strata_keys, desired_strata, print_missing_strata=False
        )

    elif isinstance(desired_strata, list):
        # Ensure that desired_strata is a list of tuples
        if all(isinstance(item, str) for item in desired_strata):
            raise ValueError("desired_strata should be a list of tuples, not strings.")
        return build_adata_dict_main(adata, strata_keys, desired_strata)

    elif isinstance(desired_strata, dict):
        # Generate all combinations of desired strata values across strata_keys
        all_combinations = itertools.product(
            *(desired_strata[key] for key in strata_keys)
        )
        desired_strata = list(all_combinations)
        return build_adata_dict_main(adata, strata_keys, desired_strata)

    else:
        raise ValueError(
            "desired_strata must be either a list of tuples or a dictionary of lists"
        )


def build_adata_dict_main(
    adata, strata_keys, desired_strata, print_missing_strata=True
):
    """
    Optimized function to build a dictionary of AnnData objects based on desired strata values.

    Parameters:
    adata (AnnData): Annotated data matrix.
    strata_keys (list of str): List of column names in `adata.obs` to use for stratification.
    desired_strata (list of tuples): List of desired strata tuples.

    Returns:
    dict: Dictionary where keys are strata tuples and values are corresponding AnnData subsets.
    """
    # Ensure that the strata columns are categorical
    for key in strata_keys:
        if not pd.api.types.is_categorical_dtype(adata.obs[key]):
            adata.obs[key] = adata.obs[key].astype("category")

    # Group indices by combinations of strata_keys for efficient access
    groups = adata.obs.groupby(strata_keys, observed=False).indices

    # Adjust group keys to always be tuples
    if len(strata_keys) == 1:
        groups = {(k,): v for k, v in groups.items()}

    # Initialize the dictionary to store subsets
    adata_dict = {}

    # Iterate over desired strata (tuples) and extract subsets
    for stratum in desired_strata:
        if stratum in groups:
            indices = groups[stratum]
            adata_dict[stratum] = adata[indices].copy()
        else:
            if print_missing_strata:
                print(
                    f"Warning: {stratum} is not a valid combination in {strata_keys}."
                )

    # Create AdataDict and set hierarchy to strata_keys
    adata_dict = AdataDict(adata_dict, tuple(strata_keys))
    return adata_dict


def concatenate_adata_dict(adata_dict, new_col_name=None, **kwargs):
    """
    Concatenates all AnnData objects in adata_dict into a single AnnData object.
    If only a single AnnData object is present, returns it as is.

    Parameters:
    - adata_dict (dict): Dictionary of AnnData objects with keys as identifiers.
    - new_col_name (str): If provided, the name of the new column that will store the adata_dict key in .obs of the concatenated adata. Defaults to None.
    - kwargs: Additional keyword arguments for concatenation.

    Returns:
    - AnnData: A single AnnData object or the original AnnData object if only one is provided. The .obs will contain a new column specifying the key of the adata of origin.
    """
    kwargs.setdefault("join", "outer")
    kwargs.setdefault("index_unique", None)  # Ensure original indices are kept

    adatas = list(adata_dict.values())

    # add the key to the obs to keep track after merging
    def add_key_to_obs_adata_dict(adata_dict, new_col_name=new_col_name):
        def add_key_to_obs_adata(adata, new_col_name=new_col_name, adt_key=None):
            adata.obs[new_col_name] = [adt_key] * adata.n_obs

        adata_dict_fapply(adata_dict, add_key_to_obs_adata)

    if new_col_name:
        add_key_to_obs_adata_dict(adata_dict)

    if len(adatas) == 1:
        return adatas[0]  # Return the single AnnData object as is

    if adatas:
        return sc.concat(adatas, **kwargs)
    else:
        raise ValueError("adata_dict is empty. No data available to concatenate.")
    
def check_and_create_strata(adata, strata_keys):
    """
    Checks if the specified stratifying variables are present in the AnnData object,
    and creates a new column combining these variables if it does not already exist.

    Parameters:
    adata : (AnnData) An AnnData object.
    strata_keys : (list of str) List of keys (column names) in adata.obs to be used for stratification.

    Returns:
    str: (str) The name of the newly created or verified existing combined strata column.

    Raises:
    ValueError: If one or more of the specified stratifying variables do not exist in adata.obs.
    """
    # Check if any of the strata_keys are not present in adata.obs
    if any(key not in adata.obs.columns for key in strata_keys):
        raise ValueError("one or more of your stratifying variables does not exist in adata.obs")
    
    # Create a new column that combines the values of existing strata_keys, if not already present
    strata_key = '_'.join(strata_keys)
    if strata_key not in adata.obs.columns:
        adata.obs[strata_key] = adata.obs[strata_keys].astype(str).agg('_'.join, axis=1).astype('category')
    else:
        #make sure it's categorical
        adata.obs[strata_key] = adata.obs[strata_key].astype('category')

    return strata_key

