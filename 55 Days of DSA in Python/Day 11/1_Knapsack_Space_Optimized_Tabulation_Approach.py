def knap_sack(max_weight, weights, values, n):
    """
    Solve the 0/1 Knapsack problem using space-optimized tabulation.

    This function calculates the maximum value that can be obtained by including 
    or excluding items in the knapsack, such that the total weight does not exceed 
    the given maximum weight. The space complexity is optimized by using only two arrays 
    to store the results of the previous and current rows.

    Args:
        max_weight (int): The maximum weight capacity of the knapsack.
        weights (list[int]): A list of integers representing the weight of each item.
        values (list[int]): A list of integers representing the value of each item.
        n (int): The total number of items.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    # Initialize two arrays to store results for the previous and current items
    prev = [0] * (max_weight + 1)
    curr = [0] * (max_weight + 1)

    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            # Exclude the current item
            exclude = prev[j]
            include = 0
            # Include the current item if it fits in the remaining weight capacity
            if weights[i - 1] <= j:
                include = values[i - 1] + prev[j - weights[i - 1]]

            curr[j] = max(exclude, include)

        # Update prev to be the current row after each iteration
        prev = curr[:]

    return curr[max_weight]
