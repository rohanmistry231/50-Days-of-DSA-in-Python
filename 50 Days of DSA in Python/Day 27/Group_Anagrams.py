def groupAnagrams(strs):
    """
    Group the anagrams in the given list of strings.

    Args:
        strs (list): A list of strings.

    Returns:
        list: A list of lists containing grouped anagrams.
    """
    anagrams = {}

    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(s)

    return list(anagrams.values())
