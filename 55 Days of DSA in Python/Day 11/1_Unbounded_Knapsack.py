def knap_sack(N, max_weight, values, weights):
    """
    Solve the Unbounded Knapsack problem using dynamic programming.

    In the Unbounded Knapsack problem, each item can be chosen multiple times 
    to maximize the total value of items that can be placed in the knapsack, 
    such that the total weight does not exceed the given maximum weight.

    Args:
        N (int): The number of items.
        max_weight (int): The maximum weight capacity of the knapsack.
        values (list[int]): A list of integers representing the value of each item.
        weights (list[int]): A list of integers representing the weight of each item.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    # Create a DP table where dp[i][j] represents the maximum value that can be obtained
    # with the first i items and a knapsack capacity of j
    dp = [[-1] * (max_weight + 1) for _ in range(N + 1)]
    
    # Initialize base cases: If there is no weight capacity or no items, max value is 0
    for j in range(max_weight + 1):
        dp[0][j] = 0  # No items, so no value can be obtained
    
    for i in range(N + 1):
        dp[i][0] = 0  # No capacity, so no value can be obtained

    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, max_weight + 1):
            # Exclude the current item
            exclude = dp[i - 1][j]
            include = 0
            # Include the current item if it fits within the remaining weight capacity
            if weights[i - 1] <= j:
                include = values[i - 1] + dp[i][j - weights[i - 1]]

            dp[i][j] = max(exclude, include)

    return dp[N][max_weight]
