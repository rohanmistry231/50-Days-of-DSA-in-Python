def max_subarray_kadane(nums):
    """
    Find the maximum subarray sum using Kadane's Algorithm.
    
    Args:
        nums (list): List of integers.
    
    Returns:
        int: Maximum subarray sum.
    """
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
