def max_product_subarray(nums):
    """
    Find the maximum product subarray using dynamic programming.
    
    Args:
        nums (list): List of integers.
    
    Returns:
        int: Maximum product subarray.
    """
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result
