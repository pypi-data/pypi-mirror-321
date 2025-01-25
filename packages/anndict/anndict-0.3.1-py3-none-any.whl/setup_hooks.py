"""
This setup 
"""
import platform
import sys
from setuptools.command.install import install

class InstallCommand(install):
    def run(self):
        # Only check TBB during actual package installation, not during build
        command = sys.argv[1] if len(sys.argv) > 1 else None
        if command == "install" and platform.system() == "Darwin":
            # MacOS-specific install requirements to make sure multithreading is possible
            try:
                import numba
                numba.config.THREADING_LAYER = 'tbb'
                # Try to actually initialize the threading layer
                @numba.jit
                def test_func():
                    return 1
                test_func()
            except Exception:
                sys.stderr.write("""
Error: TBB threading layer could not be initialized.

On macOS, please run these commands in your conda environment:
    pip uninstall tbb numba
    conda remove tbb numba
    conda install -c conda-forge tbb numba #need to conda install, pip won't work

Then try installing anndictionary again.
""")
                sys.exit(1)

        # If checks pass or we're not installing, proceed
        install.run(self)
