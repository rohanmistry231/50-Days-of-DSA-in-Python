def knap_sack(max_weight, weights, values, n):
    """
    Solve the 0/1 Knapsack problem using recursion.

    This function calculates the maximum value that can be obtained by including 
    or excluding items in the knapsack, such that the total weight does not exceed 
    the given maximum weight. It uses recursion to explore all possible combinations.

    Args:
        max_weight (int): The maximum weight capacity of the knapsack.
        weights (list[int]): A list of integers representing the weight of each item.
        values (list[int]): A list of integers representing the value of each item.
        n (int): The total number of items.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    def helper(index, remaining_weight):
        """
        Helper function to solve the problem recursively.

        Args:
            index (int): The current item being considered.
            remaining_weight (int): The remaining weight capacity of the knapsack.

        Returns:
            int: The maximum value that can be obtained from the current item onward.
        """
        # Base case: if all items have been considered or remaining weight is 0
        if index >= n or remaining_weight == 0:
            return 0

        # Recursive case: either exclude the current item or include it
        exclude = helper(index + 1, remaining_weight)
        include = 0
        if weights[index] <= remaining_weight:
            include = values[index] + helper(index + 1, remaining_weight - weights[index])

        return max(exclude, include)

    return helper(0, max_weight)
