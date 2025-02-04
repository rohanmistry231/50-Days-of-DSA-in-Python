def knap_sack(max_weight, weights, values, n):
    """
    Solve the 0/1 Knapsack problem using memoization.

    This function calculates the maximum value that can be obtained by including 
    or excluding items in the knapsack, such that the total weight does not exceed 
    the given maximum weight. Memoization is used to store the results of subproblems 
    to avoid redundant calculations.

    Args:
        max_weight (int): The maximum weight capacity of the knapsack.
        weights (list[int]): A list of integers representing the weight of each item.
        values (list[int]): A list of integers representing the value of each item.
        n (int): The total number of items.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    dp = [[-1] * (max_weight + 1) for _ in range(n)]

    def helper(index, remaining_weight):
        """
        Helper function to solve the problem using memoization.

        Args:
            index (int): The current item being considered.
            remaining_weight (int): The remaining weight capacity of the knapsack.

        Returns:
            int: The maximum value that can be obtained from the current item onward.
        """
        # Base case: if all items have been considered or remaining weight is 0
        if index >= n or remaining_weight == 0:
            return 0

        # Check if the result has already been computed
        if dp[index][remaining_weight] != -1:
            return dp[index][remaining_weight]

        # Recursive case: either exclude the current item or include it
        exclude = helper(index + 1, remaining_weight)
        include = 0
        if weights[index] <= remaining_weight:
            include = values[index] + helper(index + 1, remaining_weight - weights[index])

        dp[index][remaining_weight] = max(exclude, include)
        return dp[index][remaining_weight]

    return helper(0, max_weight)
