def binarySearch(nums, target):
    """
    Perform binary search to find the target value in a sorted array.

    Args:
        nums (list): A sorted list of integers.
        target (int): The target value to search for.

    Returns:
        int: The index of the target value, or -1 if not found.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
