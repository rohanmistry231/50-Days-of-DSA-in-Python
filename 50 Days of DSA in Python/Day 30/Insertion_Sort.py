def insertionSort(nums):
    """
    Sort the list using Insertion Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        
        # Move elements of nums[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = key
    
    return nums
