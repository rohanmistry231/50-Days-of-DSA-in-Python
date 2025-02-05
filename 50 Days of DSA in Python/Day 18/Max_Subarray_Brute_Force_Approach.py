def max_subarray_brute_force(nums):
    """
    Find the maximum subarray sum using brute force.
    
    Args:
        nums (list): List of integers.
    
    Returns:
        int: Maximum subarray sum.
    """
    max_sum = float('-inf')
    n = len(nums)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum
