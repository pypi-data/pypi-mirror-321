try:
    from .aoi_finder import run_area_of_interest_finder
except ImportError:
    raise ImportError("The PatternDetector module could not be imported. Ensure all dependencies are installed.")

__version__ = "0.2.0"

def pattern_detector(data, pattern, column_pattern):
    """
    A simplified interface for using the PatternDetector class.

    Parameters:
    - data (pd.DataFrame): The main data.
    - pattern (pd.DataFrame): The pattern data.
    - column_pattern (str): The column name for pattern matching.

    Returns:
    - pd.DataFrame: The resulting DataFrame with detected cycles.
    """
    detector = run_area_of_interest_finder(data, pattern, column_pattern)
    return detector

# Replace the module with a callable version
import sys
from types import ModuleType

class CallableModule(ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.__version__ = __version__

    def __call__(self, data, pattern, column_pattern):
        return pattern_detector(data, pattern, column_pattern)

# Replace the current module in sys.modules with the callable version
sys.modules[__name__] = CallableModule(__name__)
