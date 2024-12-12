# Solution 3: Fibonacci using Tabulation

def fibonacci(n):
    """
    Calculate the Fibonacci number at the nth position using the tabulation approach.

    Parameters:
    n (int): The position in the Fibonacci sequence to compute.

    Returns:
    int: The Fibonacci number at position n.
    
    Time Complexity: O(n)
        - A single loop runs from 2 to n.
    Space Complexity: O(n)
        - Space is used to store the entire DP table.
    """
    # Initialize the DP table to store Fibonacci numbers.
    dp = [0] * (n + 1)
    
    # Base cases
    if n > 0:
        dp[1] = 1

    # Fill the DP table iteratively.
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
