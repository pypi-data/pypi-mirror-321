"""
Main init for anndictionary
"""

import os
import platform
import numba  # Import numba to interact with its threading layer


# Check if the operating system is macOS
if platform.system() == 'Darwin':
    # Set Numba threading layer to 'tbb'
    if os.getenv("NUMBA_THREADING_LAYER") is None:
        os.environ["NUMBA_THREADING_LAYER"] = "tbb"
        numba.config.THREADING_LAYER = 'tbb'  # Explicitly set the threading layer using config

from . import utils

from . import adata_dict

from . import llm

from . import wrappers

from . import annotate

from . import automated_label_management

from . import visualize
