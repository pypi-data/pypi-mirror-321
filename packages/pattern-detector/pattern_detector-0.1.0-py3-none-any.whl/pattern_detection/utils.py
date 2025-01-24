import numpy as np
from scipy.stats import skew, kurtosis

def calculate_statistics(data):
    """
    Calculate various statistics for a given dataset.

    Parameters:
    - data (array-like): The input data.

    Returns:
    - dict: Dictionary containing max, min, mean, std, skewness, and kurtosis.
    """
    return {
        "max": np.max(data),
        "min": np.min(data),
        "mean": np.mean(data),
        "std": np.std(data),
        "skewness": skew(data),
        "kurtosis": kurtosis(data),
    }

def normalize_data(data):
    """
    Normalize the input data to range [0, 1].

    Parameters:
    - data (array-like): Input data to normalize.

    Returns:
    - np.ndarray: Normalized data.
    """
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val)

def validate_window(window, constraints):
    """
    Validate a sliding window against constraints.

    Parameters:
    - window (array-like): The input window data.
    - constraints (dict): A dictionary of constraints with keys like 'max_pos', 'min_pos', etc.

    Returns:
    - bool: True if all constraints are satisfied, False otherwise.
    """
    corr_coef = np.corrcoef(window, constraints['pattern'])[0, 1]

    return (
        np.max(window) <= constraints["max_pos"]
        and np.min(window) >= constraints["min_pos"]
        and constraints["mean_pos_upper"] >= np.mean(window) >= constraints["mean_pos_lower"]
        and abs(skew(window) - constraints["pattern_skewness"]) < 0.5
        and abs(kurtosis(window) - constraints["pattern_kurtosis"]) < 1.0
        and constraints["pattern_std"] * 0.9 <= np.std(window) <= constraints["pattern_std"] * 1.1
        and corr_coef >= constraints["cross_correlation_threshold"]
        and constraints["starting_point_lower"] <= window[0] <= constraints["starting_point_upper"]
        and constraints["ending_point_lower"] <= window[-1] <= constraints["ending_point_upper"]
    )

def calculate_correlation(data1, data2):
    """
    Calculate correlation coefficient between two datasets.

    Parameters:
    - data1 (array-like): First dataset.
    - data2 (array-like): Second dataset.

    Returns:
    - float: Correlation coefficient.
    """
    return np.corrcoef(data1, data2)[0, 1]

def bin_data(data, bin_size):
    """
    Bin the data into averages over fixed-size intervals.

    Parameters:
    - data (array-like): The input data.
    - bin_size (int): The size of the bins.

    Returns:
    - np.ndarray: Binned data.
    """
    binned = data[:len(data) // bin_size * bin_size].reshape(-1, bin_size)
    return np.mean(binned, axis=1)
