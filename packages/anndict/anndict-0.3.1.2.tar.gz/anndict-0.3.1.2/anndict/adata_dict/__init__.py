"""
This module contains the core functions of AnnDictionary. This includes:

- The AdataDict class
- functions to read, write, and build AdataDict objects
- functions to iterate over AdataDict objects
"""

from .adata_dict import (  # type: ignore
    AdataDict,
    to_nested_tuple
)

from .adata_dict_fapply import (  # type: ignore
    adata_dict_fapply,
    adata_dict_fapply_return,
)

from .read_write_build import (  # type: ignore
    #read and write AdataDict class
    read_adata_dict,
    write_adata_dict,

    #read h5ads directly into an AdataDict class
    read_adata_dict_from_h5ad,

    #a catch all to read h5ads and AdataDicts all in one go
    read,

    #build an AdataDict from an adata in memory
    build_adata_dict,

    #concatenate an AdataDict into a single adata
    concatenate_adata_dict,

    #move this function somewhere else
    check_and_create_strata
)

__all__ = [
    "AdataDict",
    "to_nested_tuple",
    "adata_dict_fapply",
    "adata_dict_fapply_return",
    "read_adata_dict",
    "write_adata_dict",
    "read_adata_dict_from_h5ad",
    "read",
    "build_adata_dict",
    "concatenate_adata_dict",
    "check_and_create_strata"
]