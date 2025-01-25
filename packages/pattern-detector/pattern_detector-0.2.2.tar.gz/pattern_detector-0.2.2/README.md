## Pattern Detector
pattern_detector is a Python library for detecting patterns in 1-D time-series data using advanced sliding window and similarity computations.

## Suggestion of use
Pattern selection is a crucial step for pattern detection algorithms. Try to select stationary start and end points in your signal for sample pattern.

## Installation
pip install pattern_detector

## Example Usage

import pattern_detector

df = pattern_detector(df, pattern, "column_name_of_pattern")