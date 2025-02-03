def findLongestChain(pairs):
    """
    Find the maximum length of a pair chain.

    Args:
        pairs (list of tuple): A list of pairs where each pair is represented as a tuple `(a, b)`.
                               The goal is to find the maximum number of pairs (a, b) such that for any two pairs 
                               `(a1, b1)` and `(a2, b2)` in the chain, the condition `b1 < a2` holds true.

    Returns:
        int: The maximum length of the pair chain that can be formed.

    The approach is similar to the Longest Increasing Subsequence (LIS) problem, but instead of comparing individual 
    elements, we compare pairs. The steps are as follows:
        1. Sort the pairs by their first element. This allows us to try and form chains by looking at the 
           second element of the pairs.
        2. Use dynamic programming to store the length of the longest chain ending with each pair.
        3. For each pair `i`, check all previous pairs `j` (where `j < i`) and see if pair `i` can follow pair `j`
           (i.e., if `pairs[j][1] < pairs[i][0]`), and update the maximum chain length accordingly.
        4. The final result will be the maximum value found in the dynamic programming array.

    Example:
        For `pairs = [[1, 2], [2, 3], [3, 4]]`, the function returns `2` as the longest chain is `[1, 2] -> [3, 4]`.

    Time Complexity:
        The time complexity is `O(n^2)`, where `n` is the number of pairs. The pairs are sorted in `O(n log n)`,
        and then we check each pair against all previous pairs in the list in the nested loop.
    """
    n = len(pairs)
    
    # Sort the pairs based on their first element
    pairs.sort()

    # dp[i] will hold the length of the longest chain ending with the i-th pair
    dp = [1] * n
    res = 1  # Initialize the result as 1 (at least one pair can be selected)

    # Iterate over the pairs and compute the maximum chain length
    for i in range(1, n):
        for j in range(i):
            # If the second element of pair j is less than the first element of pair i,
            # they can form a valid chain
            if pairs[j][1] < pairs[i][0] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        
        # Update the result with the maximum chain length so far
        if dp[i] > res:
            res = dp[i]
    
    return res
