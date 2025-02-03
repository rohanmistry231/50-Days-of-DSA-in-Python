def minDistance(word1, word2):
    """
    Calculate the minimum edit distance between two words using recursion.

    Args:
        word1 (str): The first input word.
        word2 (str): The second input word.

    Returns:
        int: The minimum number of operations required to convert word1 to word2.
    """
    n = len(word1)
    m = len(word2)

    def number_of_operations(index1, index2):
        # Base case: if both words are fully processed
        if index1 > n - 1 and index2 > m - 1:
            return 0

        # If one word is exhausted, count remaining operations for the other word
        if index1 > n - 1:
            return m - index2
        if index2 > m - 1:
            return n - index1

        # If characters are the same, no operation is needed
        if word1[index1] == word2[index2]:
            return number_of_operations(index1 + 1, index2 + 1)

        # Try all three operations: insert, delete, and replace
        insert = 1 + number_of_operations(index1, index2 + 1)  # Insert character into word1
        delete = 1 + number_of_operations(index1 + 1, index2)  # Delete character from word1
        replace = 1 + number_of_operations(index1 + 1, index2 + 1)  # Replace character in word1

        return min(insert, delete, replace)  # Return the minimum of all operations

    return number_of_operations(0, 0)
