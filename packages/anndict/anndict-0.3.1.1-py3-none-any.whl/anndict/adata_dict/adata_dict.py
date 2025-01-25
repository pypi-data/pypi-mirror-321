"""
This module contains the AdataDict class
"""
def to_nested_tuple(nested_list):
    """
    Recursively convert a nested list into a nested tuple.
    """
    if isinstance(nested_list, list):
        return tuple(to_nested_tuple(item) for item in nested_list)
    return nested_list


class AdataDict(dict):
    """
    AdataDict is a dictionary-like container where values are AnnData objects.

    This class provides two main functionalities:
    1. It behaves like an AnnData object by passing each method through to each AnnData in the dictionary.
    2. It has a method fapply(func, kwargs) that applies a given function func with arguments kwargs to each AnnData object in the dictionary.
    """

    def __init__(self, data=None, hierarchy=None):
        """
        Initialize the AdataDict with data and hierarchy.

        :param data: Dictionary with keys as tuples of indices.
        :param hierarchy: Tuple or list indicating the order of indices.
        """
        if data is None:
            data = {}
        super().__init__(data)  # Initialize the dict with data
        if hierarchy is not None:
            self._hierarchy = tuple(hierarchy)  # Tuple indicating the index hierarchy
        else:
            self._hierarchy = ()
    
    @property
    def hierarchy(self):
        return self._hierarchy

    def flatten(self, parent_key=()):
        flat_data = {}
        for key, value in self.items():
            full_key = parent_key + key
            if isinstance(value, AdataDict):
                flat_data.update(value.flatten(parent_key=full_key))
            else:
                flat_data[full_key] = value
        return flat_data

    def flatten_nesting_list(self, nesting_list):
        """
        Flatten a nested list or tuple into a single list.

        :param nesting_list: Nested list or tuple of hierarchy levels.
        :return: Flattened list of hierarchy elements.
        """
        hierarchy = []
        for item in nesting_list:
            if isinstance(item, (list, tuple)):
                hierarchy.extend(self.flatten_nesting_list(item))
            else:
                hierarchy.append(item)
        return hierarchy

    def get_levels(self, nesting_list, levels=None, depth=0):
        """
        Get the levels of hierarchy based on the nesting structure.

        :param nesting_list: Nested list indicating the new hierarchy structure.
        :param levels: List to store the levels.
        :param depth: Current depth in recursion.
        :return: List of levels with hierarchy elements.
        """
        if levels is None:
            levels = []
        if len(levels) <= depth:
            levels.append([])
        for item in nesting_list:
            if isinstance(item, list):
                self.get_levels(item, levels, depth + 1)
            else:
                levels[depth].append(item)
        return levels

    def set_hierarchy(self, nesting_list):
        """
        Rearrange the hierarchy of AdataDict based on the provided nesting structure.

        :param nesting_list: Nested list indicating the new hierarchy structure.
        """

        # Flatten the nested data
        flat_data = self.flatten()
        self.clear()
        self.update(flat_data)
        
        # Flatten and extract the current hierarchy
        self._hierarchy = tuple(self.flatten_nesting_list(self._hierarchy))
        
        # Flatten the new hierarchy
        new_hierarchy = self.flatten_nesting_list(nesting_list)
        
        # Get the levels of the nesting structure
        levels = self.get_levels(nesting_list)
        old_hierarchy = self._hierarchy

        # Function to recursively create nested AdataDicts
        def create_nested_adata_dict(current_level, key_indices, value, level_idx):
            if level_idx == len(levels):
                return value  # Base case: return the value (AnnData object)
            level = levels[level_idx]
            level_length = len(level)
            level_key = tuple(key_indices[:level_length])
            remaining_key_indices = key_indices[level_length:]
            if level_key not in current_level:
                # Remaining hierarchy for nested AdataDict
                remaining_hierarchy = levels[level_idx + 1 :] if level_idx + 1 < len(levels) else []
                current_level[level_key] = AdataDict(hierarchy=remaining_hierarchy)
            # Recurse into the next level
            nested_dict = current_level[level_key]
            nested_value = create_nested_adata_dict(nested_dict, remaining_key_indices, value, level_idx + 1)
            if level_idx == len(levels) - 1:
                # At the last level, set the value
                current_level[level_key] = nested_value
            return current_level

        # Start building the new nested AdataDict
        new_data = AdataDict(hierarchy=new_hierarchy)
        for key, value in flat_data.items():
            # Map old indices to their values
            index_map = dict(zip(old_hierarchy, key))
            # Arrange indices according to the new hierarchy
            new_key_indices = [index_map[h] for h in new_hierarchy]
            # Recursively build the nested structure
            create_nested_adata_dict(new_data, new_key_indices, value, 0)

        # Update the hierarchy and data
        self._hierarchy = to_nested_tuple(nesting_list)  # Update with the nested structure
        # Replace the existing data in self with new_data
        self.clear()
        self.update(new_data)

    def __getitem__(self, key):
        # Simplify access by converting non-tuple keys to tuple
        if not isinstance(key, tuple):
            key = (key,)
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        # Simplify setting by converting non-tuple keys to tuple
        if not isinstance(key, tuple):
            key = (key,)
        super().__setitem__(key, value)

    def __getattr__(self, attr):
        def method(*args, **kwargs):
            results = {}
            for key, adata in self.items():
                if isinstance(adata, AdataDict):
                    # Recurse into nested AdataDict
                    results[key] = getattr(adata, attr)(*args, **kwargs)
                else:
                    func = getattr(adata, attr)
                    results[key] = func(*args, **kwargs)
            return results
        return method

    def fapply(self, func, **kwargs):
        results = {}
        for key, adata in self.items():
            if isinstance(adata, AdataDict):
                # Recurse into nested AdataDict
                results[key] = adata.fapply(func, **kwargs)
            else:
                results[key] = func(adata, **kwargs)
        return results