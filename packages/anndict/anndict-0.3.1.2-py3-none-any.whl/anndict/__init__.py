"""
Main init for anndictionary.
If on Mac, runs a multithreading configuration check before allowing import.
"""
import os
import platform
import sys
import numba  # Import numba to interact with its threading layer

#import AnnDictionary namespace
from . import utils
from . import adata_dict
from . import llm
from . import wrappers
from . import annotate
from . import automated_label_management
from . import visualize


# Run mac system check for multithreading compatibility
if platform.system() == "Darwin":
    try:
        numba.config.THREADING_LAYER = 'tbb'
        # numba.set_num_threads(2)

        @numba.jit(nopython=True, parallel=True)
        def _test_func():
            acc = 0
            for i in numba.prange(4):
                acc += i
            return acc

        _test_func()
        if numba.config.THREADING_LAYER != 'tbb':
            raise RuntimeError("Expected TBB threading layer, got something else.")

    except Exception:
        # Print only our custom error and exit; no traceback will be shown.
        sys.tracebacklimit = 0  # Suppress traceback
        raise RuntimeError(
            "Failed to initialize TBB threading layer on macOS!\n"
            "Try re-installing numba + TBB via conda (run exactly these 3 lines of code):\n"
            "  pip uninstall tbb numba\n"
            "  conda remove tbb numba\n"
            "  conda install -c conda-forge tbb numba\n"
            "Then restart python and re-attempt import\n"
        ) from None


# Run mac system configuration for multithreading
if platform.system() == 'Darwin':
    # Set Numba threading layer to 'tbb'
    if os.getenv("NUMBA_THREADING_LAYER") is None:
        os.environ["NUMBA_THREADING_LAYER"] = "tbb"
        numba.config.THREADING_LAYER = 'tbb'  # Explicitly set the threading layer using config
