"""
This module provides a solution to check whether a given array is monotonic.
A monotonic array is one that is either entirely non-increasing or non-decreasing.
"""

from typing import List


def is_monotonic(array: List[int]) -> bool:
    """
    Determines if the given array is monotonic.

    An array is monotonic if:
    - It is monotone increasing (every element is greater than or equal to the previous one).
    - It is monotone decreasing (every element is less than or equal to the previous one).

    Steps:
    1. Check if the array is non-decreasing.
    2. Check if the array is non-increasing.
    3. If either condition is true, return True; otherwise, return False.

    Args:
        array (List[int]): The input array to check.

    Returns:
        bool: True if the array is monotonic, False otherwise.
    """
    n = len(array)

    if n == 0:
        return True  # An empty array is monotonic by definition

    # Flags for monotonic properties
    is_increasing = True
    is_decreasing = True

    for i in range(1, n):
        if array[i] > array[i - 1]:
            is_decreasing = False
        if array[i] < array[i - 1]:
            is_increasing = False

    return is_increasing or is_decreasing


if __name__ == "__main__":
    # Example arrays
    test_array_1 = [1, 2, 2, 3]  # Monotone increasing
    test_array_2 = [6, 5, 4, 4]  # Monotone decreasing
    test_array_3 = [1, 3, 2]  # Not monotonic
    test_array_4 = []  # Edge case: Empty array

    # Check monotonicity
    print(f"Array: {test_array_1} -> Monotonic: {is_monotonic(test_array_1)}")
    print(f"Array: {test_array_2} -> Monotonic: {is_monotonic(test_array_2)}")
    print(f"Array: {test_array_3} -> Monotonic: {is_monotonic(test_array_3)}")
    print(f"Array: {test_array_4} -> Monotonic: {is_monotonic(test_array_4)}")
