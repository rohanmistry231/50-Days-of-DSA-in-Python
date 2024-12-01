"""
This module provides two methods to solve the problem of returning an array of squared values
from a sorted array, with the squares sorted in ascending order.
"""

from typing import List


def sorted_squares_brute_force(array: List[int]) -> List[int]:
    """
    Computes the squares of each element in the input array and returns a sorted array
    using the brute force method.

    Steps:
    1. Compute the square of each element.
    2. Use Python's built-in sorting to sort the squared values.

    Args:
        array (List[int]): A sorted array of integers.

    Returns:
        List[int]: A sorted array of squared integers.
    """
    n = len(array)
    res = [0] * n  # Initialize result array
    for i in range(n):
        res[i] = array[i] ** 2  # Square each element
    res.sort()  # Sort the squared elements
    return res


def sorted_squares_two_pointer(array: List[int]) -> List[int]:
    """
    Computes the squares of each element in the input array and returns a sorted array
    using the optimized two-pointer method.

    Steps:
    1. Use two pointers to traverse the array from both ends.
    2. Compare absolute values, assign the larger square to the output array from the end.

    Args:
        array (List[int]): A sorted array of integers.

    Returns:
        List[int]: A sorted array of squared integers.
    """
    n = len(array)
    res = [0] * n  # Initialize result array
    left, right = 0, n - 1  # Set two pointers
    for k in range(n - 1, -1, -1):
        if abs(array[left]) > abs(array[right]):
            res[k] = array[left] ** 2
            left += 1
        else:
            res[k] = array[right] ** 2
            right -= 1
    return res


if __name__ == "__main__":
    # Example array
    input_array = [-7, -3, 2, 3, 11]

    # Brute force solution
    brute_force_result = sorted_squares_brute_force(input_array)
    print("Brute Force Result:", brute_force_result)

    # Optimized two-pointer solution
    two_pointer_result = sorted_squares_two_pointer(input_array)
    print("Two Pointer Result:", two_pointer_result)
