from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    """
    Calculate the minimum cost to climb to the top of the stairs using a memorization approach.
    
    Args:
        cost (List[int]): List where each element represents the cost of stepping on the corresponding stair.

    Returns:
        int: Minimum cost to reach the top of the stairs.
    """
    n = len(cost)
    
    # Memoization array to store the minimum cost for each stair.
    memo: List[int] = [-1] * n

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

        # If the result for the current index is already computed, return it.
        if memo[index] != -1:
            return memo[index]

        # Option 1: Climb one step to the next stair.
        one_step_cost = cost[index] + helper(index + 1)
        
        # Option 2: Climb two steps to the stair after the next.
        two_step_cost = cost[index] + helper(index + 2)
        
        # Store the minimum cost in the memo array and return it.
        memo[index] = min(one_step_cost, two_step_cost)
        return memo[index]

    # Start from either the first or the second stair and take the minimum cost.
    return min(helper(0), helper(1))


# Space Complexity: O(n) - For the memoization array and recursion stack.
# Time Complexity: O(n) - Each stair index is computed only once.
