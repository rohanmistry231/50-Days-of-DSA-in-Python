def max_product_subarray_brute_force(nums):
    """
    Find the maximum product subarray using brute force.
    
    Args:
        nums (list): List of integers.
    
    Returns:
        int: Maximum product subarray.
    """
    max_product = float('-inf')
    n = len(nums)
    
    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= nums[j]
            max_product = max(max_product, current_product)
    
    return max_product
