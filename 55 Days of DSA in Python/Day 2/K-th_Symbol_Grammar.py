def kth_grammar(n, k):
    """
    Finds the k-th symbol in the n-th row of a specific grammar.

    Grammar Rules:
    - Row 1 (n = 1): "0"
    - Subsequent rows are formed as:
      - Replace each "0" with "01".
      - Replace each "1" with "10".
    - Example:
      - Row 1: "0"
      - Row 2: "01"
      - Row 3: "0110"
      - Row 4: "01101001"

    Args:
        n (int): The row number (1-indexed).
        k (int): The position of the symbol in the row (1-indexed).

    Returns:
        int: The k-th symbol in the nth row (0 or 1).

    Time Complexity:
        O(n): Each recursive call reduces the problem size by one.

    Space Complexity:
        O(n): Stack space due to recursion.
    """
    # Base case: the first row has only "0".
    if n == 1:
        return 0

    # Calculate the midpoint of the current row.
    mid = 2**(n - 2)

    # If k is in the first half, recurse into the previous row.
    if k <= mid:
        return kth_grammar(n - 1, k)

    # If k is in the second half, recurse with adjusted position and invert the result.
    return 1 - kth_grammar(n - 1, k - mid)


if __name__ == "__main__":
    # Example usage
    row_number = 4
    position = 5
    print(f"The {position}-th symbol in row {row_number} is: {kth_grammar(row_number, position)}")
