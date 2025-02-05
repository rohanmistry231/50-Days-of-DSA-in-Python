def rotate(nums, k):
    """
    Rotate the array to the right by k steps.

    Args:
        nums (list): The list of integers to rotate.
        k (int): The number of positions to rotate.

    Returns:
        None: The function modifies the list in-place.
    """
    n = len(nums)
    k = k % n  # Handle cases where k is greater than the length of the array
    nums[:] = nums[-k:] + nums[:-k]
