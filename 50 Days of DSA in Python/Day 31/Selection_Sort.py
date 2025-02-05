def selectionSort(nums):
    """
    Sort the list using Selection Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(nums)
    
    # Traverse through all elements in the list
    for i in range(n):
        min_idx = i
        
        # Find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of unsorted part
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    
    return nums
