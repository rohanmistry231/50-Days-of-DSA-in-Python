def nums_same_consec_diff(n, k):
    result = []

    def backtrack(num, length):
        if length == n:
            result.append(num)
            return

        last_digit = num % 10
        # Add the next possible digits based on the difference k
        if last_digit + k < 10:
            backtrack(num * 10 + last_digit + k, length + 1)
        if last_digit - k >= 0 and k != 0:
            backtrack(num * 10 + last_digit - k, length + 1)

    # Try starting from all digits from 1 to 9 (since the number cannot start with 0)
    for i in range(1, 10):
        backtrack(i, 1)

    return result

# Example:
print(nums_same_consec_diff(3, 7))  # Output: [181, 292, 707, 818, 929]
