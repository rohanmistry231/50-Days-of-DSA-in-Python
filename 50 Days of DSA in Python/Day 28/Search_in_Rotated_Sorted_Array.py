def search(nums, target):
    """
    Search for the target value in a rotated sorted array.

    Args:
        nums (list): A rotated sorted list of integers.
        target (int): The target value to search for.

    Returns:
        int: The index of the target value, or -1 if not found.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
