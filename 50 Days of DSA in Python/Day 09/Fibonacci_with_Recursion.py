def fibonacci(n):
    """
    Calculate the Fibonacci number at the nth position using recursion.

    Parameters:
    n (int): The position in the Fibonacci sequence to compute.

    Returns:
    int: The Fibonacci number at position n.
    
    Time Complexity: O(2^n) 
        - Due to the exponential growth of recursive calls.
    Space Complexity: O(n)
        - The space required for the recursion stack is proportional to the depth of the recursion tree.
    """
    # Base cases: Return n if it's 0 or 1.
    if n <= 1:
        return n

    # Recursive case: Compute Fibonacci(n-1) + Fibonacci(n-2).
    return fibonacci(n - 1) + fibonacci(n - 2)
