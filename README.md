# [Advent of Code 2023](https://adventofcode.com/2023)

- [Day 1: Trebuchet?!](day01-trebuchet)

## Python Pytest General Framework

```python
import pytest
from my_module import my_function  # replace with your module and function

def test_my_function():
    # Arrange
    input = ...  # replace with your input
    expected_output = ...  # replace with your expected output

    # Act
    actual_output = my_function(input)

    # Assert
    assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output}"
```
