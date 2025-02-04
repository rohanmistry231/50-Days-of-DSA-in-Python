"""Module to determine if a list can be partitioned into two subsets with equal sum."""
from typing import List

def can_partition(nums: List[int]) -> bool:
    """
    Determine if a list can be partitioned into two subsets with equal sum.

    Args:
        nums (List[int]): List of numbers.

    Returns:
        bool: True if the list can be partitioned, otherwise False.
    """
    n = len(nums)
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    prev = [False] * (target + 1)
    curr = [False] * (target + 1)
    prev[0] = True
    curr[0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Pick the element if it does not exceed the target sum
            if nums[i - 1] <= j:
                curr[j] = prev[j - nums[i - 1]]
            else:
                curr[j] = False    
            # Don't pick the element
            curr[j] = curr[j] or prev[j]
        
        prev = curr[:]
    
    return curr[target]
