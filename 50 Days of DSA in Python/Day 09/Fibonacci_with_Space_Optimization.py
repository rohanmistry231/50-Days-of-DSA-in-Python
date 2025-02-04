# Solution 4: Fibonacci using Space Optimization

def fibonacci(n):
    """
    Calculate the Fibonacci number at the nth position using a space-optimized approach.

    Parameters:
    n (int): The position in the Fibonacci sequence to compute.

    Returns:
    int: The Fibonacci number at position n.
    
    Time Complexity: O(n)
        - A single loop runs from 1 to n-1.
    Space Complexity: O(1)
        - Only constant space is used for variables.
    """
    # Handle base cases directly
    if n <= 1:
        return n

    # Initialize variables to store the last two Fibonacci numbers
    prev = 0  # Represents F(n-2)
    curr = 1  # Represents F(n-1)

    # Calculate Fibonacci numbers iteratively
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number
        next_num = prev + curr

        # Update variables
        prev = curr
        curr = next_num

    # Return the nth Fibonacci number
    return curr
