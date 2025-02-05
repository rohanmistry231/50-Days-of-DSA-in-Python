from typing import List

def can_jump(nums: List[int]) -> bool:
    """
    Determines if it is possible to reach the last index.
    
    Args:
        nums (list): List of integers representing jump distances.
    
    Returns:
        bool: True if reachable, False otherwise.
    """
    max_reach = 0
    n = len(nums)
    
    for i in range(n):
        if i > max_reach:
            return False  # Can't move past this point
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            return True  # Can reach or exceed the last index
    
    return False
