def knap_sack(max_weight, weights, values, n):
    """
    Solve the 0/1 Knapsack problem using tabulation.

    This function calculates the maximum value that can be obtained by including 
    or excluding items in the knapsack, such that the total weight does not exceed 
    the given maximum weight. The solution is built iteratively using a DP table.

    Args:
        max_weight (int): The maximum weight capacity of the knapsack.
        weights (list[int]): A list of integers representing the weight of each item.
        values (list[int]): A list of integers representing the value of each item.
        n (int): The total number of items.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    # Create a DP table where dp[i][j] represents the maximum value for the first i items
    # with a weight limit of j
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            # Exclude the current item
            exclude = dp[i - 1][j]
            include = 0
            # Include the current item if it fits in the remaining weight capacity
            if weights[i - 1] <= j:
                include = values[i - 1] + dp[i - 1][j - weights[i - 1]]

            dp[i][j] = max(exclude, include)

    return dp[n][max_weight]
