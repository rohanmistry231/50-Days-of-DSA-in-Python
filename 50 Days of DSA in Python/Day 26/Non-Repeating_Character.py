def firstUniqChar(s):
    """
    Find the first non-repeating character in the string using a hash table.

    Args:
        s (str): The input string.

    Returns:
        int: The index of the first non-repeating character, or -1 if none exists.
    """
    freq = {}
    
    # Count the frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find the first character with frequency 1
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1
