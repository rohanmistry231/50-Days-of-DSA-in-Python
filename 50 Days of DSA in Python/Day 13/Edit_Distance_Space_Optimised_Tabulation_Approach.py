def minDistance(word1, word2):
    """
    Calculate the minimum edit distance between two words using space optimized tabulation.

    Args:
        word1 (str): The first input word.
        word2 (str): The second input word.

    Returns:
        int: The minimum number of operations required to convert word1 to word2.
    """
    n = len(word1)
    m = len(word2)

    # Initialize two 1D arrays to store the previous and current rows of the DP table
    prev = [0] * (m + 1)  # Previous row
    curr = [0] * (m + 1)  # Current row

    # Base case: Fill the first row
    for j in range(m + 1):
        prev[j] = j

    # Fill the DP table row by row
    for i in range(1, n + 1):
        curr[0] = i  # The first element of the current row
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]  # No operation needed if characters match
            else:
                # Calculate the minimum number of operations
                replace = 1 + prev[j - 1]  # Replace character
                delete = 1 + prev[j]      # Delete character from word1
                insert = 1 + curr[j - 1]  # Insert character into word1
                curr[j] = min(delete, replace, insert)  # Choose the minimum operation

        # Update the previous row for the next iteration
        prev = curr[:]

    return prev[m]
