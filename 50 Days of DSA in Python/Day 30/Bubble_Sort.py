def bubbleSort(nums):
    """
    Sort the list using Bubble Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(nums)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize: if no two elements were swapped in an inner loop, break early
        swapped = False
        
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        
        # If no two elements were swapped, the list is sorted
        if not swapped:
            break
            
    return nums
