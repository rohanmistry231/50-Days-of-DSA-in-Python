def quickSort(nums):
    """
    Sort the list using Quick Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(nums) <= 1:
        return nums

    # Select the pivot (last element in the array)
    pivot = nums[-1]
    left = []
    right = []
    
    # Partition the list into left (smaller than pivot) and right (greater than pivot)
    for num in nums[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    
    # Recursively apply quickSort to the left and right subarrays
    return quickSort(left) + [pivot] + quickSort(right)
