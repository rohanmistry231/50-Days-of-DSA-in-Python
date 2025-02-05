def isIsomorphic(s, t):
    """
    Check if two strings are isomorphic using hash tables.

    Args:
        s (str): The first input string.
        t (str): The second input string.

    Returns:
        bool: True if the strings are isomorphic, otherwise False.
    """
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_map:
            if s_map[char_s] != char_t:
                return False
        else:
            s_map[char_s] = char_t

        if char_t in t_map:
            if t_map[char_t] != char_s:
                return False
        else:
            t_map[char_t] = char_s

    return True
