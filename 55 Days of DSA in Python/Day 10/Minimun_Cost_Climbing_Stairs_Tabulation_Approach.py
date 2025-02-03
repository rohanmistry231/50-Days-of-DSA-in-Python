from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    """
    Calculate the minimum cost to climb to the top of the stairs using a tabulation approach.

    Args:
        cost (List[int]): List where each element represents the cost of stepping on the corresponding stair.

    Returns:
        int: Minimum cost to reach the top of the stairs.
    """
    n = len(cost)

    # Array to store the minimum cost to reach each stair index.
    dp: List[int] = [-1] * (n + 1)

    # Initialize base cases.
    dp[0] = 0  # Starting from the ground (before the first step).
    dp[1] = 0  # Starting from the first step.

    # Iterate from the 2nd step to the top, calculating the cost to reach each step.
    for i in range(2, n + 1):
        # Option 1: Cost to reach the current step from the previous step.
        one_step_cost = cost[i - 1] + dp[i - 1]

        # Option 2: Cost to reach the current step from two steps back.
        two_step_cost = cost[i - 2] + dp[i - 2]

        # Store the minimum cost to reach this step.
        dp[i] = min(one_step_cost, two_step_cost)

    # The last element in the array represents the minimum cost to reach the top.
    return dp[n]


# Space Complexity: O(n) - For the `dp` array storing costs for each stair index.
# Time Complexity: O(n) - Linear iteration through the `cost` array.
