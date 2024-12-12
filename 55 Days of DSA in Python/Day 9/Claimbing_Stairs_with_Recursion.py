# Solution: Climbing Stairs using Recursion Approach

def climbStairs(n):
    """
    Calculate the number of distinct ways to climb to the top of a staircase with `n` steps,
    where each time you can climb 1 or 2 steps.

    Parameters:
    n (int): The total number of steps in the staircase.

    Returns:
    int: The number of distinct ways to climb to the top.
    
    Time Complexity: O(2^n)
        - Recursive tree has overlapping subproblems leading to exponential complexity.
    Space Complexity: O(n)
        - Stack space used for recursive calls.
    """
    # Handle small inputs directly
    if n <= 2:
        return n

    # Helper function to solve the subproblem recursively
    def helper(first, second, n, curr):
        """
        Recursive helper function to compute the number of ways.

        Parameters:
        first (int): Number of ways to reach the step before the current step.
        second (int): Number of ways to reach the current step.
        n (int): Total number of steps.
        curr (int): Current step being evaluated.

        Returns:
        int: Number of ways to reach the nth step.
        """
        # Subproblem computation
        next_num = first + second  # Total ways to reach the next step

        # Base condition: If we've reached the nth step
        if curr == n:
            return next_num

        # Recursive call for the next step
        return helper(second, next_num, n, curr + 1)

    # Start the recursion with the first two steps
    return helper(1, 2, n, 3)
