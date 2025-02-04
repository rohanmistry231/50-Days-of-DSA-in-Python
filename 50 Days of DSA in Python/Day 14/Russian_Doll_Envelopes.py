def maxEnvelopes(envelopes):
    """
    Find the maximum number of envelopes that can be Russian-dolled (nested).

    Args:
        envelopes (list of tuple): A list of envelopes represented as pairs of integers (width, height). 
                                   The goal is to find the maximum number of envelopes that can be nested such 
                                   that each envelope is strictly larger than the previous one in both width and height.

    Returns:
        int: The maximum number of envelopes that can be Russian-dolled (nested).

    The idea is to first sort the envelopes by width and then, for envelopes with the same width, 
    sort them by height in descending order. This way, we ensure that no two envelopes with the same 
    width can be part of the same chain.
    
    Once sorted, the problem reduces to finding the longest increasing subsequence (LIS) based on the height 
    of the envelopes.

    Example:
        For `envelopes = [[5,4], [6,4], [6,7], [2,3]]`, the function returns `3` because the envelopes 
        that can be nested are `[2,3] -> [5,4] -> [6,7]`.

    Time Complexity:
        The time complexity is `O(n log n)`, where `n` is the number of envelopes. The sorting step takes `O(n log n)`,
        and finding the longest increasing subsequence using binary search takes `O(n log n)` as well.
    """
    # Step 1: Sort envelopes by width in ascending order, 
    # and by height in descending order if widths are the same.
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    n = len(envelopes)
    
    # Step 2: Find the longest increasing subsequence of heights using binary search
    sub = [envelopes[0][1]]  # Start with the first envelope's height

    def binary_search(sub, num):
        left, right = 0, len(sub)
        while left < right:
            mid = (left + right) // 2
            if num > sub[mid]:
                left = mid + 1
            else:
                right = mid
        return left
    
    # Iterate through the envelopes and update the subsequence
    for i in range(1, n):
        num = envelopes[i][1]  # Get the height of the current envelope
        if num > sub[-1]:
            sub.append(num)  # Add to subsequence if it's larger than the last element
        else:
            x = binary_search(sub, num)  # Find the correct position to replace
            sub[x] = num  # Update the subsequence with the smaller number

    return len(sub)  # The length of the subsequence gives the number of envelopes that can be nested
