def mergeSort(nums):
    """
    Sort the list using Merge Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(nums) <= 1:
        return nums
    
    # Divide the array into two halves
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.

    Args:
        left (list): The left sorted list.
        right (list): The right sorted list.

    Returns:
        list: The merged sorted list.
    """
    sorted_list = []
    i = j = 0
    
    # Compare elements from both lists and add the smaller one to sorted_list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Append remaining elements from both lists (if any)
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list
