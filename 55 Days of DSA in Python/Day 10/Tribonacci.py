def tribonacci(n: int) -> int:
    """
    Calculate the n-th Tribonacci number using space optimization.

    Tribonacci sequence:
    - T(0) = 0, T(1) = 1, T(2) = 1
    - T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3

    Args:
        n (int): The index of the Tribonacci number to compute.

    Returns:
        int: The n-th Tribonacci number.
    """
    # Base cases
    if n == 0: 
        return 0
    if n == 1 or n == 2: 
        return 1

    # Initialize variables for T(n-3), T(n-2), and T(n-1)
    trib_n_minus_3: int = 0  # T(0)
    trib_n_minus_2: int = 1  # T(1)
    trib_n_minus_1: int = 1  # T(2)

    # Compute T(n) iteratively
    for i in range(3, n + 1):
        # Calculate the current Tribonacci number
        trib_n: int = trib_n_minus_3 + trib_n_minus_2 + trib_n_minus_1

        # Update the previous values
        trib_n_minus_3, trib_n_minus_2, trib_n_minus_1 = trib_n_minus_2, trib_n_minus_1, trib_n

    return trib_n


# Space Complexity: O(1) - Only a fixed number of variables are used regardless of `n`.
# Time Complexity: O(n) - A single loop from 3 to `n` (inclusive).
