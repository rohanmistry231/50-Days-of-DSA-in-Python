# Solution 2: Fibonacci using Memoization

# Initialize a dictionary to store precomputed Fibonacci values.
memo = {0: 0, 1: 1}

def fibonacci(n):
    """
    Calculate the Fibonacci number at the nth position using memoization.

    Parameters:
    n (int): The position in the Fibonacci sequence to compute.

    Returns:
    int: The Fibonacci number at position n.
    
    Time Complexity: O(n)
        - Each Fibonacci number from 0 to n is computed once and stored.
    Space Complexity: O(n)
        - Space is used to store the memoization dictionary and recursion stack.
    """
    # Check if the result is already computed.
    if n in memo:
        return memo[n]
    
    # Compute and store the Fibonacci value in the dictionary.
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    
    return memo[n]
