def minDistance(word1, word2):
    """
    Calculate the minimum edit distance between two words using memoization.

    Args:
        word1 (str): The first input word.
        word2 (str): The second input word.

    Returns:
        int: The minimum number of operations required to convert word1 to word2.
    """
    n = len(word1)
    m = len(word2)

    # Initialize memoization array with -1 (indicating uncomputed values)
    arr = [[-1] * m for _ in range(n)]

    def helper(index1, index2):
        # Base case: if one string is empty, return the length of the other string
        if index1 < 0: 
            return index2 + 1
        if index2 < 0:
            return index1 + 1

        # If the value is already computed, return the stored result
        if arr[index1][index2] != -1:
            return arr[index1][index2]

        # If characters match, no operation is needed, move to the next pair
        if word1[index1] == word2[index2]:
            arr[index1][index2] = helper(index1 - 1, index2 - 1)
            return arr[index1][index2]

        # Try all three operations: replace, delete, and insert
        replace = 1 + helper(index1 - 1, index2 - 1)  # Replace
        delete = 1 + helper(index1 - 1, index2)      # Delete
        insert = 1 + helper(index1, index2 - 1)      # Insert

        # Store the result of the minimum operation
        arr[index1][index2] = min(replace, delete, insert)
        return arr[index1][index2]

    return helper(n - 1, m - 1)
