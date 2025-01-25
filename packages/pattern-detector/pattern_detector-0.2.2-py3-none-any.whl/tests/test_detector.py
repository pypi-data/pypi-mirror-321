import pytest
import numpy as np
import pandas as pd
from pattern_detector.aoi_finder import run_area_of_interest_finder

def test_preprocess_pattern():
    pattern = pd.DataFrame({"value": range(10)})
    detector = run_area_of_interest_finder(None, pattern, "value")
    detector.preprocess_pattern()
    assert detector.pattern1 is not None
    assert len(detector.pattern1) > 0

def test_calculate_similarity():
    data = pd.DataFrame({"value": range(100)})
    pattern = pd.DataFrame({"value": range(10)})
    detector = run_area_of_interest_finder(data, pattern, "value")
    detector.preprocess_pattern()
    detector.calculate_similarity()
    assert len(detector.similarity_dict) > 0

def test_find_area_of_interest():
    data = pd.DataFrame({"value": range(100)})
    pattern = pd.DataFrame({"value": range(10)})
    detector = run_area_of_interest_finder(data, pattern, "value")
    result = detector.find_area_of_interest()
    assert "cycle" in result.columns
    assert not result["cycle"].isnull().all()
