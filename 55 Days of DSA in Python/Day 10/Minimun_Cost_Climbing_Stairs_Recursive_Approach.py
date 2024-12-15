from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    """
    Calculate the minimum cost to climb to the top of the stairs.
    
    Args:
        cost (List[int]): List where each element represents the cost of stepping on the corresponding stair.

    Returns:
        int: Minimum cost to reach the top of the stairs.
    """
    n = len(cost)

    def helper(index: int) -> int:
        """
        Recursive helper function to compute the minimum cost starting at a given stair index.
        
        Args:
            index (int): Current stair index.

        Returns:
            int: Minimum cost from the current stair to the top.
        """
        # Base case: If the index is beyond the last stair, the cost is 0.
        if index >= n:
            return 0

        # Option 1: Climb one step to the next stair.
        one_step_cost = cost[index] + helper(index + 1)
        
        # Option 2: Climb two steps to the stair after the next.
        two_step_cost = cost[index] + helper(index + 2)
        
        # Return the minimum cost of the two options.
        return min(one_step_cost, two_step_cost)

    # Start from either the first or the second stair and take the minimum cost.
    return min(helper(0), helper(1))


# Space Complexity: O(n) - Due to the recursion stack for calls up to `n`.
# Time Complexity: O(2^n) - Recursive solution with overlapping subproblems.
