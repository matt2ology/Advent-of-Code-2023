# [Day 1: Trebuchet](https://adventofcode.com/2023/day/1)

**What is the sum of all of the calibration values?**

1. In [Day 1 input](<../puzzle inputs/Day 1 Trebuchet/input.txt>)
2. On each line, the **calibration value** can be found by combining the
   **first digit** and the **last digit** (in that order) to form a
   single **two-digit number**.

```example
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

The **calibration values** of these four lines are `12`, `38`, `15`, and `77`.
Adding these together produces **142**.

## Pytest notes

In general, if you need to test the same functionality with different inputs,
`@pytest.mark.parametrize` is preferred. If you need to perform common setup
tasks or share resources among multiple test methods within a class,
`@classmethod` is preferred.

In some cases, you might even use both decorators together, leveraging the
strengths of each to organize and structure your tests effectively.

### @pytest.mark.parametrize

```python
import pytest

# Define test data as a list of tuples
testdata = [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
]

@pytest.mark.parametrize("a, b, expected", testdata)
def test_addition(a, b, expected):
    """Test addition function."""
    result = a + b
    assert result == expected, f"Expected {expected}, but got {result}"
```

### @classmethod

```python
import pytest
from day01_trebuchet.day01 import sum_all_calibration_values

class TestSumAllCalibrationValues:
    """Test cases for sum_all_calibration_values function."""

    @classmethod
    def setup_class(cls):
        """Setup class method to initialize common resources."""
        cls.input_file = "../puzzle inputs/Day 1 Trebuchet/sample_input.txt"
        cls.expected_result = 142

    def test_sum_all_calibration_values_sample_input(self):
        """Test sum_all_calibration_values function with sample input."""
        # Act (i.e., execute the function)
        result = sum_all_calibration_values(self.input_file)

        # Assert (i.e., check the result)
        assert result == self.expected_result, \
            f"Expected {self.expected_result}, but got {result}"
```
