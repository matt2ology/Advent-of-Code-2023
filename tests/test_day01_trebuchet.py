"""Tests for day01_trebuchet.py."""
import pytest

from day01_trebuchet.day01 import sum_all_calibration_values


# Define the input files and expected results as tuples in a list
testdata = [
    ("../puzzle inputs/Day 1 Trebuchet/sample_input.txt", 142),
    # Add more test data as needed...
]


@pytest.mark.parametrize("input_file, expected_result", testdata)
def test_sum_all_calibration_values(input_file, expected_result):
    """Test sum_all_calibration_values function."""
    # Act (i.e., execute the function)
    result = sum_all_calibration_values(input_file)

    # Assert (i.e., check the result)
    assert result == expected_result, \
        f"Expected {expected_result}, but got {result}"
