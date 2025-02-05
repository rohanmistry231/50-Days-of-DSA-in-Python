def isPalindrome(s):
    """
    Check if the string is a palindrome using two pointers.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, otherwise False.
    """
    s = ''.join(char.lower() for char in s if char.isalnum())  # Remove non-alphanumeric characters and lowercase
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
