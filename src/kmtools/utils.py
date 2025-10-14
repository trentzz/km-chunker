import sys
import time


class Utils:
    """Utility functions for logging, timing, and other shared operations."""

    @staticmethod
    def log(message: str, verbose: bool = False):
        """Print a message if verbose mode is enabled."""
        if verbose:
            print(message, file=sys.stderr, flush=True)

    @staticmethod
    def time_it(label: str, func, *args, verbose=False, **kwargs):
        """Time execution of a function."""
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        if verbose:
            Utils.log(f"{label} completed in {end - start:.2f}s", verbose)
        return result
